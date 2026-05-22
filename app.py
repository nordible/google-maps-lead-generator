import streamlit as st
import asyncio
import os
import pandas as pd
from io import BytesIO
from src.places_api import search_places, get_coordinates, get_sub_locations
from src.business_info import process_businesses
from src.data_export import save_places_to_excel
from src.utils import get_current_date
from dotenv import load_dotenv

load_dotenv(override=True)

# Set page config
st.set_page_config(
    page_title="Google Maps Lead Generator",
    page_icon="🔍",
    layout="wide"
)

# App title and description
st.title("AI-Powered Google Maps Lead Generator")
st.markdown(
    """
    This tool helps you generate leads from Google Maps by:
    1. Searching for businesses matching your criteria
    2. Extracting contact information from their websites
    3. Using AI to find emails and social media profiles
    
    **💡 Tip for high volume:** To get more than 260 leads, we've enabled **Automated Multi-Location Search**. 
    The tool will automatically break down your search into neighborhoods to bypass API limits.
    """
)

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    
    # API Keys
    st.subheader("API Keys")
    serper_api_key = st.text_input("Serper API Key", type="password", value=os.environ.get("SERPER_API_KEY", ""))
    openrouter_api_key = st.text_input("OpenRouter API Key", type="password", value=os.environ.get("OPENROUTER_API_KEY", ""))
    
    # LLM Model Settings
    st.subheader("LLM Model")
    llm_model = st.selectbox(
        "Select LLM Model",
        options=[
            "meta-llama/llama-3-8b-instruct",
            "openai/gpt-4o-mini",
            "openai/gpt-4.1-mini",
            "anthropic/claude-3-haiku",
            "anthropic/claude-3.5-sonnet",
            "deepseek/deepseek-chat",
            "mistral/mistral-large-2",
            "local-model"
        ],
        index=0,
    )
    
    llm_api_base = st.text_input("LLM API Base URL", value=os.environ.get("LLM_API_BASE", "https://openrouter.ai/api/v1"))
    
    # Save settings button
    if st.button("Save Settings"):
        # Temporarily set environment variables for this session
        os.environ["SERPER_API_KEY"] = serper_api_key
        os.environ["OPENROUTER_API_KEY"] = openrouter_api_key
        os.environ["LLM_MODEL"] = llm_model
        os.environ["LLM_API_BASE"] = llm_api_base
        st.success("Settings saved for this session!")

# Main form
with st.form("search_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.text_input("Location (city, address, etc.)", value="New York")
        search_query = st.text_input("Search Query (e.g., 'coffee shops', 'dentists')", value="Real Estate Agents")
    
    with col2:
        num_places = st.number_input("Target Number of Leads", min_value=20, max_value=5000, value=20, step=20)
        expand_search = st.toggle("Expand Search", value=False, help="Enable this to automatically search by neighborhoods if the target leads aren't met in a single city-wide search.")
    
    submit_button = st.form_submit_button("Start Lead Generation")

# Initialize session state if not already done
if "excel_path" not in st.session_state:
    st.session_state.excel_path = None

async def main_with_progress(location, search_query, target_leads, should_expand):
    """
    Main function with progress reporting for Streamlit
    """
    # Status placeholder for showing current operation
    status = st.empty()
    
    # Check if we need multi-location search
    all_places_data = []
    
    if should_expand and target_leads > 100:
        status.text("🏙️ Fetching neighborhoods for automated multi-location search...")
        sub_locations = await get_sub_locations(location)
        
        if not sub_locations:
            status.warning("⚠️ Could not find neighborhoods automatically. Falling back to city-wide search.")
            sub_locations = [location]
        else:
            status.info(f"📍 Found {len(sub_locations)} neighborhoods. Starting automated grid search...")
            # Each sub-location gives ~200 leads safely
            needed_subs = (target_leads // 100) + 1
            sub_locations = sub_locations[:needed_subs]
    else:
        sub_locations = [location]

    total_found_so_far = 0
    sub_locations_searched = 0
    for sub_loc in sub_locations:
        sub_locations_searched += 1
        status.text(f"🔍 Getting coordinates for {sub_loc}...")
        search_loc = sub_loc if len(sub_locations) == 1 else f"{sub_loc}, {location}"
        coords = get_coordinates(search_loc)
        if not coords:
            continue
            
        status.text(f"🔍 Searching for businesses in {sub_loc}...")
        # Calculate pages needed
        remaining_leads = target_leads - total_found_so_far
        pages_needed = min(13, (remaining_leads + 19) // 20)
        
        try:
            places_data = search_places(search_query, coords, pages_needed)
            if places_data:
                all_places_data.extend(places_data)
                current_batch_count = sum(len(p.get('places', [])) for p in places_data)
                total_found_so_far += current_batch_count
        except Exception as api_err:
            error_msg = str(api_err)
            if "credits" in error_msg.lower():
                st.error("❌ **Out of Credits:** Your Serper account has run out of credits. Please add more credits at [serper.dev](https://serper.dev) to continue.")
                return None, sub_locations_searched
            
            st.error(f"❌ {error_msg}")
            # Stop the loop if there's a serious API error (like auth)
            if "Unauthorized" in error_msg:
                return None, sub_locations_searched
            continue
        
        if total_found_so_far >= target_leads:
            break

    if not all_places_data:
        st.error("❌ No places found. Try a different search query or location.")
        return None, 0
        
    # Step 3: Save places data to Excel
    status.text("💾 Saving initial data to Excel...")
    excel_filename = f"data_{search_query}_{location}_{get_current_date()}.xlsx"
    file_path = save_places_to_excel(all_places_data, excel_filename, limit=target_leads)
    
    if not file_path:
        st.error("❌ No businesses were found in the search results. Try a different query or location.")
        return None, sub_locations_searched

    # Step 4: Process businesses to get detailed information
    status.text("🌐 Processing businesses to extract detailed information...")
    
    # Create a Streamlit progress bar
    progress_bar = st.progress(0)
    progress_text = st.empty()
    
    # Load data to get total count
    from src.data_export import load_excel_data
    df_preview, _ = load_excel_data(file_path)
    total_to_process = len(df_preview)
    
    if total_to_process < target_leads:
        if should_expand:
            st.warning(f"⚠️ I've completed the expanded search across **{sub_locations_searched} neighborhoods** in {location}, but only found **{total_to_process}** businesses. This usually means the query is very niche or the area has reached its limit of available data.")
        else:
            st.warning(f"⚠️ City-wide search returned **{total_to_process}** results. To reach your target of **{target_leads}**, enable **'Expand Search'**—this allows me to automatically search in surrounding neighborhoods.")
    
    # Define a custom callback to track progress
    async def progress_callback(total, current, business_name):
        # Update the progress bar
        progress_bar.progress((current + 1) / total)
        progress_text.text(f"Processing: {current + 1}/{total} - {business_name}")
    
    # Process the businesses with our progress callback
    await process_businesses(file_path, progress_callback=progress_callback)
    
    st.success(f"✅ Lead generation complete! Found {total_to_process} businesses.")
    
    return file_path, sub_locations_searched


# Main execution logic
if submit_button:
    if expand_search:
        st.info(f"🚀 **Expansion Active:** I will search through **{location}** and its **neighborhoods** to reach your goal of **{num_places}** leads. This 'Magnifying Glass' approach bypasses standard Google Maps limits.")
    else:
        st.info(f"⚠️ **Expansion Disabled:** Searching only the main city area. Results are limited to ~260. **Enable 'Expand Search'** to include neighborhoods and reach **{num_places}** leads.")
    
    # Check if API keys are set
    if not os.environ.get("SERPER_API_KEY") or not os.environ.get("OPENROUTER_API_KEY"):
        st.error("⚠️ Please set your API keys in the sidebar before starting.")
    else:
        with st.spinner("Starting lead generation..."):
            # Run the async function
            excel_path, searched_count = asyncio.run(main_with_progress(location, search_query, num_places, expand_search))
            if excel_path:
                st.session_state.excel_path = excel_path

# Download section - Always check if the file exists
if st.session_state.excel_path and os.path.exists(st.session_state.excel_path):
    st.subheader("Download Results")
    
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(st.session_state.excel_path)
        
        # Display a preview of the data
        if not df.empty:
            st.write(f"Found {len(df)} businesses:")
            st.dataframe(df)
            
            # Create a download button
            with open(st.session_state.excel_path, "rb") as excel_file:
                excel_bytes = excel_file.read()
                
            st.download_button(
                label="📥 Download Excel File",
                data=excel_bytes,
                file_name=os.path.basename(st.session_state.excel_path),
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_button"
            )
    except Exception as e:
        st.error(f"Error displaying results: {e}")
        st.write(f"You can find your file at: {st.session_state.excel_path}")

# FAQ Section
st.divider()
st.header("Frequently Asked Questions (FAQ)")

with st.expander("Why am I only getting ~260 leads when I asked for 1000?"):
    st.write("""
    This is an **API and Google Maps limitation**. For any single search query in a single location, Google typically stops returning new results after about 13-14 pages (approx. 260-300 leads). 
    
    To get more than this, you should:
    1. **Enable 'Expand Search'**: This will automatically break your search into smaller neighborhoods.
    2. **Be specific with location**: Searching 'Manhattan' instead of 'New York' will give more precise results.
    """)

with st.expander("How does 'Expand Search' help me get 2000+ leads?"):
    st.write("""
    Think of 'Expand Search' as a **Magnifying Glass** moving across the map:
    
    1.  **The Problem:** Google Maps limits any single search center-point to ~260 results. Even if there are 5000 realtors in NYC, a single search for "New York" won't show all of them.
    2.  **The Solution:** Instead of one big search, the tool splits the city into **neighborhoods** (e.g., Chelsea, SoHo, Harlem). 
    3.  **The Action:** It performs a fresh search for each neighborhood individually. 
        *   *Example:* 15 Neighborhoods × 150 leads each = **2,250 leads.**
    
    By "moving the magnifying glass" to different parts of the city, the tool captures data that a single city-wide search would miss.
    """)

with st.expander("What does 'Expand Search' do?"):
    st.write("""
    'Expand Search' is our **Automated Multi-Location Search** feature. 
    
    Instead of searching the whole city at once (which hits the 260-lead limit), the tool will:
    1. Look up neighborhoods within your target city (e.g., Chelsea, SoHo, Harlem for NYC).
    2. Perform a fresh search in each of those neighborhoods.
    3. Combine all results into one file.
    
    This is the best way to get thousands of leads for a single city.
    """)

with st.expander("Is the OpenStreetMap (Nominatim) API free?"):
    st.write("""
    **Yes, it is completely free.** 
    
    We use it to convert location names into coordinates and to find neighborhood names. It has a 'fair use' policy of 1 request per second, which our app respects. You will not be charged for these lookups.
    """)

with st.expander("How many leads can I get for $15?"):
    st.write("""
    With a **$15 investment** ($10 in Serper + $5 in OpenRouter), you can generate **over 10,000 fully enriched leads**.
    
    *   **Serper ($10):** Gives 50,000 credits. Since each search for 20 leads costs 3 credits, you can fetch ~16,500 basic business profiles.
    *   **OpenRouter ($5):** Using a budget model like `gpt-4o-mini`, $5 can process thousands of websites to find emails and social links.
    
    Compared to platforms like Apollo or Clay, this tool is roughly **50x cheaper** for the same data.
    """)

with st.expander("How do I save my API keys permanently?"):
    st.write("""
    To avoid entering keys every time, create a `.env` file in the project folder with the following content:
    ```env
    SERPER_API_KEY="your_key_here"
    OPENROUTER_API_KEY="your_key_here"
    ```
    The app will load these automatically on startup.
    """)

with st.expander("I am getting a '400 Bad Request' error. How do I fix it?"):
    st.write("""
    A **400 Bad Request** error usually means there is a temporary issue with the Serper API's batch processing or your account tier.
    
    **Troubleshooting Steps:**
    1. **Check Credits:** Ensure your Serper account has active credits.
    2. **Reduce Leads:** Try searching for a smaller number of leads (e.g., 20 or 40) to see if it's a payload size issue.
    3. **Verify API Key:** Ensure your Serper API key is entered correctly in the sidebar.
    4. **Contact Support:** If the error persists, there may be a service interruption on Serper's side.
    """)
        

import asyncio
from src.places_api import search_places, get_coordinates
from src.business_info import process_businesses
from src.data_export import save_places_to_excel
from src.utils import get_current_date
from dotenv import load_dotenv

load_dotenv(override=True)

async def main(location, search_query, num_pages):
    """
    Main function to orchestrate the lead generation process.
    
    Args:
        location (str): Location to search (city, address, etc.)
        search_query (str): What to search for (restaurants, dentists, etc.)
        num_pages (int): Number of pages to fetch (20 results per page)
    """
    print(f"\n🔍 Starting lead generation for '{search_query}' in '{location}'")
    
    # Step 1: Get coordinates from location
    coords = get_coordinates(location)
    if not coords:
        print("Could not get coordinates for the location. Exiting.")
        return
        
    # Step 2: Search for places using Serper Maps API
    places_data = search_places(search_query, coords, num_pages)
    if not places_data:
        print("No places found. Exiting.")
        return
        
    # Step 3: Save places data to Excel
    excel_filename = f"data_{search_query}_{location}_{get_current_date()}.xlsx"
    save_places_to_excel(places_data, excel_filename)
    
    # Step 4: Process businesses to get detailed information and update Excel file
    await process_businesses(excel_filename)

if __name__ == "__main__":
    print("--------------------------------------------------")
    print("🛠️ Google Maps Lead Generator (CLI Tool)")
    print("--------------------------------------------------")
    location = input("Enter Location (e.g., New York): ") or "Toronto"
    search_query = input("Enter Search Query (e.g., Realtors): ") or "Realtors"
    target_leads = int(input("Enter Target Number of Leads (e.g., 50): ") or "20")
    
    # Calculate pages (20 results per page)
    num_pages = max(1, target_leads // 20)
    
    # Run main function
    asyncio.run(main(location, search_query, num_pages))

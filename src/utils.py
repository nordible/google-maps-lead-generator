import os
from langchain_openai import ChatOpenAI
from datetime import datetime

# User agents for web scraping
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
]

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d_%H-%M")

async def ainvoke_llm(
    model=None,  # Now optional, will fallback to env
    system_prompt="",
    user_message="",
    response_format=None,
    temperature=0.1
):
    # Get configuration from environment
    api_base = os.getenv("LLM_API_BASE", "https://openrouter.ai/api/v1")
    api_key = os.getenv("OPENROUTER_API_KEY", "not-needed")
    default_model = os.getenv("LLM_MODEL", "meta-llama/llama-3-8b-instruct")
    
    # Use provided model or fallback to default
    target_model = model if model else default_model
    
    llm = ChatOpenAI(
        model=target_model, 
        temperature=temperature,
        api_key=api_key,
        base_url=api_base,
    )
    
    # If Response format is provided, use structured output
    # Note: Local LLMs must support Tool/Function calling or JSON mode
    if response_format:
        llm = llm.with_structured_output(response_format)
    
    # Prepare messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    
    # Invoke LLM asynchronously
    response = await llm.ainvoke(messages)
    
    return response if response_format else response.content

import os
import json
import requests
from typing import List, TypedDict
from .utils import USER_AGENTS, ainvoke_llm

class NeighborhoodsResponse(TypedDict):
    neighborhoods: List[str]

def get_coordinates(city):
    """
    Convert a city name to latitude and longitude coordinates.
    
    Args:
        city (str): Name of the city to geocode
        
    Returns:
        tuple: (latitude, longitude) if successful, (None, None) if not
    """
    try:
        response = requests.get(
            "https://nominatim.openstreetmap.org/search", 
            params={"q": city, "format": "json"}, 
            headers={"User-Agent": USER_AGENTS[2]}
        )
        data = response.json()
        if data:
            return {"lat": data[0]['lat'], "lon": data[0]['lon']}
        else:
            return None
    except Exception as e:
        print(f"Error getting coordinates: {e}")
        return None

async def get_sub_locations(city):
    """
    Get a list of neighborhoods/sub-locations for a city using OpenRouter LLM.
    """
    try:
        system_prompt = "You are a geographic expert. Provide a list of major neighborhoods or districts for the given city."
        user_message = f"List the top 15-20 neighborhoods or districts in {city}. Return only the names as a list."
        
        response = await ainvoke_llm(
            system_prompt=system_prompt,
            user_message=user_message,
            response_format=NeighborhoodsResponse
        )
        
        return response.get('neighborhoods', [])
    except Exception as e:
        print(f"Error getting sub-locations via LLM: {e}")
        return []


def search_places(query, coords, num_pages=1):
    """
    Search for places using Serper Maps API (Batch mode).
    
    Args:
        query (str): Search query (e.g., "restaurants", "dentists")
        coords (dict): Latitude and longitude dict
        num_pages (int): Number of pages to request (20 results per page)
        
    Returns:
        list: List of places data from the API
    """
    payload = []
    lat = str(coords['lat']).strip()
    lon = str(coords['lon']).strip()
    
    # Create batch payload for each page
    for page in range(1, num_pages + 1):
        payload.append({
            "q": query,
            "ll": f"@{lat},{lon},13z",
            "page": page
        })
    
    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(
            "https://google.serper.dev/maps", 
            headers=headers, 
            data=json.dumps(payload)
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            try:
                error_data = response.json()
                # Handle cases where response might be a list or a dict
                if isinstance(error_data, list):
                    error_message = error_data[0].get("message", "Batch request failed")
                else:
                    error_message = error_data.get("message", "Unknown error")
                raise Exception(f"Serper API Error: {error_message} (Status: {response.status_code})")
            except (ValueError, IndexError):
                raise Exception(f"Serper API Error: Status {response.status_code}")
            
    except Exception as e:
        raise e

import requests
import os
from typing import Optional

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST", "sky-scrapper3.p.rapidapi.com")

def search_flights(origin: str, destination: str, departure_date: str, return_date: Optional[str] = None, adults: int = 1) -> dict:
    """
    Search flights using Sky Scrapper API
    Note: Requires valid RapidAPI key
    """
    
    if not RAPIDAPI_KEY:
        return {
            "status": "error",
            "message": "RAPIDAPI_KEY not configured",
            "flights": []
        }
    
    try:
        url = "https://sky-scrapper.p.rapidapi.com/api/v1/searchFlights"
        
        querystring = {
            "originSkyId": origin.upper()[:3],
            "destinationSkyId": destination.upper()[:3],
            "departDate": departure_date,
            "adults": str(adults),
            "sortBy": "best",
            "currency": "EUR",
        }
        
        if return_date:
            querystring["returnDate"] = return_date
        
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": RAPIDAPI_HOST
        }
        
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        flights = []
        if "data" in data and "itineraries" in data["data"]:
            for flight in data["data"]["itineraries"][:5]:
                flights.append({
                    "price": flight.get("price", {}).get("raw", "N/A"),
                    "duration": flight.get("duration", "N/A"),
                    "stops": flight.get("legs", [{}])[0].get("stopCount", 0),
                })
        
        return {
            "status": "success",
            "flights": flights,
            "count": len(flights)
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": f"Flight search failed: {str(e)}",
            "flights": []
        }
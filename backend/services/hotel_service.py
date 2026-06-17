def search_hotels(city: str, check_in: str, check_out: str, guests: int = 1) -> dict:
    """
    Search for hotels in a destination
    Note: For now returns mock data, can be extended with real API
    """
    
    return {
        "status": "success",
        "hotels": [
            {
                "name": "Budget Hotel",
                "price_per_night": 50,
                "rating": 3.5,
                "location": f"Central {city}",
            },
            {
                "name": "Mid-Range Hotel",
                "price_per_night": 100,
                "rating": 4.0,
                "location": f"Downtown {city}",
            },
            {
                "name": "Premium Hotel",
                "price_per_night": 150,
                "rating": 4.5,
                "location": f"Best Location {city}",
            }
        ],
        "count": 3
    }


def get_hotel_recommendations(budget: float, preferences: list) -> dict:
    """
    Get hotel recommendations based on budget
    """
    
    return {
        "budget_estimate": budget,
        "recommendations": [
            {
                "type": "Budget Hotel",
                "price_range": f"€{budget * 0.3:.0f}-€{budget * 0.4:.0f} per night",
            },
            {
                "type": "Mid-Range Hotel",
                "price_range": f"€{budget * 0.4:.0f}-€{budget * 0.6:.0f} per night",
            }
        ]
    }
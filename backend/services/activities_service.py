from typing import List

DESTINATION_ACTIVITIES = {
    "copenhagen": ["Tivoli Gardens", "Design Museum", "Nyhavn", "Street food markets", "Christianshavn", "Amalienborg Palace"],
    "athens": ["Acropolis", "Parthenon", "Local tavernas", "Street art tours", "National Museum", "Plaka district"],
    "barcelona": ["Sagrada Familia", "Park Güell", "Gothic Quarter", "Tapas bars", "Beach walks", "La Boqueria Market"],
    "lisbon": ["Jerónimos Monastery", "Belém Tower", "Seafood restaurants", "Azulejo tiles", "Tram 28", "Miradouro viewpoints"],
    "london": ["Big Ben", "Tower of London", "British Museum", "Markets", "Theater district", "Royal palaces"],
    "paris": ["Eiffel Tower", "Louvre", "Café culture", "Seine walks", "Montmartre", "Champs-Élysées"],
    "berlin": ["Brandenburg Gate", "Street art", "Museum Island", "Beer gardens", "Nightlife", "Historical sites"],
    "amsterdam": ["Canals", "Anne Frank House", "Van Gogh Museum", "Cycling tours", "Dam Square", "Street food"],
    "rome": ["Colosseum", "Vatican", "Trevi Fountain", "Roman Forum", "Pasta & pizza", "Pantheon"],
    "madrid": ["Prado Museum", "Royal Palace", "Tapas bars", "Retiro Park", "Flamenco shows", "Street performers"],
}

def get_activities(destination: str, interests: List[str]) -> dict:
    """
    Get activities for a destination based on user interests
    """
    
    dest_lower = destination.lower()
    
    if dest_lower not in DESTINATION_ACTIVITIES:
        activities = ["Explore the city", "Visit museums", "Try local food", "Walk around neighborhoods"]
    else:
        activities = DESTINATION_ACTIVITIES[dest_lower]
    
    return {
        "status": "success",
        "destination": destination,
        "activities": activities[:8],
        "count": len(activities)
    }


def get_daily_budget_breakdown(total_budget: float, days: int) -> dict:
    """
    Break down total budget into daily allocations
    """
    
    daily_budget = total_budget / max(days, 1)
    
    return {
        "total_budget": total_budget,
        "days": days,
        "daily_budget": daily_budget,
        "breakdown": {
            "accommodation": f"€{daily_budget * 0.4:.2f}",
            "food": f"€{daily_budget * 0.3:.2f}",
            "activities": f"€{daily_budget * 0.2:.2f}",
            "transport": f"€{daily_budget * 0.1:.2f}"
        }
    }
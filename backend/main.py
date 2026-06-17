from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv

from agents.travel_agent import plan_trip, TravelPlanRequest

# Load environment variables
load_dotenv()

app = FastAPI(title="Travel Planner Agent API", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Travel Planner Agent API is running"
    }


@app.post("/plan-trip")
def plan_travel(request: TravelPlanRequest):
    """
    Main endpoint to plan a trip
    
    Receives travel details and returns an AI-generated travel plan
    """
    return plan_trip(request)


@app.get("/destinations")
def get_popular_destinations():
    """Get list of popular destinations for reference"""
    return {
        "destinations": [
            "Copenhagen",
            "Athens",
            "Barcelona",
            "Lisbon",
            "London",
            "Paris",
            "Berlin",
            "Amsterdam",
            "Rome",
            "Madrid"
        ]
    }


@app.get("/interests")
def get_travel_interests():
    """Get list of travel interests for filtering"""
    return {
        "interests": [
            "cultural",
            "food",
            "architecture",
            "design",
            "nature",
            "nightlife",
            "history",
            "art"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
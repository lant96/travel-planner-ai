import os
import requests
from pydantic import BaseModel

class TravelPlanRequest(BaseModel):
    origin: str
    destination: str
    departure_date: str
    return_date: str
    budget: float
    interests: list
    adults: int = 1


def plan_trip(request: TravelPlanRequest) -> dict:
    """
    Plan a trip using Groq API
    """
    
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    if not groq_api_key:
        return {
            "status": "error",
            "message": "GROQ_API_KEY not found in .env file. Please add your API key.",
            "request": request.dict()
        }
    
    try:
        # Call Groq API
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {groq_api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = f"""
Plan a complete trip with the following details:

Origin: {request.origin}
Destination: {request.destination}
Departure Date: {request.departure_date}
Return Date: {request.return_date}
Total Budget: €{request.budget}
Number of Adults: {request.adults}
Interests: {', '.join(request.interests)}

Please provide a detailed travel plan including:
1. Flight recommendations (best value, fastest, most convenient options)
2. Hotel recommendations (budget, mid-range, premium options with prices)
3. Top activities to experience based on interests
4. Daily budget breakdown
5. Total estimated cost
6. Why this combination works for the given constraints

Be specific with numbers, prices, and reasoning.
"""
        
        payload = {
            "model": "openai/gpt-oss-120b",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        # Check for errors
        if response.status_code != 200:
            error_msg = response.text
            if "Invalid API Key" in error_msg or "authentication" in error_msg.lower():
                return {
                    "status": "error",
                    "message": "Invalid Groq API Key. Please check your GROQ_API_KEY in .env file.",
                    "request": request.dict()
                }
            else:
                return {
                    "status": "error",
                    "message": f"Groq API Error: {response.status_code} - {error_msg[:200]}",
                    "request": request.dict()
                }
        
        data = response.json()
        
        # Extract recommendation from response
        if 'choices' in data and len(data['choices']) > 0:
            recommendation = data['choices'][0]['message']['content']
        else:
            recommendation = "No response from Groq API"
        
        return {
            "status": "success",
            "recommendation": recommendation,
            "request": request.dict()
        }
    
    except requests.exceptions.Timeout:
        return {
            "status": "error",
            "message": "Request to Groq API timed out. Please try again.",
            "request": request.dict()
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"Failed to connect to Groq API: {str(e)}",
            "request": request.dict()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Trip planning failed: {str(e)}",
            "request": request.dict()
        }
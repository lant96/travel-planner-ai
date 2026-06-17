# 🌍 AI Travel Planner

An intelligent travel planning application powered by **Groq LLM**, **FastAPI**, and **React**. The AI agent generates personalized travel recommendations based on your budget, dates, and interests.

## Features

-  **AI-Powered Recommendations** - Uses Groq's language models to generate smart travel plans
-  **Budget-Aware Planning** - Optimizes recommendations within your budget
-  **Interest-Based** - Tailors suggestions based on your travel interests
-  **Fast & Responsive** - Built with React and FastAPI for smooth performance
-  **Real API Integration** - Connects to Groq API for intelligent reasoning

## Architecture

```
Frontend (React + Vite)
    ↓
FastAPI Backend
    ↓
Groq LLM API
    ↓
Travel Recommendations
```

## Quick Start

### Prerequisites
- Python 3.12+
- Node.js 16+
- Groq API Key (free from https://console.groq.com)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/travel-planner-ai.git
cd travel-planner-ai
```

2. **Set up backend**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. **Create .env file**
```bash
cp .env.example .env
# Edit .env and add your Groq API key
```

4. **Set up frontend**
```bash
cd ../frontend
npm install
```

### Running the Application

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

## How It Works

1. **Fill in trip details** - Origin, destination, dates, budget, interests
2. **Click "Get AI Travel Plan"** - Backend sends request to Groq API
3. **Get personalized recommendation** - AI generates detailed travel plan with:
   - Flight options
   - Hotel recommendations
   - Activities
   - Budget breakdown
   - Cost estimates

## Getting Your Groq API Key

1. Go to https://console.groq.com
2. Sign up for free
3. Create API key
4. Add to `.env` file as `GROQ_API_KEY`

## Tech Stack

- **Frontend:** React 18, Vite, Axios
- **Backend:** FastAPI, Python 3.12
- **AI:** Groq LLM (openai/gpt-oss-120b)
- **Deployment:** Vercel (Frontend), Render (Backend)

## 📁 Project Structure

```
travel-planner-ai/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── agents/
│   │   └── travel_agent.py
│   └── services/
│       ├── flight_service.py
│       ├── hotel_service.py
│       └── activities_service.py
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Example Usage

**Input:**
- From: Athens
- To: Copenhagen
- Dates: July 1-10, 2026
- Budget: €1000
- Interests: Food, Culture

**Output:**
```
TRAVEL PLAN: Athens to Copenhagen
- Recommended flights
- Hotel suggestions with prices
- Top activities
- Daily budget breakdown
- Total estimated cost with reasoning
```

## Future Enhancements

- [ ] Multi-turn conversation for trip refinement
- [ ] Real-time flight price tracking
- [ ] User authentication & saved trips
- [ ] Advanced filtering options
- [ ] Mobile app version

## 📄 License

MIT License - feel free to use this project!
#  Intelligent Travel Planner

**An intelligent AI powered travel planning assistant that builds personalized itineraries in real-time.**

## Overview
The Intelligent Travel Planner isn’t just another chatbot answering travel questions. It works more like a real travel consultant behind the scenes. Powered by a smart workflow built with LangGraph, it knows which tools to use and when to use them.

When you ask for a trip plan, it doesn’t just generate suggestions, it actively researches destinations, checks live weather, estimates your budget, and converts costs into your preferred currency. The result is a practical, well-organized itinerary you can actually use, not just a list of ideas.

## Key Features

 -**A Truly Autonomous AI Core:** The system doesn’t just follow a script, it intelligently decides which tools to use and when, so every trip plan is thoughtfully put together.

-**Smarter Travel Search:** By tapping into  Google Places API, it finds highly rated attractions, great restaurants, and even lesser-known local gems.

-**Real-Time Weather Updates:** It checks live forecasts from OpenWeatherMap to make sure your itinerary actually fits the season and current conditions.

-**Automatic Currency Conversion:** Using up-to-date exchange rates from Fixer.io, it converts all estimated costs into your preferred currency—no manual calculations needed.

-**Built-In Budget Planning:** It gives you clear cost estimates for activities and dining, so you know what to expect before you go.

## Tech Stack

- **LLM Orchestration**: [LangGraph](https://langchain-ai.github.io/langgraph/) & [LangChain](https://www.langchain.com/)
- **LLM Providers**: Llama 3.3-70b (via **Groq**) 
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Tools & APIs**:  
  - **OpenWeatherMap**: Weather Data
  - **Fixer.io**: Currency Exchange Rates
  - **Google Places**: Places Info
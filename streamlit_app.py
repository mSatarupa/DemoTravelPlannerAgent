from dotenv import load_dotenv
import streamlit as st
import requests
import datetime


# --- Configuration ---
import os
load_dotenv()   
BASE_URL = "http://127.0.0.1:8080"
BASE_URL = os.getenv("BASE_URL", BASE_URL)  # Fallback to default if not set in .env

st.set_page_config(
    page_title="Travel Planner Agent",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Load Custom CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    local_css("assets/style.css")
except FileNotFoundError:
    st.warning("⚠️ CSS file not found. Running with default styles.")

# --- Sidebar ---
with st.sidebar:
    st.image("assets/—Pngtree—travel logo with airplane and_22631511.png")
    st.title("Trip Configuration")
    st.markdown("---")
    
    st.markdown("### ⚙️ Settings")    
    currency = st.selectbox("Currency", ["AUD", "USD", "EUR", "GBP", "JPY", "INR", "NZD"])
    
    st.markdown("---")
    st.markdown("### 🕒 History")
    if "history" not in st.session_state:
        st.session_state.history = []
    
    for i, item in enumerate(reversed(st.session_state.history[-5:])):
        st.caption(f"{i+1}. {item}")

    st.markdown("---")
  

# --- Main Interface ---
st.title("🌍 Intelligent Travel Planner")
st.markdown("#### *Your AI-powered travel planning assistant*")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🧳 Where to?")
    with st.form(key="query_form"):
        destination = st.text_input("Destination", placeholder="e.g. Paris, Tokyo, New York")
        days = st.number_input("Duration (Days)", min_value=1, max_value=30, value=5)
        budget = st.selectbox("Budget Level", ["Low", "Moderate", "Luxury"])
        interests = st.text_input("Interests / Preferences", placeholder="e.g. Historic Sites, Museums, Food, Hiking")
        
        submit_button = st.form_submit_button("🚀 Plan My Trip")

if submit_button:
    if not destination.strip():
        st.error("Please enter a destination.")
    else:
        # Construct the natural language query from inputs
        query = f"Plan a {days}-day {budget} trip to {destination}. Interests: {interests}. Currency: {currency}."
        
        # Save to history
        st.session_state.history.append(f"{destination} ({days} days)")
        
        with col2:
            with st.spinner(f"🔍 Researching {destination}, checking weather, and building your itinerary..."):
                try:
                    payload = {"question": query}
                    # Timeout set to 120s because agents can take time
                    
                    response = requests.post(f"{BASE_URL}/query", json=payload, timeout=120)
                    
                    if response.status_code == 200:
                        answer = response.json().get("answer", "No answer returned.")
                        
                        # Formatted Output
                        st.markdown(f"""
                        <div class="bot-msg">
                            <h1>🛫 Your {destination} Itinerary</h1>
                            <p><b>Generated:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
                            <hr>
                            {answer}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Download button for the itinerary
                        st.download_button(
                            label="📥 Download Itinerary as Text",
                            data=answer,
                            file_name=f"my_travel_plan_{destination}.txt",
                            mime="text/plain"
                        )
                        
                    else:
                        st.error(f"❌ Error {response.status_code}: {response.text}")
                
                except requests.exceptions.ConnectionError:
                    st.error("❌ Could not connect to the backend. Is it running on port 8000?")
                except Exception as e:
                    st.error(f"❌ An unexpected error occurred: {e}")

# Default state description
if not submit_button:
    with col2:
        st.info("👈 Fill out the trip details on the left to generate your personalized itinerary!")
        st.markdown(f"""
        ### What I can do:
        - 🌤️ **Check Weather**: I'll ensure your activities match the forecast.
        - 🏩 **Find Places**: I search for real, top-rated hotels and attractions.
        - 💰 **Budget**: I estimate costs in {currency}.
        """)
        
import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq




class ModelLoader(BaseModel):
    load_dotenv()   
    model_provider: str = "groq"
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        
        print("Loading LLM from Groq..............")
        groq_api_key = os.getenv("GROQ_API_KEY")
        model_name = os.getenv("GROQ_MODEL_NAME")
        llm=ChatGroq(model=model_name, api_key=groq_api_key)
        
        
        return llm
    
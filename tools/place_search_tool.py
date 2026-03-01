import os
from utils.place_info_search import GooglePlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        # Only initialize Google tool if key is present and not empty
        if self.google_api_key:
            self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        else:
            self.google_places_search = None
            
      
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            # Try Google first if available
            if self.google_places_search:
                try:
                    attraction_result = self.google_places_search.google_search_attractions(place)
                    if attraction_result:
                        return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
                except Exception as e:
                    # Log error if needed, proceed to fallback
                    pass
            
           
        
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            if self.google_places_search:
                try:
                    restaurants_result = self.google_places_search.google_search_restaurants(place)
                    if restaurants_result:
                        return f"Following are the restaurants of {place} as suggested by google: {restaurants_result}"
                except Exception:
                    pass

           
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            if self.google_places_search:
                try:
                    restaurants_result = self.google_places_search.google_search_activity(place)
                    if restaurants_result:
                        return f"Following are the activities in and around {place} as suggested by google: {restaurants_result}"
                except Exception:
                    pass

            
        
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            if self.google_places_search:
                try:
                    restaurants_result = self.google_places_search.google_search_transportation(place)
                    if restaurants_result:
                        return f"Following are the modes of transportation available in {place} as suggested by google: {restaurants_result}"
                except Exception:
                    pass

            
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]
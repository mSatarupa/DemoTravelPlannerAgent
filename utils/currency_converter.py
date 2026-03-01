import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        # Fixer.io uses http for free plan, usually. Or https if paid.
        # Check documentation or try http first if free.
        self.base_url = "http://data.fixer.io/api/latest" 
    
    def convert(self, amount: float, from_currency: str, to_currency: str):
        """Convert the amount from one currency to another using Fixer.io (Base EUR)"""
        params = {
            "access_key": self.api_key,
            # 'symbols': f"{from_currency},{to_currency}" #  fetch only needed
        }
        
        response = requests.get(self.base_url, params=params)
        
        if response.status_code != 200:
            raise Exception(f"API call failed: {response.text}")
            
        data = response.json()
        
        if not data.get("success"):
            error_info = data.get("error", {})
            raise Exception(f"Fixer API Error: {error_info.get('info', 'Unknown error')}")
            
        rates = data.get("rates", {})
        
        # Fixer base is usually EUR. 
        # API returns rates relative to base (e.g. 1 EUR = x USD, 1 EUR = y INR)
        # To convert USD -> INR: (Amount / USD_Rate) * INR_Rate
        
        # Ensure currencies exist
        if from_currency not in rates:
            raise ValueError(f"Currency {from_currency} not found in exchange rates.")
        if to_currency not in rates:
            raise ValueError(f"Currency {to_currency} not found in exchange rates.")
            
        from_rate = rates[from_currency]
        to_rate = rates[to_currency]
        
        # Conversion logic
        # 1. Convert 'from' to Base (EUR) -> amount / from_rate
        # 2. Convert Base to 'to' -> result * to_rate
        
        converted_amount = (amount / from_rate) * to_rate
        return round(converted_amount, 2)
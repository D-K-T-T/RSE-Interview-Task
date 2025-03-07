import requests

class FruityViceAPI:
    FRUITY_URL = "https://www.fruityvice.com/api/fruit"

    def get_fruit_info(self, fruit_name):
        """
        Purpose:
        -Use GET request to fetch fruit details from the FruityVice API.

        Parameters:
        -fruit_name (str): The name of the fruit to look up.(e.g. "apple", "banana")

        Returns:
        -A dictionary with fruit details, or an error message.
        """
        try:
            # Send a GET request to the FruityVice API
            response = requests.get(f"{self.FRUITY_URL}/{fruit_name.lower()}")
            # Raise an exception for HTTP errors
            response.raise_for_status()  
            # Parse the JSON response
            data = response.json()

            # Details to be extracted from the response
            fruit_details = {
                "name": data.get("name"),
                "id": data.get("id"),
                "family": data.get("family"),
                "sugar": f"{data.get('nutritions', {}).get('sugar')}g",
                "carbohydrates": f"{data.get('nutritions', {}).get('carbohydrates')}g",
            }
            return fruit_details
        
        # Handles HTTP errors identified by status codes
        except requests.exceptions.HTTPError as e:
            return {"error": f"HTTP Error: We couldn't find the fruit you requested. Please check the spelling or try another fruit. (Error code: {e.response.status_code})"}
        
        # Handles connection errors
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection Error: We encountered an issue connecting to the server. Please check your internet connection or try again later. (Error: {str(e)})"}
        
        # Handles missing or incorrectly formatted data
        except KeyError as e:
            return {"error": f"Data Error: The data we received was incomplete or incorrectly formatted. Please try again later. (Missing data: {e})"}

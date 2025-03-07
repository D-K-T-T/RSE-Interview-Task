import argparse
import json
from fruity_vice_task.fruity_vice_api import FruityViceAPI

def main():
    """
    Purpose:
    -Command-line tool for retrieving fruit details from the FruityVice API.

    """
    argument_parser = argparse.ArgumentParser(description="Fetch fruit details from FruityVice API.")
    argument_parser.add_argument("fruit_name", type=str, help="Name of the fruit (e.g. Banana or Apple)")
    argument_parser.add_argument("--format", choices=["human", "machine"], default="human", help="Output format")

    arguments = argument_parser.parse_args()

    # Initialize the API and fetch fruit details
    fruity_api = FruityViceAPI()
    fruit_details = fruity_api.get_fruit_info(arguments.fruit_name)

    # Handles error messages returned from the API response
    if "error" in fruit_details:
        print(f"Error: {fruit_details['error']}")
    else:
        #Fruit details displayed
        if arguments.format == "human":
            print(f"Name: {fruit_details['name']}")
            print(f"ID: {fruit_details['id']}")
            print(f"Family: {fruit_details['family']}")
            print(f"Sugar: {fruit_details['sugar']}")
            print(f"Carbohydrates: {fruit_details['carbohydrates']}")
        else:
            print(json.dumps(fruit_details, indent=2))

if __name__ == "__main__":
    main()

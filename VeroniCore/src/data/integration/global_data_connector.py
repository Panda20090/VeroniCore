# global_data_connector.py
# This script connects to global APIs and data sources, retrieves real-time data, and integrates it into the VeroniCore system.

import requests
import json

class GlobalDataConnector:
    def __init__(self, api_url, headers=None):
        self.api_url = api_url
        self.headers = headers if headers else {}
        print(f"Initialized GlobalDataConnector with API URL: {self.api_url}")

    def fetch_data(self, params=None):
        try:
            response = requests.get(self.api_url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            print(f"Data fetched successfully from {self.api_url}")
            return data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def integrate_data(self, data, storage_path="VeroniCore/data/global_data.json"):
        try:
            with open(storage_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data integrated successfully into {storage_path}")
        except Exception as err:
            print(f"An error occurred while integrating data: {err}")

if __name__ == "__main__":
    # Example usage of GlobalDataConnector
    api_url = "https://api.example.com/data"
    connector = GlobalDataConnector(api_url)

    # Fetch and integrate data
    data = connector.fetch_data(params={"key": "value"})
    if data:
        connector.integrate_data(data)
    
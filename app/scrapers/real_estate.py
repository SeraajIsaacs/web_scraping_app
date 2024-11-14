import requests

def run(site_name, api_info):
    url = f"https://{site_name}/api/properties"  # Example endpoint for properties
    headers = {"Authorization": f"Bearer {api_info}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Assume each item has "location", "price", and "type" (rent or sale)
        return [{"location": item["location"], "price": item["price"], "type": item["type"]} for item in data]
    else:
        return {"error": "Failed to retrieve data"}

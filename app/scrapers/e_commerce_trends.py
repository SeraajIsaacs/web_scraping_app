import requests

def run(site_name, api_info):
    url = f"https://{site_name}/api/trending-products"  # Example endpoint for trending products
    headers = {"Authorization": f"Bearer {api_info}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Assume each product has "name", "category", and "sales_rank"
        return [{"name": item["name"], "category": item["category"], "sales_rank": item["sales_rank"]} for item in data]
    else:
        return {"error": "Failed to retrieve data"}

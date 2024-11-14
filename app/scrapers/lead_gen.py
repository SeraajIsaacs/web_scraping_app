import requests

def run(site_name, api_info):
    url = f"https://{site_name}/api/business-directory"  # Example endpoint for business directory
    headers = {"Authorization": f"Bearer {api_info}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Assume each business has "name", "industry", "contact_email"
        return [{"name": item["name"], "industry": item["industry"], "contact_email": item["contact_email"]} for item in data]
    else:
        return {"error": "Failed to retrieve data"}

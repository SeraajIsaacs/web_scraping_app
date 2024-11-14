import requests

def run(site_name, api_info):
    url = f"https://{site_name}/api/endpoint"  # Example API URL
    headers = {"Authorization": f"Bearer {api_info}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Extract price info from data
        return data
    else:
        return {"error": "Failed to retrieve data"}

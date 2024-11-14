import requests

def run(site_name, api_info):
    url = f"https://{site_name}/api/social-sentiment"  # Example endpoint for sentiment data
    headers = {"Authorization": f"Bearer {api_info}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Assume data has "text" and "sentiment" fields
        return [{"text": item["text"], "sentiment": item["sentiment"]} for item in data]
    else:
        return {"error": "Failed to retrieve data"}

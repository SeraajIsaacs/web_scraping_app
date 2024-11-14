import requests

def run(site_name, api_info):
    url = f"https://{site_name}/api/seo-insights"  # Example endpoint for SEO insights
    headers = {"Authorization": f"Bearer {api_info}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Assume each item has "keyword", "volume", "competition"
        return [{"keyword": item["keyword"], "volume": item["volume"], "competition": item["competition"]} for item in data]
    else:
        return {"error": "Failed to retrieve data"}

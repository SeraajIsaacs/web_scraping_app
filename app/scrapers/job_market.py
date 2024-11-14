import requests

def run(site_name, api_info):
    url = f"https://{site_name}/api/job-listings"  # Example endpoint for job listings
    headers = {"Authorization": f"Bearer {api_info}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Assume each job listing has "title", "company", "location", "skills"
        return [{"title": item["title"], "company": item["company"], "location": item["location"], "skills": item["skills"]} for item in data]
    else:
        return {"error": "Failed to retrieve data"}

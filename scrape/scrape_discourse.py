import requests
import json
from datetime import datetime

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY = "/c/tools-in-data-science"


def fetch_posts(start_date, end_date):
    results = []
    page = 0
    while True:
        page += 1
        r = requests.get(f"{BASE_URL}{CATEGORY}.json?page={page}")
        if not r.ok: break
        data = r.json()
        for topic in data.get("topic_list", {}).get("topics", []):
            created = datetime.strptime(topic['created_at'][:10], "%Y-%m-%d")
            if start_date <= created <= end_date:
                results.append({
                    "id": topic['id'],
                    "title": topic['title'],
                    "link": f"{BASE_URL}/t/{topic['slug']}/{topic['id']}",
                    "text": topic['title'] + ". " + topic.get("excerpt", "")
                })
        if page > 5: break  # prevent overload
    with open("data/discourse_posts.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    fetch_posts(datetime(2025, 1, 1), datetime(2025, 4, 14))

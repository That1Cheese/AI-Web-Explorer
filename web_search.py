#!/usr/bin/env python3
"""
Simple Google Custom Search script
"""

import requests
import sys

# Configuration - Add your credentials here
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
GOOGLE_SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID_HERE"

def search(query, num_results=10):
    """Search Google and return results"""
    url = "https://www.googleapis.com/customsearch/v1"
    results = []

    params = {
        'key': GOOGLE_API_KEY,
        'cx': GOOGLE_SEARCH_ENGINE_ID,
        'q': query,
        'num': num_results
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if 'items' in data:
            for idx, item in enumerate(data['items'], 1):
                results.append({
                    'position': idx,
                    'title': item.get('title', ''),
                    'url': item.get('link', ''),
                    'snippet': item.get('snippet', '')
                })

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

    return results

def print_results(results):
    """Print search results"""
    if not results:
        print("No results found")
        return

    print(f"\nFound {len(results)} results:\n")
    for r in results:
        print(f"{r['position']}. {r['title']}")
        print(f"   URL: {r['url']}")
        print(f"   {r['snippet']}")
        print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python web_search.py 'search query'")
        sys.exit(1)

    query = sys.argv[1]
    results = search(query)
    print_results(results)

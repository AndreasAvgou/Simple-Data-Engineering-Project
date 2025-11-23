import requests
import logging

def fetch_data(url: str):
    try:
        logging.info(f"Fetching from {url}")
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logging.error(f"Fetch error: {e}")
        return []

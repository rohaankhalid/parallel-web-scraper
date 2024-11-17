import requests
from bs4 import BeautifulSoup
import time

def fetch_page_data(url, retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.title.string if soup.title else 'No Title Found'
                return {'url': url, 'title': title}
            else:
                return {'url': url, 'title': f"Failed: {response.status_code}"}
        except Exception as e:
            print(f"Retrying {url} due to error: {e}")
            time.sleep(1)  # Wait 1 second before retrying
    return {'url': url, 'title': "Error after retries"}

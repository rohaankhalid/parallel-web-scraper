import threading
from .basic_scraper import fetch_page_data

data_lock = threading.Lock()
scraped_data = []

def scrape_url(url):
    result = fetch_page_data(url)
    with data_lock:
        scraped_data.append(result)

def scrape_with_threads(urls, num_threads):
    threads = []
    for url in urls:
        thread = threading.Thread(target=scrape_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return scraped_data

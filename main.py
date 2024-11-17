import time
import asyncio
import os
from scraper.basic_scraper import fetch_page_data
from scraper.threading_scraper import scrape_with_threads
from scraper.async_scraper import scrape_with_asyncio

# Function to save results directly in the specified folder, overwriting the existing file
def save_results(scraper_name, url_file, data):
    # Extract URL set (e.g., "urls_10") from url_file
    url_set = url_file.split('.')[0]
    
    # Define the folder path (basic, threading, or async)
    folder_path = f"results/{scraper_name}"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Define the filename and save the results
    filename = f"{folder_path}/{scraper_name}_{url_set}_results.txt"
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry['url']}: {entry['title']}\n")
    print(f"Results saved to {filename}")

# Function to load URLs from a file
def load_urls(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Function to perform basic scraping
def scrape_with_basic(urls):
    scraped_data = []
    for url in urls:
        result = fetch_page_data(url)
        scraped_data.append(result)
    return scraped_data

if __name__ == "__main__":
    # List of urls.txt files for testing
    url_files = ["urls_10.txt", "urls_30.txt", "urls_50.txt", "urls_100.txt"]

    # Loop through each file and run the scrapers
    for url_file in url_files:
        print(f"\nRunning scrapers for {url_file}...")

        # Load URLs from the current file
        urls = load_urls(f"data/{url_file}")

        # Measure time for the basic scraper
        start_time = time.time()
        scraped_data_basic = scrape_with_basic(urls)
        basic_time = time.time() - start_time

        # Measure time for threading
        start_time = time.time()
        scraped_data_threading = scrape_with_threads(urls, num_threads=5)
        threading_time = time.time() - start_time

        # Measure time for asyncio
        start_time = time.time()
        scraped_data_async = asyncio.run(scrape_with_asyncio(urls, max_connections=5))
        async_time = time.time() - start_time

        # Save results for each scraper in their respective folders
        save_results("basic", url_file, scraped_data_basic)
        save_results("threading", url_file, scraped_data_threading)
        save_results("async", url_file, scraped_data_async)

        # Print times for the current set of URLs
        print(f"\nResults for {url_file}:")
        print(f"Basic Time: {basic_time:.2f} seconds")
        print(f"Threading Time: {threading_time:.2f} seconds")
        print(f"Async Time: {async_time:.2f} seconds")
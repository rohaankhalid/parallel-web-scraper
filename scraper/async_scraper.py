import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch_page_data_async(session, url, semaphore, retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    async with semaphore:
        for attempt in range(retries):
            try:
                async with session.get(url, headers=headers, timeout=10) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'html.parser')
                        title = soup.title.string if soup.title else 'No Title Found'
                        return {'url': url, 'title': title}
                    else:
                        return {'url': url, 'title': f"Failed: {response.status}"}
            except (aiohttp.ClientError, asyncio.TimeoutError, ConnectionResetError) as e:
                print(f"Attempt {attempt + 1} failed for {url}: {e}")
                await asyncio.sleep(1)
        return {'url': url, 'title': "Error after retries"}

async def scrape_with_asyncio(urls, max_connections):
    semaphore = asyncio.Semaphore(max_connections)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page_data_async(session, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks)

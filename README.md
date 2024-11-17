# Parallel Web Scraper

## Project Overview
This project demonstrates the use of parallel programming techniques to optimize web scraping in Python. The web scraper fetches titles from web pages using three different methods:
1. **Basic Scraper**: A serial (non-parallel) approach.
2. **Threading Scraper**: Uses Python’s `threading` module to perform parallel requests.
3. **Async Scraper**: Utilizes `asyncio` and `aiohttp` for asynchronous web scraping.

The goal is to compare the performance of these methods and understand how threading and asynchronous programming can improve efficiency in I/O-bound tasks.

---

## How to Use

### Prerequisites
- **Python**: Make sure Python 3.8 or later is installed on your system. You can check this by running:
  ```bash
  python --version
  ```
  If Python is not installed, download it from [python.org](https://www.python.org) and follow the installation instructions.
  
- **Pip**: Ensure that `pip` (Python package installer) is installed and updated. You can check this by running:
  ```bash
  pip --version
  ```
  If `pip` is not installed, refer to the [pip installation guide](https://pip.pypa.io/en/stable/installation/)

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohaankhalid/parallel-web-scraper
   cd parallel_web_scraper

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     source venv/Scripts/activate
   - On macOS/Linux:
     ```bash
     source venv/bin/activate

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

### Running the Program
1. **Run the main script**:
   ```bash
   python main.py
   
3. The script will:
   - Load URLs from `urls_10.txt`, `urls_20.txt`, `urls_30.txt`, and `urls_100.txt`.
   - Perform scraping using the Basic, Threading, and Async methods.
   - Save the results in the `results/` directory and print execution times to the terminal.

4. **Modifying `num_threads` and `max_connections`**:
   - To test with different numbers of threads and async connections, manually update these values in `main.py` and rerun the script.

---

## Scrapers Explanation

### 1. Basic Scraper
- **File**: `basic_scraper.py`
- **Description**: Performs web scraping serially, fetching each URL one by one using the `requests` library.
- **Use Case**: Useful as a baseline for performance comparison.

### 2. Threading Scraper
- **File**: `threading_scraper.py`
- **Description**: Uses Python’s `threading` module to perform concurrent web requests. Suitable for I/O-bound tasks like web scraping.
- **Benefit**: Reduces total execution time by parallelizing requests.

### 3. Async Scraper
- **File**: `async_scraper.py`
- **Description**: Uses `asyncio` and `aiohttp` to handle asynchronous requests efficiently.
- **Benefit**: Further optimizes performance by allowing non-blocking I/O operations.

---

## Results and Performance Analysis

### Summary of Results
Below are the time ranges (in seconds) recorded for each configuration:

| **URL Set**     | **Basic Time** | **Threading Time (2, 5, 10, 15 threads)** | **Async Time (2, 5, 10, 15 connections)** |
|------------------|----------------|------------------------------------------|------------------------------------------|
| **urls_10.txt**  | 2.98 - 3.64    | 1.31 - 1.50                              | 1.53 - 2.04                              |
| **urls_30.txt**  | 8.91 - 9.91    | 2.95 - 3.29                              | 4.06 - 5.56                              |
| **urls_50.txt**  | 13.35 - 14.21  | 6.10 - 6.58                              | 5.44 - 8.63                              |
| **urls_100.txt** | 26.70 - 30.83  | 11.15 - 12.45                            | 9.78 - 13.10                             |

### Observations
- **Threading Performance**: Generally, threading improved performance compared to the basic scraper, but the benefit diminished as the number of threads increased, likely due to system limitations and overhead.
- **Async Performance**: The async scraper showed significant improvements over the basic scraper but faced diminishing returns and potential issues with connection limits, as evidenced by the `ConnectionResetError`.
- **Optimal Configuration**: The best performance was often seen around `num_threads=5` and `max_connections=5`, beyond which the gains were marginal or inconsistent.

### Exception Note
- **ConnectionResetError**: During the test with `15` connections, an exception occurred, suggesting that some servers might be rejecting too many simultaneous requests.

---

## Dependencies
- `requests`: For HTTP requests in the basic scraper.
- `aiohttp`: For asynchronous requests in the async scraper.
- `asyncio`: To handle asynchronous programming.
- `time`: To measure execution times.
- `os`: For file operations.

---

## Web Scraping Ethics

### Respecting `robots.txt` Files
This project adheres to ethical web scraping practices by respecting the rules specified in each website's `robots.txt` file. The `robots.txt` file is a publicly accessible document located at `https://www.example.com/robots.txt` that outlines which parts of the website can and cannot be accessed by automated scripts.

- **Implementation**: Before adding any new URLs to the `urls.txt` files, I checked the `robots.txt` file of each website to ensure that the pages I intended to scrape are not disallowed. This helps to ensure compliance with the website's policies and avoids any potential legal or ethical issues.
- **Best Practice**: The scraper also avoids sending too many requests in rapid succession to minimize the impact on the website's performance and prevent overloading the server.

By following these guidelines, the project demonstrates responsible web scraping and encourages developers to always respect website rules.

---

## Future Work
- **More Robust Error Handling**: Implement retries and better exception handling to deal with connection issues.
- **Dynamic Load Balancing**: Explore adaptive techniques to optimize the number of threads or connections based on system resources.
- **Extending Functionality**: Scrape additional data fields or implement support for JavaScript-heavy websites using tools like `selenium`.

---


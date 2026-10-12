import time
from collections import deque
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

START_URL = "" # CHANGE THIS
USER_AGENT = "CrawlTheNet/1.0"

def crawl(max_pages=50, delay=1.0):
    domain = urlparse(START_URL).netloc

    rp = RobotFileParser()
    rp.set_url(urljoin(START_URL, "/robots.txt"))
    rp.read()

    session = requests.Session()
    session.headers.update({ "User-Agent": USER_AGENT })

    queue = deque([START_URL])
    visited = set()
    results = {}

    while queue and len(visited) < max_pages:
        url = queue.popleft()

        if url in visited or not rp.can_fetch(USER_AGENT, url):
            continue

        visited.add(url)

        try:
            resp = session.get(url, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"Error on {url}: {e}")
            continue

        if "text/html" not in resp.headers.get("Content-Type", ""):
            continue

        soup = BeautifulSoup(resp.text, "html.parser")
        results[url] = soup.h1.string.strip() if soup.h1 and soup.h1.string else ""
        print(f"[{len(visited)}] {url}")

        for a in soup.find_all("a", href=True):
            link, _ = urldefrag(urljoin(url, str(a["href"])))

            if urlparse(link).netloc == domain and link not in visited:
                queue.append(link)

        time.sleep(delay)

    return results

if __name__ == "__main__":
    pages = crawl()

    for url, h1 in pages.items():
        print(f"{url} -> {h1}")

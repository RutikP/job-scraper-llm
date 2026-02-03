
# scraper/parser.py

from bs4 import BeautifulSoup


def parse_jobs(html):
    soup = BeautifulSoup(html, "html.parser")

    jobs = []
    seen = set()

    for link in soup.find_all("a", href=True):
        href = link["href"]
        title = link.get_text(strip=True)

        if "/positions/" not in href:
            continue
        if "#" in href:
            continue
        if not title or len(title) < 5:
            continue

        if href.startswith("/"):
            href = "https://careers.airbnb.com" + href

        if href in seen:
            continue

        seen.add(href)
        jobs.append({"title": title, "url": href})

    return jobs

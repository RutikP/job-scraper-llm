
# scraper/jd_parser.py

from bs4 import BeautifulSoup


def parse_job_description(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "svg"]):
        tag.decompose()

    body = soup.find("body")
    if not body:
        return ""

    text = body.get_text(separator="\n", strip=True)

    lines = [line.strip() for line in text.split("\n") if len(line.strip()) > 30]

    return "\n".join(lines)

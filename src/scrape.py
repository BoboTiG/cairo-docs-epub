from pathlib import Path
from typing import List

from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests

from .constants import BASE_URL, IGNORED_PAGES, OUTPUT_TMP, LINK_REGEXP, USER_AGENT

URLS = set()


def clean(html: NavigableString) -> str:
    body = html.find_parent().find("div", {"class": "body"}).find_next("div")

    # Remove the TOC
    for toc in body.find_all("div", {"class": "toctree-wrapper"}):
        toc.decompose()

    # Remove header links
    for hlink in body.find_all("a", {"class": "headerlink"}):
        hlink.decompose()

    # Improve external links display
    for link in body.find_all("a", {"class": "reference external"}):
        href = link.get("href")
        if href.startswith(".."):
            # file.sol example
            link.replaceWith(href.split("/")[-1])
        else:
            link.string = href

    # Neutralize internal links
    for link in body.find_all("a", {"class": "reference internal"}):
        link.replaceWith(link.string)

    # Remove the only one picture
    for img in body.find_all("img"):
        img.decompose()

    return str(body).encode("latin-1").decode("utf-8")


def fetch_page(session: requests.Session, url: str, file: Path) -> str:
    if url in URLS:
        return ""

    URLS.add(url)
    print(f"{url} …", end=" ", flush=True)

    with session.get(url) as req:
        html = req.text

    soup = BeautifulSoup(html, features="html.parser")
    body = soup.find("div", {"class": "body"})
    if not body:
        print("..", flush=True)
        return ""

    full_body = str(body).encode("latin-1").decode("utf-8")
    content = clean(body)
    file.write_text(content)
    print("OK", flush=True)
    return full_body


def fetch_pages(session: requests.Session, url: str, idx: int) -> None:
    file = OUTPUT_TMP / url.removeprefix(BASE_URL)
    file = file.with_stem(f"{str(idx).zfill(2)} - {file.stem}")
    file.parent.mkdir(parents=True, exist_ok=True)

    content = fetch_page(session, url, file)
    for link_idx, link_url in enumerate(links(content), 1):
        fetch_pages(session, link_url, link_idx)


def links(content: str) -> List[str]:
    return [
        f"{BASE_URL}{link}"
        for link in LINK_REGEXP.findall(content)
        if not str(Path(link)).startswith(IGNORED_PAGES)
    ]


def scrape() -> None:
    session = requests.session()
    session.headers["user-agent"] = USER_AGENT
    fetch_pages(session, f"{BASE_URL}index.html", 0)

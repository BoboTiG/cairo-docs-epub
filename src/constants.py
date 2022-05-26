import re
from pathlib import Path

# Website
BASE_URL = "https://www.cairo-lang.org/docs/"
LINK_REGEXP = re.compile(r' href="(.+.html)"')
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
IGNORED_PAGES = (".", "genindex", "search")

# Paths
ROOT = Path(__file__).parent.parent
OUTPUT_TMP = ROOT / "tmp"
OUTPUT_FINAL = ROOT / "output"

# ePub
EPUB_AUTHOR = "StarkWare Industries Ltd."
EPUB_FILE = OUTPUT_FINAL / "starknet-and-cairo-documentation.epub"
EPUB_TITLE = "StarkNet and Cairo Documentation"
TITLE_REGEXP = re.compile(r"<h1>(.+)</h1>")

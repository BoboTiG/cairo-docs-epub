from pathlib import Path
from subprocess import check_call

import mkepub
from mkepub.mkepub import Book, Page


from .constants import EPUB_AUTHOR, EPUB_FILE, EPUB_TITLE, OUTPUT_TMP, TITLE_REGEXP


def add_page(book: Book, path: Path, parent: Page | None = None) -> Page:
    html = path.read_text()
    title = extract_title(html)
    return book.add_page(title=title, content=html, parent=parent)


def extract_title(html: str) -> str:
    return TITLE_REGEXP.findall(html)[0]


def make_it() -> None:
    book = mkepub.Book(title=EPUB_TITLE, author=EPUB_AUTHOR)

    with Path("cover.jpg").open(mode="rb") as fh:
        book.set_cover(fh.read())

    files = sorted(OUTPUT_TMP.glob("**/*.html"), key=lambda p: Path(p).stem)

    # Create the top-level chapters
    top_files = list(filter(lambda file: file.stem.endswith("index"), files))
    top_levels = {file.parent: add_page(book, file) for file in top_files}

    # Append pages to chapters
    print()
    for page in files:
        if page in top_files:
            continue
        assert not page.stem.endswith("index")
        parent = top_levels[page.parent]
        add_page(book, page, parent=parent)

    EPUB_FILE.parent.mkdir(exist_ok=True)
    book.save(EPUB_FILE)

    # Check
    check_call(["epubcheck", str(EPUB_FILE)])

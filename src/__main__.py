import sys


def main() -> int:
    from .scrape import scrape
    from .epub import make_it

    scrape()
    make_it()
    return 0


if __name__ == "__main__":
    sys.exit(main())

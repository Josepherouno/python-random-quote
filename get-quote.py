import random
from pathlib import Path


def main() -> None:
    """Print a random quote from ``quotes.txt``."""
    quotes_path = Path(__file__).with_name("quotes.txt")
    with quotes_path.open(encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]
    print(random.choice(quotes))


if __name__ == "__main__":
    main()

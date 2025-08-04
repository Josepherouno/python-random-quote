import random


def main():
    with open("quotes.txt", "r", encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]
    print(random.choice(quotes))


if __name__ == "__main__":
    main()

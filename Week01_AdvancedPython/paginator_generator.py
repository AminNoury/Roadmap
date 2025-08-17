# Placeholder for paginator_generator.py
items = list(range(1, 51))
page_size = 10


def paginator(data, page_size):
    for i in range(0, len(data), page_size):
        # print(data[i: i+page_size])
        yield data[i: i+page_size]


def main():
    for page in paginator(items, page_size):
        print(page)


if __name__ == "__main__":
    main()

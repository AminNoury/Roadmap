def generator(n):
    i = 0
    while True:
        yield i
        i += n


gen = generator(100)


def main():
    for i in range(10):
        print(next(gen))


if __name__ == "__main__":
    main()

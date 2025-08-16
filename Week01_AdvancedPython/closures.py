def outer_function():
    message = "Hello, World!"

    def inner_function():
        print(message)

    return inner_function


outer = outer_function()


def initialize():
    print("Initializing resources...")


def main():
    initialize()
    print("Program is running...")
    # Put main logic here
    outer()


if __name__ == "__main__":
    main()

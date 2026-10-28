def is_odd(number):
    return number % 2 != 0


def main():
    try:
        value = int(input("Enter a number: "))
        if is_odd(value):
            print(f"{value} is an odd number.")
        else:
            print(f"{value} is an even number.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()

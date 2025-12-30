import random as r

def roll():
    return r.randint(1, 6)

def main():
    while True:
        choice = input(
            "Enter your choice\n"
            "1. Roll Dice\n"
            "2. Exit\n"
        ).strip()

        if choice == "1":
            result = roll()
            print(f"You rolled: {result}")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option. Select 1 or 2.")

if __name__ == "__main__":
    main()

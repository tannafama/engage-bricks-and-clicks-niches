def main():
    main()
    data = generate_random_data()
import random

def generate_random_data():
    data = [random.randint(1, 100) for _ in range(10)]


    for item in data:

        print(f"Random Number: {item}")
    return data
if __name__ == "__main__":
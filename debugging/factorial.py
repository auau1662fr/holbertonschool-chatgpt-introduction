#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # décrémente n pour éviter la boucle infinie
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Error: number must be non-negative")
            sys.exit(1)
        print(factorial(number))
    except ValueError:
        print("Error: argument must be an integer")
        sys.exit(1)


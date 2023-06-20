# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 6 - Permutations and Combinations
# Maira Bermeo

# Acknowledgements:
# I worked with the class


import math


def print_tables(name, func, n):
    print(name)
    for i in range(n + 1):
        print((name[0] + "(" + str(i) + ",r" + ")").rjust(8), end=" ")
    print()
    for i in range(n + 1):
        for r in range(n + 1):
            print(str(func(i, r)).rjust(8), end=" ")
        print()


def main():
    n = 10
    print_tables("Permutations", math.perm, n)
    print_tables("Combinations", math.comb, n)


if __name__ == "__main__":
    main()
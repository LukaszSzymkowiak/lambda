from functions import *


def main():
    numbers_list = random_numbers_list_func()
    print(f"Number list: {numbers_list}")
    even_numbers = even_numbers_func(numbers_list)
    print(f"Even numbers with lambda, filter: {even_numbers}")
    odd_numbers = odd_numbers_func(numbers_list)
    print(f"Odd numbers with lambda, filter: {odd_numbers}")
    power_of_numbers = power_of_numbers_func(numbers_list)
    print(f"Power of 2 with lambda, map: {power_of_numbers}")
    sqrt_numbers = sqrt_numbers_func(numbers_list)
    print(f"Sqrt with lambda, map: {sqrt_numbers}")


if __name__ == '__main__':
    main()

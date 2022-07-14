import random
import math
import numpy


# random list
def random_numbers_list_func():
    number_list = []
    while len(number_list) < 15:
        random_number = random.randint(1, 200)
        number_list.append(random_number)
    return number_list


# filter, lambda
def even_numbers_func(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def odd_numbers_func(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))


# map, lambda
def power_of_numbers_func(numbers):
    return list(map(lambda x: math.pow(x, 2), numbers))


def sqrt_numbers_func(numbers):
    sqrt = list(map(lambda x: math.sqrt(x), numbers))
    formatted_sqrt = list(numpy.around(numpy.array(sqrt), 2))
    return formatted_sqrt

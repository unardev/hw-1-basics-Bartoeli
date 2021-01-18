#!/usr/bin/env python3
from math import sqrt


def sample_get_full_name(first_name, last_name):
    """
    Sample function to return full name
    :param first_name: First name
    :param last_name: Last name
    :return: Full name
    :rtype: str
    """

    return '{} {}'.format(first_name, last_name)


def sample_get_fermat_numbers_in_range(n_from, n_to):
    """
    Sample function to return fermat numbers (https://en.wikipedia.org/wiki/Fermat_number) for numbers in given range
    :param n_from: F_nfrom
    :param n_to: F_nto
    :return:
        list of fermat numbers if n_from >= 0 and n_to >=0
        [] if n_from < 0 or n_to < 0
    """

    # Fermat numbers are defined for non-negative integers only
    if n_from < 0 or n_to < 0:
        return []
    else:
        result = []
        for a in range(n_from, n_to + 1):
            result.append(2 ** (2 ** a) + 1)
        return result


def sum_list(source_list):
    """
    Function to sum given list's elements that are multiplicated by their index.

    :param list: List to be summed
    :return: sum, e. g. for [1,2,3] return 0*1 + 1*2 + 2*3 = 8
    :rtype: int
    """
    pass


def check_parity(number):
    """
    Function to check if a given number is odd or even

    :param number: Check parity of this number
    :return: True if even, False if odd
    :rtype: bool
    """
    pass


def get_first_and_last(source_list):
    """
    Function to return list of the first and the last element of given array

    :param source_list: Return elements for this list
    :return:
        List of two numbers if given array contains at least two elements
        Empty list if source_list contains one or no elements
    :rtype: list
    """
    pass


def solve_quadratic_equation(a, b, c):
    """
    Function to solve a quadratic equation in form ax^2 + bx + c == 0 for given parameters
    hint: try sqrt() function for square root
    :return:
        x_1, x_2 rounded to 3 decimal places if a != 0
        () if a == 0
    :rtype: tuple
    """
    pass


if __name__ == '__main__':
    """Use your own parameters, if you want to test your code"""

    print(sample_get_full_name("Anakin", "Skywalker"))
    print(sample_get_fermat_numbers_in_range(0, 10))
    print(sum_list())
    print(check_parity())
    print(get_first_and_last())
    print(solve_quadratic_equation())

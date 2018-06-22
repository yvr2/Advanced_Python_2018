#!/usr/bin/env python3


def decorator_function(input_function):
    '''This is the decorator function.'''
    def wrapper_function(*args, **kwargs):
        print('Output of the function {} is as follows:'.format(input_function.__name__))
        return input_function(*args, **kwargs)
    return wrapper_function


#Two simple functions passed in below, could have any number of input parameters
#and will still pass to decorator function


@decorator_function
def product_of_variables(a, b, c):
    '''Calculates product of three variables.'''
    product = a * b * c
    print('Product of values {}, {}, and {} is {}'.format(a, b, c, product))


@decorator_function
def sum_of_variables(x, y):
    '''Calculates sum of two variables.'''
    sum = x + y
    print('Sum of values {} and {} is {}'.format(x, y, sum))


product_of_variables(33, 26, 88)

sum_of_variables(5, 8)

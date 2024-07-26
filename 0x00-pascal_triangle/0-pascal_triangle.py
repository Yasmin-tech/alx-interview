#!/usr/bin/python3
'''
    Implement a function that returns a list of lists of integers
    representing the Pascal’s triangle.
'''


def pascal_triangle(n):
    '''
         Returns a list of lists of integers representing
         the Pascal’s triangle of n
    '''
    triangle = []
    if n <= 0:
        return triangle
    return pascal_triangle_recursive(n)


def pascal_triangle_recursive(n):
    '''
        returns a list of lists of integers representing
        the Pascal’s triangle recursivly
    '''

    if n == 1:
        triangle = []
        triangle.append([1])
        # print("n = ", n) For Debugging

        return triangle
    else:
        triangle = pascal_triangle_recursive(n - 1)

    # print("n = ", n) For Debugging
    # print("the triangle is ", triangle) For Debugging

    previous_row = triangle[n - 2]
    new_row = [1]
    length = len(previous_row)

    for j in range(length):
        first_number = previous_row[j]
        try:
            second_number = previous_row[j + 1]
        except IndexError:
            second_number = 0
        new_row.append(first_number + second_number)
    # print(new_row) For Debugging
    triangle.append(new_row)
    return triangle

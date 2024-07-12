#!/usr/bin/python3
''' Impelemnt the function minOperations that calculates
    the fewest number of operations needed to result in exactly
    n H characters in the file
    '''


def minOperations(n):
    ''' In this function we can oonly performe two operations:
        Copy All and Paste.
        Given a number n, this method calculates the fewest number of
        operations needed to result in exactly n H characters in the file.
        '''
    if not isinstance(n, int):
        return 0
    step = 1
    string = 'H'
    coppied_string = ''
    string_to_paste = ''
    num_operations = 0
    diviser = 1
    while (len(string) < n):
        if step == 1:
            coppied_string = CopyAll(string)
            step += 1
            num_operations += 1
        elif step == 2:
            string = Paste(coppied_string, string)
            step += 1
            num_operations += 1
            print(len(string))
        else:
            if n % len(string) == 0:
                diviser = len(string)
                coppied_string = CopyAll(string)
                string = Paste(coppied_string, string)
                num_operations += 2
                print(len(string))
            elif len(string) % diviser == 0:
                string = Paste(coppied_string, string)
                num_operations += 1
                print(len(string))
    return num_operations


def CopyAll(string):
    '''
        Helping function
        '''
    return string


def Paste(string_to_paste, string):
    ''' Helping Function
        '''
    string += string_to_paste
    return string

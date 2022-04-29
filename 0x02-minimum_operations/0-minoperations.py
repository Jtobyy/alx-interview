#!/usr/bin/python3
'''
Minimum Operations
'''


def minOperations(n):
    '''
    calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    '''
    if n <= 1:
        return 0
    elif n <= 5:
        return n
    elif is_prime(n):
        return n
    else:
        h_p = highest_prime_mult(n)  # h_p: highest prime
        f_n = h_p + 1  # counts operations(+1 for copy op),
        # f_n: fewest number of ops
        c_n = h_p  # counts hashes, c_n: current number of hashes
        while c_n < n:
            f_n += 1  # paste
            c_n += h_p
        return f_n


def is_prime(n):
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True


def highest_prime_mult(n):
    temp = 2
    for i in range(2, int(n/2)):
        if n % i == 0:
            for j in range(2, int(i/2)):
                if i % j == 0:
                    break
            else:
                temp = i
    return temp

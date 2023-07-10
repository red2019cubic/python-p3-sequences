#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    i = 0
    j = 1
    if length > 0:
        fibonacci_list.append(i)
    if length > 1:
        fibonacci_list.append(j)
    if length > 2:
        while length > 2:
            fibonacci_list.append(
                fibonacci_list[i - j] + fibonacci_list[i - (j + 1)])
            length -= 1
    print(fibonacci_list)

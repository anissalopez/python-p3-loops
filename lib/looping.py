#!/usr/bin/env python3
import ipdb

def happy_new_year():
    num = 10
    while (num > 0):
        print(num)
        num -= 1
    if(num == 0):
        print("Happy New Year!")

    pass

def square_integers(int_list):

    new_list = list()
    for num in int_list:
        newNum =  num * num
        new_list.append(newNum)

    return new_list

def fizzbuzz():
    num = 1


    while (num <= 100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
        num += 1
    
print(fizzbuzz())
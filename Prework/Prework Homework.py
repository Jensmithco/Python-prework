# Question 1

#Write a function to print "hello_USERNAME!" USERNAME is the input of the funtion.
#The first of the code has been defined as below.

def hello_name(user_name):

        """prints a simple message"""

        print("hello" + "_" + user_name + "!")
        
hello_name('USERNAME')


#Question #2

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():

    """prints odd numbers from 1-100"""

    for number in range(1,100):
        if number % 2 != 0:
            print(number)

first_odds()

#Question 3

#Please write a Python function, max_num_in_list to return the max number of a given list.
#The first line of the code has been defined as below.

def max_num_in_list(a_list):

    """returns the max number in a given list"""

    maxnum = print(max(a_list))
    return maxnum


my_list = [1, 5, 8, 12, 23, 4, 13]
max_num_in_list(my_list)

#Question 4

#Write a funtion to return if the given year is a leap year. A leap year is divisible by 4,
#but not divisible by 100, unless it is also divisible by 400. The return should be boolean
#Type (true/false)

def is_leap_year(a_year):

    """returns whether a year is a leap year"""

    if int(a_year) % 4 == 0 and int(a_year) % 100 != 0:
        return True
        
    elif int(a_year) % 100 != 0 and int(a_year) % 400 == 0:
        return True
        
    else:
        return False

print(is_leap_year(1956))

#Question 5

# Write a function to check to see if all numbers in list are consecutive numbers. For
# example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive
# numbers. The return should be boolean Type.

def is_consecutive(a_list):

    """checks to see if numbers in a list are consecutive"""

    if sorted (a_list) == list(range(min(a_list), max(a_list)+1)):
            return True
    else:
            return False



jen_list = [3, 4, 5, 6, 7, 8]
jen_list2  = [2, 5, 6, 9]

print(is_consecutive(jen_list2))
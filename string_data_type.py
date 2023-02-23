# string:- sequences of characters

# how  to define multi-line string literals:
# Eg:-
# s ='''abhishek
# sunil 
# khodke'''
# print(s)

# how to access characters of a string:
# 1 By using index
# 2 By using slice operator

# 1 By using index:-
# Eg:-
# s = 'abhishek'
# print(s[7])  

# s = "abhishek"
# print(s[0])

# s = 'abhishek'
# print(s[-1])

# s ='abhishek'
# print(s[8])   # index error


# s = input("Enter some string:-")
# i = 0
# for x in s:
#     print(f"positive index {i} negative index {-i} is{x}".format(i,i-len(s),x))
#     i =i+1

# Accessing characters by using slice operator:-

# s = 'abhishek'
# print(s[1:2:1])

# s = "abhi"
# print(s[::])

# s = "abhi"
# print(s[:])

# s = 'abhi'
# print(s[-1:])   # print i

# s = "abhishek"
# print(s[-1::])  # print k

# s = "i am learing python"
# print(s[::-1])   # nohtyp gnirael ma i

# s = "index and slicing"
# print(s[:7])      # index a

# s = " index and slicing"
# print(s[7:])    # and slicing

# s = "string is squences of characters"
# print(s[0:len(s):2])     # srn ssune fcaatr


# in forward direction:
# default value for begin:-  0
# default value for end:-  length of string
# default value for step:-  +1


# in backward direction: 
# default value for begin:-  -1
# default value for end:-  -(length of string+1)

# mathematical operators in string:-
# 1 + operator for concatenation  Eg:- print("abhishek "+"khodke") op- abhishek khodke
# 2 * operator for repetition   Eg:-print("Hello"*"Hello")  op- HelloHello

# String Methods:-
# capitalize()	Converts the first character to upper case
# count()	Returns the number of times a specified value occurs in a string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# join()	Converts the elements of an iterable into a string
# lower()	Converts a string into lower case
# upper()	Converts a string into upper case
# replace()	Returns a string where a specified value is replaced with a specified value
# split()	Splits the string at the specified separator, and returns a list
# title()	Converts the first character of each word to upper case
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rsplit()	Splits the string at the specified separator, and returns a list


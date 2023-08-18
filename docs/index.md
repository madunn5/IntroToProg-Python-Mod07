# Pickling in Python
**Dev:** *MDunn*   
**Date:** *8.17.2023*

## Introduction
In this paper I will go over how I created a Python program that implements pickling and exception handling into the code. This was my first opportunity to test what I have learned so far and make a program from scratch in whatever way I see fit. It also gave me the opportunity to research pickling and exception handling as that was not something that was covered very deeply in the lecture purposefully.

## Researching Pickling in Python
Pickling in Python means to serialize and deserialize data types, most commonly be turning the loaded data in binary data. Pickle is the name of the Python specific module that is used to accomplish serializing/deserializing the data. Pickle.dump() or Pickle.dumps() are the functions used to serialize an object, the difference being that .dump() writes the data to a file and .dumps() represents it as a byte object. Pickle.load() or Pickle.loads() are the functions used to deserialize an object, and just like the dump functions the difference between the two is the same – either from a file or from byte object. For this assignment, I used .dump() and .load(). There will be examples of both functions later in this assignment. 

The source I used to research Pickling was https://www.datacamp.com/tutorial/pickle-python-tutorial and I found their examples to be very helpful as I started writing my code.

## Researching Exception Handling in Python
Exception Handling in Python must deal with how errors in the program can arise, and how the code handles them. So far in the course, I have had instances where I’ve had to code around errors, but they have mostly been handled by use if/else statements. Exception Handling allows for the use of built in functions that can relay the error to the user, but they also allow for custom error creating as well. These functions can range from ValueErrors, which occur when the wrong argument is given, or errors like ZeroDivisionError that are clearer in their name. I found that using Exception as e: is the type of handling that worked best for me in the code as it is the broadest and allows for catching more errors that I might not be thinking of in most situations. In situations where one type of error is most common, it would make more sense to use the specific type of Error, like a ZeroDivisionError for a math function where dividing by 0 is possible. For this program I felt like taking a broader approach would be preferable.

The sources I used to research Exception Handling were https://www.geeksforgeeks.org/python-try-except/ , https://www.tutorialspoint.com/python3/python_exceptions.htm#, https://embeddedinventor.com/python-except-exception-as-e-meaning-explained/. I found each website to be helpful for all the examples I ended up using in my code.

## Creating & Testing the Program
Once I had completed enough research to feel confident about performing the task at hand, I started to right my code one section at a time. I built off our previous homework assignments up to this point, and I thought that trying to build something like Assignment 06 might be a good challenge for me, so that was the path I started down.

The first section of the code acts a log of information about what the code should accomplish, as well as any changes made to the code so that anyone can come in and get an idea of what is going on. 

'''
-------------------------------------------------
Title: Assignment 07 - Pickling
Description: A simple example of storing data in a binary file
              and then using pickle to unpickle it. Additionally,
              the program can print the data to a text file,
              delete all previously saved data and show the user
              the binary data
ChangeLog: (Who, When, What)
MDunn,8/17/2023,Created Script
-------------------------------------------------
'''

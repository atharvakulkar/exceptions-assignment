#!/usr/bin/env python
# coding: utf-8

# Q1. What is an Exeption in python? Write the difference between Exceptions and syntax errors?

# In[2]:


An exception in Pyrhon is an error that occurs during the execution of prgram
   It may be due to various reasons such as invali input, division by zero
   out("of", "memeory,or", "typing", "to", "access", "an", "undefiend", "variable.")
   When an exception occurs the normal flow of program is disrupted
   and the program terminates
   
   
   
   The key differnece between exceptions and syntax errors is thst 
   exceptions occur during the execution of program while syntax errors occur 
   before the program is executed.Additonally,exceptions can be handeled or reolved progrma
   programmitically,but erroes are to be fixed manually
   


# 
# Q2. What happens when an exception is not handled? Explain with an example

# In[3]:


When an excepion is not handeled, the program termianets abruptly and generates a traceback
which is a detailed report of the error that occured
The traceback provides the information about the line of code where the error has occured
the("type", "of", "errror", "and", "the", "discripton", "of", "error")


# In[4]:


def divide(x,y):
    result=x/y
    return result

print(divide(10,5))
print(divide(10,0))


# Q3. Which Python statements are used to catch and handle exceptions? Explain with an example

# In[5]:


In Python,exceptions can be caught and  handled using the try and except statements
The try block contains the code that might riase an exception and the except block
contains the code that will handle the exceptions if it occurs.


# In[7]:


## ZeroDivisionError example
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError :
        print("cannot divide by zero")
    else:
        return result
    
print(divide(10,5))
print(divide(10,0))


# Q) 4 Explain with example
#    ** try and else
#     ** finally
#     ** raise
# 

# In[9]:


# try and else
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        return result

print(divide(10, 5)) # Output: 2.0
print(divide(10, 2)) # Output: 5.0


# In[10]:


#finally
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        result = None
    finally:
        print("executing finally block")
    return result
print(divide(10,5))
print(divide(10,0))


# In[ ]:


## raise 
def divide (x,y):
    if y == 0:
        raise  ZeroDivisionError("Cannot divide by zero")
    return x / y

try:
    print(divide(10,5))
    print(divide(10,0))
except ZeroDivisionError as e:
    print(e)    
    


# Q5. What are custom exceptions in python ? why do we need custo  exceptions ?
# explain with an example
# 

# In[12]:


Custom Exceptions are user defined exceptions in python.They allow
ypu to define specific type of exceptions for your application,so you an handle
errors and exceptions in a mroe organized and meaningful way 




For example, consider a scenario where you are writing a library that performs some mathematical calculations. In this library, you may encounter several different types of errors, such as invalid input, overflow, and divide-by-zero errors. You could handle these errors by raising built-in exceptions, such as ValueError or ZeroDivisionError, but it may not provide enough context or information about the error that has occurred.


# In[14]:


class InvalidInputError(Exception):
    pass

class OverflowError(Exception):
    pass

class DivideByZeroError(Exception):
    pass

def divide(x, y):
    if y == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return x / y

def calculate(x, y):
    try:
        if x < 0 or y < 0:
            raise InvalidInputError("Input values must be positive")
        result = divide(x, y)
    except DivideByZeroError as e:
        print(e)
    except InvalidInputError as e:
        print(e)
    else:
        return result

print(calculate(10, 5)) # Output: 2.0
print(calculate(-10, 5)) # Output: Input values must be positive
print(calculate(10, 0)) # Output: Cannot divide by zero
     


# Q6. Create a custom exception class. Use this class to handle an exception

# In[16]:


class CustomException(Exception):
    pass

def divide(x, y):
    if y == 0:
        raise CustomException("Cannot divide by zero")
    return x / y

try:
    print(divide(10, 5)) # Output: 2.0
    print(divide(10, 0))
except CustomException as e:
    print(e) # Output: Cannot divide by zero
     


# In[ ]:





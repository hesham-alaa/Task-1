#!/usr/bin/env python
# coding: utf-8

# # Task 1 ( Basics )

# # Question 1 :
# Define a function which can compute the sum of two numbers.
# 
# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

# In[13]:


num1=2
num2=5
sum=num1+num2


# # Question 2:
# 
#     Write a method which can calculate square value of number
# 
# Hints:
#     Using the ** operator
# 

# In[15]:


sum**2


# # Question 3
# Define a function that can convert a integer into a string and print it in console.
# 
# Hints:
# 
# Use str() to convert a number to string.

# In[17]:


type(sum)
convert_number=str(sum)
print(type(convert_number))


# # Question 4 :
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
# 
# Hints:
# 
# Use int() to convert a string to integer.

# In[57]:


num3=input('Plz enter first number\t')
num4=input('Plz enter second number\t')
num3=int(num3)
num4=int(num4)
sum1=num3+num4
print('sum1 =',sum1)


# # Question 5 :
# Define a function that can accept two strings as input and concatenate them and then print it in console.
# 
# Hints:
# 
# Use + to concatenate the strings
# 

# In[71]:


M=input('plz enter 1st string :')
S=input('plz enter 2nd string:')
S=str(S)
M=str(M)
print(M+S)


# # Question 6 :
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
# 
# Hints:
# 
# Use len() function to get the length of a string

# In[72]:


print(M)
print(S)
print('length of M=',len(M))
print('length of S=',len(S))
if len(M) == len(S):
    print('al l strings line by line.')


# # Question 7 :
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
# 
# Hints:
# 
# Use % operator to check if a number is even or odd.

# In[58]:


print('sum1=',sum1)
if (sum1 % 2)!=0:
    print('sum1 is odd')
elif (sum1 % 2)==0:
        print('sum1 is even')


# # Question 8 :
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
# 
# Hints:
# 
# Use if statement to judge condition.

# In[93]:


st=input('plz enter 1st string:')
st=str(st)
if st== 'yes' or st== 'YES' or st== 'Yes' :
    print('yes')
else :
    print('NO')    


# In[95]:


st=input('plz enter 1st string:')
st=str(st)
if st== 'no' or st== 'NO' or st== 'No' :
    print('NO')
else :
    print('YES')


# # Question 9 :
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# 
# Hints: 
# Consider use range(#begin, #end) method

# In[ ]:





# In[ ]:





# In[ ]:





# # Question 10 :
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# In[10]:


#Search about it please


# In[ ]:





# In[ ]:





# In[ ]:





# # Question 11 :
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# 

# In[ ]:





# In[ ]:





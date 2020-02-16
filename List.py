#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[4]:


import random

def generateList(size, lowerbound, upperbound):
    assert size > 0, "List cannot be empty"
    assert type(size) == int, "Size must be a integer value"
    lst = []
    for i in range(size):
        lst.append(random.randint(lowerbound,upperbound))
    return lst

def sum(inputList):
    sum = 0
    for number in inputList:
        sum += number
    return sum

def average(inputList):
    return sum(inputList)/len(inputList)
        

userLengthOfList = int(input("Please enter the length for the list: "))
lowerBoundOfList = int(input("Please enter the lower bound for the range of integer values: "))
upperBoundOfList = int(input("Please enter the upper bound for the range of integer values: "))
currentList = generateList(userLengthOfList, lowerBoundOfList, upperBoundOfList)
print(currentList)
print("List length: " + str(len(currentList)))
print("Largest Integer: " + str(max(currentList)))
print("Smallest Integer: "+ str(min(currentList)))
print("Sum: " + str(sum(currentList)))
print("Average: " + str(average(currentList)))


# In[ ]:





# In[ ]:





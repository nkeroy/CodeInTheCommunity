#!/usr/bin/env python
# coding: utf-8

# In[5]:


# FUNCTIONS
def buildGlobalDict():
    # open file
    file = open("C:\\Users\\nkero\\Downloads\\word_list.txt", "r")
    # read line
    # build dictionary
    while(True):
        line = file.readline()
        if line == "":
            break
        processLine(line,globalDict)
    print("Finished building globalDict {}")
    
    

def processLine(line, dict):
    line = line.strip()
    level = dict
    for letter in line:
        if letter == "\n":
            continue
        
        elif letter not in level.keys():
            level[letter] = {}
        level = level[letter]
    
def checkWord(word, dict):
    level = dict
    for letter in word:
        if letter not in level.keys():
            return False
        level = level[letter]
    return True

def game():
    previousLetter = ""
    currentGameDict = {}
    while(True):
        word = input("Please enter a word: ")
        # if word does not exist
        if not checkWord(word, globalDict):
            print("You didn't type a word found in word_list.txt")
            break
        # if current word does not start with previous word last letter
        elif previousLetter != "" and word[0] != previousLetter:
            print("You didn't type a word that starts with " + "\'" + previousLetter + "\'")
            break
        # if word has already be used before
        elif checkWord(word, currentGameDict):
            print("You typed a word that has been used before")
            break
        else:
            processLine(word, currentGameDict)
            previousLetter = word[-1]

globalDict = {}
buildGlobalDict()
game()


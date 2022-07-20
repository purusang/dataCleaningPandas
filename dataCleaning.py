# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 08:16:02 2022

@author: DELL

Using the excel attached below, i'd like a clean data using regex and build a function that does the following.

load data and clean it
look at the text column in the spreadsheet. 
i want to label it 0 for being a specific description 
and 1 for being a general description (having other)

function 1 - general function of instances of other
if it has OTHER, OTHER/OTHER, OTHER:OTHER, OTH label 0 
else 1 in a new column

function 2 a function to show change from 0 to 1 , 0 to 0, 1 to 0 and 1 to 1

function 3/ a function showing how general the text is.

if it has other or OTH it is 0 and Low
if it has other:other or other:other:other it is 0 Medium
if it has more than 3 others in per row then it's 0 Maximum
else it is specific


0 specific  
1 for general

"""

import pandas as pd
import re
def function1(str):
    if re.search(r"\b(OTHER|OTH)\b",str, re.IGNORECASE):
        return True
    return False
def function2(df):
    column1 = df['label_binary']
    column2 = df['othersFound']
    changes = []
    for col1, col2 in zip(column1, column2):
        if col1 == 0 and col2 ==0:
            changes.append("0 to 0")
        elif col1 == 0 and col2 ==1:
            changes.append("0 to 1")
        if col1 == 1 and col2 ==0:
            changes.append("1 to 0")
        if col1 == 1 and col2 ==1:
            changes.append("1 to 1")
    return changes
def function3(df):
    p  = re.compile(r"\b(OTHER|OTH)\b", flags = re.IGNORECASE)
    counts = []
    for string in df['text']:
        m = p.findall(str(string))
        general = 'specific'
        if len(m)>3:
            general = "Maximum"
        elif len(m) >1:
            general = "Medium"
        elif len(m) == 1:
            general = "Low"
        counts.append(general)
    return counts

df = pd.read_csv('D:/upwork/dataCleaning/data_2.csv',sep=',', on_bad_lines='skip' , index_col=False, dtype='unicode')
# print(df['text'])

print("---------------")
othersFound = [0 if(function1(str(d)))  else 1 for d in df['text']]
# print(othersFound)
df['othersFound'] = othersFound
# print(df)    

# #show changes
# showChanges = function2(df)
# # print(othersFound)
# df['showChanges'] = showChanges
# # print(df.to_string())    

#count
generality = function3(df)
df['generality'] = generality
    
# print(df.to_string())

df.to_csv("D:/upwork/dataCleaning/result1.csv")
    
    
    
    
    
    
    
    
    
    
    
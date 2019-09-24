# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:21:44 2019

@author: Angelina Paredes
"""

import csv
import pandas as pd
import efficient_apriori as ep

# documentation from https://buildmedia.readthedocs.org/media/pdf/efficient-apriori/latest/efficient-apriori.pdf
index = 0
temp = 0
# Data cleaning and inserting delimiter into the data
with open("browsing-data.txt", 'r') as csvfile:
    hw1reader = csv.reader(csvfile, delimiter=' ')
    for row in hw1reader:
        new_str = ''
        if index == 0:
            temp = len(row)
        elif len(row) > temp:
            temp = len(row)
        index = index + 1
        for x in range(len(row)): 
            if (row[x] != ''):
                new_str += row[x]
                new_str += ','

maxLength = temp
index = 0
temp = 0
new_file = ''

with open("browsing-data.txt", 'r') as csvfile:
    hw1reader = csv.reader(csvfile, delimiter=' ')
    for row in hw1reader:
        new_str = ''
        index += 1
        for x in range(len(row)): 
            if (row[x] != ''):
                new_str += row[x]
                new_str += ','
        if(len(row) < maxLength):
            diff = maxLength - len(row)
            for x in range(len(row), maxLength):
                new_str += ','
                   
        new_file = new_file + '\n' + new_str + '\n'
       
with open("browsing-txt1.txt", "w+") as f:
    f.write(new_file)
f.close ()
#creating a new data frame from updated browsing data
data = pd.read_csv('browsing-txt1.txt')
records = []
for i in range(0,100):
    records.append([str(data.values[i,j]) for j in range(0, 32)]) #creating list of list for apriori algorithm 
for i,j in enumerate(records):
    while 'nan' in records[i]: records[i].remove('nan') # removes Nan from data set 
support = 100 / len(records) # minimum support 
print(support)
itemsets, rules = ep.apriori(records, min_support = .075)  #I tried 100/# of elements but it returns an empty set
output = open('output.txt', 'w+')
#descending confidence values for itemsets size 2
rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
for i,rule in enumerate(sorted(rules_rhs, key=lambda rule: rule.confidence)):
        if i < 5:
            rule_file = str(rule.lhs[0]) + " -> " + str(rule.rhs[0]) + " " + str(rule.confidence) + "\n"
            output.write(rule_file)
            
            
#descending confidence values for itemsets size 3     
rules_rhs = filter(lambda rule: len(rule.lhs) == 2 and len(rule.rhs) == 1, rules)
for i,rule in enumerate(sorted(rules_rhs, key=lambda rule: rule.confidence)):
        if i < 5:
            rule_file = str(rule.lhs[0]) + " " +str(rule.lhs[1])+ " -> " + str(rule.rhs[0]) + " " + str(rule.confidence) + "\n"
            output.write(rule_file)
output.close()
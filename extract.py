#!/usr/bin/python

import os
import re #regular expressions
import csv
from collections import Counter


def processFile(fieldSearch, termToSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums):
    #open the original textfile
    #readerFile = open(filename, 'r')
    newfile = open(filenameOutput, 'w')
    
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiterInput, quotechar='|')
        rownum = 0
        for row in spamreader:
            if rownum == 0:
                newfile.write(delimiterOutput.join(row) + '\n')
            else:
                if fieldSearch <> "allfields": #if term can only be in one specific field
                    rowContents = str(row)
                    if termToSearch.lower() in rowContents.lower():
                    	print termToSearch + " " + termToSearch.lower() + "\n" + rowContents + "\n" + rowContents.lower()
                    	fieldContents = row[int(fieldSearch)]
                        #if termToSearch in row[int(fieldSearch)] : #if the term is found in the specific field, print it
                        if termToSearch.lower() in fieldContents.lower() : #if the term is found in the specific field, print it
                            print "Found the text " + "'" + termToSearch + "' in line number: " + str(rownum) +  " and in field #" + str(fieldSearch) + "\n"
                            newfile.write(delimiterOutput.join(row) + '\n') #join all values of row with the new delimiter and print it into the new file
                else: #if the term can be in any field
                    rowContents = str(row)
                    if termToSearch.lower() in rowContents.lower() : #i need to change this to "like" instead so that it looks for strings inside each word
                        print "Found the text " + "'" + termToSearch + "' in line number: " + str(rownum) + "\n"
                        newfile.write(delimiterOutput.join(row) + '\n')
            rownum += 1

filename = raw_input("what file would you like to query and extract from? ") 
path = './'

print "You will be searching and extracting from " + filename
rownum = 0
print "The first line of your file is the following: \n" #show first line for user to be able to determine the delimiter
with open(filename, 'rb') as f:
#    if rownum == 0:
#       rownum += 1
    for row in f:
#    lines = f.readlines(0)
        if rownum == 0:
            print row
            rownum += 1
        break
#print lines[0]
#select the delimiter to use
delimiterInput = raw_input("What delimiter is your file using? leave blank if unformatted ")
#if not delimiter is specified, the script will use space as delimiter
if delimiterInput == '':
    delimiterInput = ' '    
print "The fields and field numbers are the following: \n" #show all fields with their number
#fields = lines[0].split(delimiterInput)
fields = row.split(delimiterInput)
#print fields[0] #prints the first field
fieldNums = len(fields) #determine how many fields there are in each line
x = 0
while x < fieldNums: #shows the field names with their numbers in the file
        print str(x) + ' ' + fields[x]
        x += 1

    
fieldSearch = raw_input("Select a field number to search (leave blank for all fields): ")
#if no specific field is chose, all fields will be searched
if fieldSearch == '':
    fieldSearch = 'allfields'
print "you will be searching field: " + fieldSearch #display the field to search
#user input for text to search
termToSearch = raw_input("What string would you like to search: ")
#user chooses the delimiter to use in the output file
delimiterOutput = raw_input("What delimiter would you like to use in your output? ")
#filename.close()
#user chooses an output file. If no name is given, the default is newfile.txt
#all files that exist already will be overwritten
filenameOutput = raw_input("What filename would you like to give your new file (newfile.txt is default).\n If file exists already, it will be overwritten: ")
if filenameOutput == '':
    filenameOutput = 'newfile.txt'
#run the function processFile() with the following filled variables from above
processFile(fieldSearch, termToSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums) 
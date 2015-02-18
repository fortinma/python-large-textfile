#!/usr/bin/python

import os
import re #regular expressions
import csv

#select file
#display first line of file
#choose delimiter
#choose field to search (number)
#choose text to search
#run through extraction
#select new delimiter
#save to new file (must create new filename from search) 
#selecting the filename

#process the text file with delimiter, new delimiter
#search the text file using a specific field, or not
#with results create a new textfile
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
                    if termToSearch in row:
                        if row[int(fieldSearch)] == termToSearch: #if the term is found in the specific field, print it
                            print "Found the text " + "'" + termToSearch + "' in line number: " + str(rownum) +  " and in field #" + str(fieldSearch) + "\n"
                            newfile.write(delimiterOutput.join(row) + '\n') #join all values of row with the new delimiter and print it into the new file
                else: #if the term can be in any field
                    if termToSearch in row: #i need to change this to "like" instead so that it looks for strings inside each word
                        print "Found the text " + "'" + termToSearch + "' in line number: " + str(rownum) + "\n"
                        newfile.write(delimiterOutput.join(row) + '\n')
            rownum += 1

    #open the new file to export to 
    
    
    #read lines from file
    #header = readerFile.readlines()
    #using the initial delimiter, extract the first line for the file that contains
    #field names
    #headerPrint = header[0].split(delimiterInput)
    #close that file
    #readerFile.close()
    #open the file again in order to process the data
    #readerFile = open(filename, 'r')
    #write the header with field names to the new file
    
    '''
    y = 1
    h = 1 #to count lines searched
    for line in spamreader:
        print "line " + str(h) + " processed."  #print the line currently being searched
        h += 1
        if fieldSearch <> "allfields": #if a specific field is chosen
            if termToSearch in line:
                partsofLine = line.split(delimiterInput) #split lines one by one with the initial delimiter
                linebylinenum = len(partsofLine)
                if linebylinenum <> fieldNums:
                    print "mismatched number of fields on "
                if termToSearch in partsofLine[int(fieldSearch)]: #if the term is found in the specific field
                    print str(y) + " record(s) added to " + filenameOutput #show number of records being added to file
                    y += 1
                    t = 0
                    while t < fieldNums: #write data into new file if text can be found in the field
                        newfile.write(partsofLine[t] + delimiterOutput) 
                        t += 1
            else:
                print "not found in line # " + str(h)
        else: #if any field should be searched
            if termToSearch in line: #if term is found anywhere in the line
                newfile.write(line)
                print line
            else:
                print "not found in line # " + str(h)
    newfile.close() #once finished processing, close both the input and output files
    readerFile.close()
    '''
    
filename = raw_input("what file would you like to extract from? ") 
path = './'

print "You will be searching and extracting from " + filename
with open(filename, 'r') as f:
    rownum = 0
    if rownum == 0:
        lines = f.readlines()
        rownum += 1
    print "The first line of your file is the following: \n" #show first line for user to be able to determine the delimiter
    print lines[0]
    #select the delimiter to use
    delimiterInput = raw_input("What delimiter is your file using? leave blank if unformatted ")
    #if not delimiter is specified, the script will use space as delimiter
    if delimiterInput == '':
        delimiterInput = ' '    
    print "The fields and field numbers are the following: \n" #show all fields with their number
    fields = lines[0].split(delimiterInput)
    #print fields[0] #prints the first field
    fieldNums = len(fields) #determine how many fields there are in each line
    f.close() #close the input file
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
#run the function processFile
processFile(fieldSearch, termToSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums)
 

#!/usr/bin/python

import os
#select file
#display first line of file
#choose delimiter
#choose field to search (number)
#choose text to search
#run through extraction
#select new delimiter
#save to new file (must create new filename from search) 
#selecting the filename


def processFile(fieldSearch, termToSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums):
    readerFile = open(filename, 'r')
    newfile = open(filenameOutput, 'w')
    header = readerFile.readlines()
    headerPrint = header[0].split(delimiterInput)
    readerFile.close()
    readerFile = open(filename, 'r')
    x = 0
    while x < fieldNums:
        newfile.write(headerPrint[x] + delimiterOutput)
        x += 1
    y = 1
    for line in readerFile:
        if fieldSearch <> "allfields":
            partsofLine = line.split(delimiterInput)
            if termToSearch in partsofLine[int(fieldSearch)]:
                print str(y) + " record(s) added to " + filenameOutput
                y += 1
                x = 0
                while x < fieldNums:
                    newfile.write(partsofLine[x] + delimiterOutput)
                    #print partsofLine[x] + delimiterOutput
                    x += 1
        else:
            if termToSearch in line:
                newfile.write(line)
                print line
    newfile.close()
filename = raw_input("what file would you like to extract from? ")
path = './'
print "You will be searching and extracting from " + filename
with open(filename, 'r') as f:
    lines = f.readlines()
    print "The first line of your file is the following: \n"
    print lines[0]
    delimiterInput = raw_input("What delimiter is your file using? leave blank if unformatted ")
    if delimiterInput == '':
        delimiterInput = ' '    
    print "The fields and field numbers are the following: \n"
    fields = lines[0].split(delimiterInput)
    #print fields[0] #prints the first field
    fieldNums = len(fields)
    f.close()
x = 0
while x < fieldNums:
        print str(x) + ' ' + fields[x]
        x += 1

    
fieldSearch = raw_input("Select a field number to search (leave blank for all fields): ")
if fieldSearch == '':
    fieldSearch = 'allfields'
print "you will be searching field: " + fieldSearch
termToSearch = raw_input("What string would you like to search: ")
delimiterOutput = raw_input("What delimiter would you like to use in your output? ")
#filename.close()
filenameOutput = raw_input("What filename would you like to give your new file (newfile.txt is default).\n If file exists already, it will be overwritten: ")
if filenameOutput == '':
    filenameOutput = 'newfile.txt'

processFile(fieldSearch, termToSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums)
    

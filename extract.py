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

#process the text file with delimiter, new delimiter
#search the text file using a specific field, or not
#with results create a new textfile
def processFile(fieldSearch, termToSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums):
    #open the original textfile
    readerFile = open(filename, 'r')
    #open the new file to export to 
    newfile = open(filenameOutput, 'w')
    #read lines from file
    header = readerFile.readlines()
    #using the initial delimiter, extract the first line for the file that contains
    #field names
    headerPrint = header[0].split(delimiterInput)
    #close that file
    readerFile.close()
    #open the file again in order to process the data
    readerFile = open(filename, 'r')
    #write the header with field names to the new file
    
    x = 0
    while x < fieldNums:
        newfile.write(headerPrint[x] + delimiterOutput)
        x += 1
    y = 1
    for line in readerFile:
        if fieldSearch <> "allfields": #if a specific field is chosen
            partsofLine = line.split(delimiterInput) #split lines one by one with the initial delimiter
            linebylinenum = len(partsofLine)
            if linebylinenum <> fieldNums:
                print "mismatched number of fields on "
            if termToSearch in partsofLine[int(fieldSearch)]: #if the term is found in the specific field
                print str(y) + " record(s) added to " + filenameOutput #show number of records being added to file
                y += 1
                x = 0
                while x < fieldNums: #write data into new file if text can be found in the field
                    newfile.write(partsofLine[x] + delimiterOutput) 
                    x += 1
        else: #if any field should be searched
            if termToSearch in line: #if term is found anywhere in the line
                newfile.write(line)
                print line
    newfile.close() #once finished processing, close both the input and output files
    readerFile.close()
filename = raw_input("what file would you like to extract from? ") 
path = './'
filename = "AddressPoints.txt" #only temporary...because i am doings this over and over
                                #when starting this
print "You will be searching and extracting from " + filename
with open(filename, 'r') as f:
    lines = f.readlines()
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
#currently getting the following error, which i think is because of malformatted records:
#Traceback (most recent call last):
#File "extract.py", line 98, in <module>
# processFile(fieldSearch, termToSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums)
#File "extract.py", line 44, in processFile
#if termToSearch in partsofLine[int(fieldSearch)]: #if the term is found in the specific field
#IndexError: list index out of range

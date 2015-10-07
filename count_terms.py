#!/usr/bin/python
#script to search a text file, delimited or not and create analytics (summaries) for all terms used.
import os
import re #regular expressions
import csv
from collections import Counter

#start the function with the variables declared at the bottom

def processFile(fieldSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums):
    #create the environment for a new file
    newfile = open(filenameOutput, 'w') 
    #open the original textfile
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiterInput, quotechar='|') #used to parse quickly, delimited files
        rownum = 0
        for row in spamreader:
            if rownum == 0:
                # If this is the first line, print into the new file, the header of the original file
                newfile.write(delimiterOutput.join(row) + '\n\n') 
                newfile.write("Field analyzed: " + str(row[int(fieldSearch)]) + "(" + fieldSearch +")\n\n") 
                #open a string called wordstring
                wordstring = "" 
            else:
                if fieldSearch <> "allfields": #if term can only be in one specific field
                    #rowContents = str(row)
                 	fieldContents = row[int(fieldSearch)]
                        #keep adding to the wordstring list and separate all terms with the delimiter '$$'
                        #not using a space, because there are plenty of terms I want to evaluate as full names. Example: Lake St. John
                        wordstring += '$$' + str(fieldContents) 
                else: #if the term can be in any field
                    rowContents = str(row)
                    #wordstring += rowContents.split(delimiterInput)
                    wordstring += rowContents
                    #newfile.write(delimiterOutput.join(row) + '\n')
            rownum += 1
    wordlist = wordstring.split('$$')
#    print "wordstring: " + wordstring + '\n'
#    print "wordlist: " + str(wordlist) + '\n' 
#    print "w: "
#    for w in wordlist:
#        print w
#        wordfreq.append(wordlist.count(w)) 
#        print str(wordlist.count(w))
#    newfile.write(delimiterOutput.join(str(zip(wordlist, wordfreq))))       
#    newfile.write(str(zip(wordlist, wordfreq)))
    wordListToFreqDict(wordlist, newfile) # run function wordListtoFreqDict with our list of words and the newfile to write them to

#################################
def wordListToFreqDict(wordlist, newfile):
    wordfreq = [wordlist.count(p) for p in wordlist]
    #return dict(zip(wordlist, wordfreq))
    sortFreqDict(dict(zip(wordlist, wordfreq)), newfile) # run the sortFeqDict function with the wordlist and wordfreq and the newfilename to write them to


def sortFreqDict(freqdict, newfile):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    newfile.write("Term" + str(delimiterOutput) + "Frequency\n")
    for s in aux:
        place = s[1]
        nums = s[0]
        newfile.write(str(place) + str(delimiterOutput) + str(nums) + "\n")
        print str(place) + ' ' + str(nums)



#################################

####################
#Script starts here#
####################
filename = raw_input("what file would you like to query and extract from? ")  #asks user to select a file to process
path = './'

print "You will be counting terms in file: " + filename
rownum = 0
print "The first line of your file is the following: \n" #show first line for user to be able to determine the delimiter
with open(filename, 'rb') as f:
    for row in f:
        if rownum == 0:
            print row
            rownum += 1
        break
#select the delimiter to use
delimiterInput = raw_input("What delimiter is your file using? leave blank if unformatted? ")
#if not delimiter is specified, the script will use space as delimiter
if delimiterInput == '':
    delimiterInput = ' '    
print "The fields and field numbers are the following: \n" #show all fields with their number
fields = row.split(delimiterInput)
fieldNums = len(fields) #determine how many fields there are in each line
x = 0
while x < fieldNums: #shows the field names with their numbers in the file
        print str(x) + ' ' + fields[x]
        x += 1

    
fieldSearch = raw_input("Select a field number to analyze (leave blank for all fields): ")
#if no specific field is chose, all fields will be searched
if fieldSearch == '':
    fieldSearch = 'allfields'
print "you will be searching field: " + fieldSearch #display the field to search
#user input for text to search
#termToSearch = raw_input("What string would you like to search: ")
#user chooses the delimiter to use in the output file
delimiterOutput = raw_input("What delimiter would you like to use in your output? ")
#filename.close()
#user chooses an output file. If no name is given, the default is newfile.txt
#all files that exist already will be overwritten
filenameOutput = raw_input("What filename would you like to give your new file (newfile.txt is default).\n If file exists already, it will be overwritten: ")
if filenameOutput == '':
    filenameOutput = 'newfile.txt'
#run the function processFile() with the following filled variables from above
processFile(fieldSearch, delimiterOutput, delimiterInput, filenameOutput, filename, fieldNums) 
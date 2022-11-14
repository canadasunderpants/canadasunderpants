# -*- coding: utf-8 -*-
#------------------------------------------#
# Title: CDInventory.py
# Desc: Script CDINventory to store CD Inventory data
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#JdenHaan, 2022-Nov-06, added CD inventory script
#JdenHaan, 2022-Nov-12, added read and updated write functionality
#------------------------------------------#
"""
Created on Fri Nov 11 19:07:59 2022

@author: jonat
"""

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data dictionary
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('Write or Read file data.')
while True:
    print('\n[a] add data to list\n[w] to write data to file\n[r] to read data from file')
    print('[d] display data\n[e] to erase entry in memory\n[exit] to quit')
    strChoice = input('a, w, r, d, e, or exit: ').lower()  # convert choice to lower case at time of input
    print('\n\n')

    if strChoice == 'exit':
        break
    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Add data to list in memory
        print('you chose to add a CD')
        dicRow['id'] = int(input('Enter an ID: '))
        dicRow['album'] = input('Enter the Album name: ')
        dicRow['artist'] = input('Enter the Artist\'s name: ')
        lstTbl.append(dicRow)
        print(lstTbl)
        pass
    elif strChoice == 'w':
        # List to File
        # TODO add code here to write from in-memory list to file
        print('your file will be called "CDInventory.txt"')
        strRow = ''
        for row in lstTbl:
            objF = open(strFileName, 'a')
            ID = str(dicRow['id'])
            album = dicRow['album']
            artist = dicRow['artist']
            strRow = [ID,album,artist]
            strRowstr = ','.join(map(str,strRow))
            objF.write(strRowstr)
        objF.close() 
        pass
    elif strChoice == 'r':
        # File to print
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'album': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        # TODO read the file line by line into in-memory list.
        pass
    elif strChoice == 'd':
        # Display data
        # TODO display the data to the user.
        print(lstTbl)
        pass
    elif strChoice == 'e':
        #Delete entry from lstTbl
        print('items currently in memory')
        print('each\'row\':')
        for row in lstTbl:
            print(row)
        print()
        delID = int(input('Which entry would you like to delete? '))
        if delID == dicRow['id']:
            del dicRow['id']
            del dicRow['album']
            del dicRow['artist']
        else:
            print('that entry is not in the CD Inventory')
    else:
        print('Please choose either a, w, r or exit!')
#------------------------------------------#
# Title: CDInventory.py
# Desc: A script to input, output and store CD inventory data using dictionaries 
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# BWorkeneh, 2020-Feb-18, Modified file 
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dictRow = {}  # dictionary of data row
strFileName = 'CDInventory.csv'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':    
        #1 load existing data 
        lstTbl.clear()# per lecture on 18-Jan-2020, clear memory inorder to load from file
        objFile = open(strFileName,'r')
        for row in objFile:
            dictRow= row.strip().split(',')
            dictRow = {'ID': int(dictRow[0]),'Title':dictRow[1], 'Aritst': dictRow[2]}
            lstTbl.append(dictRow) 
        objFile.close()
        if len(lstTbl)== 0:
            print('File was empty\n')
        elif len(lstTbl) >0:
            print('Inventory loaded from file\n')
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {'ID':intID, 'Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dictRow)
        print('\n')
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print('\n')
    elif strChoice == 'd':
        if len(lstTbl)>0:
              delID = None 
              delindex = 0 # a variable for the index of lstTbl containing the entry to be deleted
              notfound = 0 # int used to check if the entered id is not in lstTbl 
              delID = int(input('Enter the ID for the CD you want to remove: '))# input automatically converts to string, type cast to int           
              for row in lstTbl:
                  if delID in row.values():# 
                        del lstTbl[delindex]
                        print('The entry has been deleted')
                  elif delID not in row.values():
                        notfound += 1 
                        if notfound == len(lstTbl):
                          print('The ID is not in the inventory')
                  delindex += 1 
        elif len(lstTbl)==0:
            print('The inventory is empty')
        print('\n')
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')# write mode instead of append mode 
        for row in lstTbl:
            strRow = ''
            for item in row.values():#row.values() instead of row only 
                strRow += str(item) + ',' # ids are saved as string in txt file but converted to int when being used by the program
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')
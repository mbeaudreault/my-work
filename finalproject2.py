#Project Description:
#--------------------
#I chose the program that will read a large amount of flight data and process it
#so that a user can search for specific flights based off of the data provided
#by the data.

#Solution:
#---------
#In order to solve this problem multiple sorting algorithms will
#have to be implemented to sort the provided data. Furthermore search algorithms
#will have to be implemented so the user can search for specific flights. 

#Pseudocode for Main Function:
#-----------------------------
#Get File function to get the file
#Call a function that sorts the data in to a list for each catagory of data
#Have user choose what catagory they want to search for to search for
#Have the user input what they want to search for
#Call the search function with the associated catagory the user is searching for
#Return all the flights and call a function that prints the results

#Function Design:
#----------------

#A function to make sure a valid file is opened
def getFile():
    #Using exception handeling open the file
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file:")
        try:
            file = open(fname, 'r')
            goodFile = True
        except IOError:
            print("In valid filename, please try again...")
    #Return the valid file
    return file

#Using the valid file open get a function to get the data from the file
def getData(file):
    #open the file
    infile = file
    #initialize lists for all of the data in the file
    airLines = []
    flightNums = []
    deptTimes = []
    arrTimes = []
    prices  = []
    line = infile.readline()
    #for the entire file
    while line != "":
        line = line.strip()
        #split the line in the file up and add each pieve of data to their
        #specific lists
        airLine, flightNum, departTime, arrTime, price = line.split(",")
        airLines.append(airLine)
        flightNums.append(flightNum)
        deptTimes.append(departTime)
        arrTimes.append(arrTime)
        prices.append(price)
        #move to the next line and repeat
        line = infile.readline()
    #Close the file
    infile.close()     
    #return all of the data lists
    return airLines, flightNums, deptTimes, arrTimes, prices

#Initialze a function that finds the smallest in a list of data
def findSmallest(dataList):
    #Initialize smallest as the first intem in the list
    smallest = dataList[0]
    #create a list that will hold the index of the smallest
    indexOfSmallest = []
    #initialize index as zero
    index = 0
    #Runs through the entire list of data
    for i in range(len(dataList)):
        #If the ith index of the list is smaller than the smallest make
        #that the smallest and save the index of that
        if dataList[i] < smallest:
            smallest = dataList[i]
            index = i
    #Append the index to the index of smallest list
    indexOfSmallest.append(index)
    #return the list of indexes
    return indexOfSmallest

#Define a function that computes the flight time of a trip
def findFlightTime(deptTimes, arrTimes):
    #initialize a list that will hold all of the flight times
    flightTimes = []
    #for the length of the depart times list
    for i in range(len(deptTimes)):
        #split the depart time into two before and after the ':'
        deptTimeHours, deptTimeMins = deptTimes[i].split(':')
        #Set DeptTime = to 60 times the hours portion of the variable
        #and add the minutes
        deptTime = int(deptTimeHours)*60 + int(deptTimeMins)
        #repeat this for arrival time
        arrTimeHours, arrTimeMins = arrTimes[i].split(':')
        arrTime = int(arrTimeHours)*60 + int(arrTimeMins)
        #Subtract arrival time from depart time to get flight time
        flightTime = arrTime - deptTime
        #add flight times to the list
        flightTimes.append(flightTime)
    #return the list of flight times
    return flightTimes

#define a function that will find something in the data list that the
#user is looking for
def findEquivalent(dataList, searchingFor):
    #initialize indexes of equivalents
    indexesOfEquivalent = []
    #for the length of the data list
    for i in range(len(dataList)):
        #if the index in the data list is equal to what the user is
        #searching for
        if dataList[i] == searchingFor:
            #Save the index and append the index into a list
            index = i
            indexesOfEquivalent.append(index)
    #return the lists of indexes
    return indexesOfEquivalent

#define a function that finds all data inbetween two points
#taking a data list, a high, and a low as a parameter
def findInBetween(dataList, high, low):
    #initialize a list of the indexes of data inbetween
    indexesOfInBetween = []
    #for the length of this data list
    for i in range(len(dataList)):
        #If the data of index i is inbetween these two points
        if int(dataList[i]) < high and int(dataList[i]) > low:
            #save the index and append it to a list
            index = i
            indexesOfInBetween.append(index)
    #return the list of indexes
    return indexesOfInBetween

#define a function that finds the average of a data list
#taking a data list as a parameter
def findAverage(dataList):
    #initialize a sum to zero
    Sum = 0
    #for the lenght of the data list
    for i in range(len(dataList)):
        #increment the sum by the value of the index of that data list
        Sum = Sum + int(dataList[i])
    #Divide the sum by the length of the data list to get average
    average = Sum/len(dataList)
    #return this average
    return average

#define a function that will change the list of data into another
#based off of the indexes given
def modifyDataList(dataList, indexes):
    #intilize the new data list
    newDataList = []
    #for the lenght of the indexes that the list will be changed into
    for i in range(len(indexes)):
        #A new pieve of data equals the the index of the indexes of the main
        #data list
        newData = dataList[indexes[i]]
        #append this new data to the new data list
        newDataList.append(newData)
    #return the new data list
    return newDataList

#define a line strip function that takes anything out of each
#index in the data list
def listStrip(dataList, thingToStrip):
    #initialize the new stripped data list
    strippedDataList = []
    #for the lenght of the original data list
    for i in range(len(dataList)):
        #strip the thing to strip for the individual index in the data list
        strippedData = dataList[i].strip(thingToStrip)
        #append this new data to the new data list
        strippedDataList.append(strippedData)
    #return the new list of stripped ata
    return strippedDataList

#define a function that will see if what the user is searching for exits
def findExists(dataList, searchingFor):
    #The thing that is being searched for has not been found
    found = False
    #while this is still not found
    while found == False:
        i = 0
        #loop throuhg the entire data list and see if what is being searched
        #for is in that list
        while i < len(dataList) and found == False:
            #if it is in side the list the searching for has been found
            if dataList[i] == searchingFor:
                found = True
            i = i + 1
        #if searching for is not in the list ask the user to search for some
        #thing else and repeat untill the user enters a valid option
        if found == False:
            searchingFor = input("The data you were looking for does not exsist please seach for somthing else: ")
    #return the valid searching for variable 
    return searchingFor

#define a function that will see if the thing the user is searching for is
#valid, valid being a variable that checks to see if it is valid
def findValidSearch(search, valid):
    #initialize that the search is valid to false 
    isValid = False
    #while the search is still false
    while isValid == False:
        #if the search is invalid as the user to search again
        if search.find(str(valid)) == -1:
            search = input("invalid search -- try again: ")
        else:
            #if the search is valid return the search
            isValid = True
    return search

#a function that retuns the user each type of data in a list once
def listOptions(dataList):
    #initialize a list of each type of data starting with the first
    #in the data list
    newList = [dataList[0]]
    #for the lenght of the data list
    for i in range(len(dataList)):
        #initialize new at true
        new = True
        #for the lenght of the new list if the piece of data is not in the new
        #list add it to the new list
        for j in range(len(newList)):
            if dataList[i] == newList[j]:
                new = False
        #add the new data to the list
        if new == True:
            newList.append(dataList[i])
    return newList

#a function that will sort the data list high to low and will in turn
#sort the indexes of the datalist in the main list in the same order
def sortDataLowToHigh(dataList, indexes):
    #for the lenght of the data list
    for i in range(len(dataList)):
        #for the remain parts of the data list that have not been
        #ordered yet
        for j in range(len(dataList)-1-i):
            #put the remaining highest at the end of the list
            if dataList[j] > dataList[j + 1]:
                dataList[j], dataList[j + 1] = dataList[j + 1], dataList[j]
                #order the list of indexes in the same way
                indexes[j], indexes[j+1] = indexes[j+1], indexes[j]
    #return the newly ordered list of indexes
    return indexes
        
    
#define a functtion that will print all fo the results taking the data
#and list of the indexes
def printResults(indexes, airLines, flightNums, deptTimes, arrTimes, prices):
    #takes the indexes and prints all the results in the correct format
    print("The flights that meet your criteria are: ")
    print(" ")
    print("AIRLINE   FLT#   DEPT   ARR    PRICE")
    print("------------------------------------------")
    #for the length of the indexes
    if len(indexes) == 0:
        print("No flights match this criteria.")
    for i in range(len(indexes)):
        printStatment = ""
        #call alignprint results and the return to a print stament for each
        #type of data
        printStatment = alignPrintResults(airLines, indexes[i], printStatment, 10)
        printStatment = alignPrintResults(flightNums, indexes[i], printStatment, 7)
        printStatment = alignPrintResults(deptTimes, indexes[i], printStatment, 7)
        printStatment = alignPrintResults(arrTimes, indexes[i], printStatment, 7)
        printStatment = alignPrintResults(prices, indexes[i], printStatment, 0)
        #print the final print stametn for each given index in the indexes list
        print(printStatment)
    print(" ")
    return 

#define a functiona that will align the print results to make sure
#everything is even
def alignPrintResults(dataList, index, printStatment, length):
    #add the data in the data list of the given index to the print statment
    printStatment = printStatment + str(dataList[index])
    #for the range of the length of the data subtracted by the total
    #space possible add spaces for each remaining space
    for i in range(length - len(dataList[index])):
            printStatment = printStatment + " "
    #return the print statment
    return printStatment
        
def userChoice(lowRange, highRange):
    #initialize correct choice to flase
    correctChoice = False
    #while the user has not chosen correctly print this list and make them
    #rechoose
    while correctChoice == False:
        print("Please choose one of the following options:")
        print("1 -- Find all flights on a particular airline")
        print("2 -- Find the cheapest flight")
        print("3 -- Find all fights less than a specific price")
        print("4 -- Find the shortest flight")
        print("5 -- Find all flights that depart within a specified range")
        print("6 -- Sort by price or duration based off of airline")
        print("7 -- Find the average price for a specified airline")
        print("8 -- Quit")
        choice = int(input("Choice ==>"))
        #if the user choose correctly set choice to true and move on
        if choice <= highRange and choice >= lowRange:
            correctChoice = True
    #take the users choice as an input
    return choice

#define a function that executes the users choices
def exeChoices(airLines, flightNums, deptTimes, arrTimes, prices):
    #initialze the choice at 0 propting the user to ask for his or her choice
    choice = 0
    #intialize the list of indexes that will be filled by find functions
    indexes = []
    #While the users choice is not quit
    while choice != 8:
        #call the user choice function prompting the user to choose
        choice = userChoice(1,8)
        #if the user choose option one
        if choice == 1:
            #ask the user to search for an airline
            airLineSearch = input("Enter airline to search for: ")
            #Search throught the list of airlines to see if what the user
            #is searching for exists
            searchingFor = findExists(airLines, airLineSearch)
            #call the searching for function returning a list of idexes
            #of the data list that match what the user is looking for
            indexes = findEquivalent(airLines,searchingFor)
        #if the user chooses option 2
        elif choice == 2:
            #Call a function to find the indexes of the smallest price in
            #the prices list
            indexes = findSmallest(prices)
        #if the user chooses option 3
        elif choice == 3:
            #ask the user what the highest price he is willing to pay is
            high = [input("What is the max price you are willing to pay in dollars: ")]
            #remove the dollar sign from the list of prices
            #and high input if user inputs one
            high = listStrip(high, '$')
            high = int(high[0])            
            newPrices = listStrip(prices, '$')
            #find the indexes of all prices that range from 0 to what the
            #user is searching for 
            indexes = findInBetween(newPrices, high, 0)
        #If the user chooses option 4
        elif choice == 4:
            #compute the flight times of each flight
            flightTimes = findFlightTime(deptTimes, arrTimes)
            #returns the index in a list of the flight that has the
            #smallest flight time
            indexes = findSmallest(flightTimes)
        #if the user chooses option 5
        elif choice == 5:
            #Ask the user what the earliest time to search for is
            low = input("Enter the earliest time to search for: ")
            low = findValidSearch(low, ':')
            #do the same fot the latest time
            high = input("Enter the latest time to search for:")
            high = findValidSearch(high, ':')
            #find the amount of minutes from zero
            #that lowest and highest times depart
            #by using the hight and low time and zer0
            low = findFlightTime(['0:00'], [low])
            high = findFlightTime(['0:00'], [high])
            #create a list of zeros the length of departure times
            zeros = []
            for i in range(len(deptTimes)):
                zeros.append('0:00')
            #Find the amount of minutes form time zero that each
            #flight leave
            flightTimes = findFlightTime(zeros, deptTimes)
            #return a list of indexes of flight times that are smaller
            #than return the indexes of the data list which are lower than
            #the hight and higher than the low
            indexes = findInBetween(flightTimes, high[0], low[0])
        #if the user chooses option 6
        elif choice == 6:
            #give the user a list of air lines to choose from
            newList = listOptions(airLines)
            #Ask the user to choose between the results
            print("Choose Between:")
            for i in range(len(newList)):
                print(newList[i])
            airLineSearch = input("Enter a airline to search for: ")
            #Check to see if the air line the user is searching for exists
            airLineSearch = findExists(airLines,airLineSearch)
            #ask the user what he or she would like to sort by
            sortBy = input("Sort by price or flight duration: ")
            #Check if the user input a valid option
            soryBy = findExists(['price','flight duration'],sortBy)
            #find all airlines that match what the user is searching for
            indexes = findEquivalent(airLines, airLineSearch)
            #if the user searched for price
            if sortBy == 'price':
                #change the list of prices to only include the airline the
                #user is searching for
                modifiedData = modifyDataList(prices, indexes)
                #return the newly arranged indexes of the data
                indexes = sortDataLowToHigh(modifiedData, indexes)
            #if the user chooses to search for flight times
            else:
                #find the flight times of all of the data
                flightTimes = findFlightTime(deptTimes, arrTimes)
                #change the list of flight times to only include
                #the airlines the user is searching for
                modifiedData = modifyDataList(flightTimes, indexes)
                #return a list of reorded indexes 
                indexes = sortDataLowToHigh(modifiedData, indexes)
        #if the user chooses option 7
        elif choice == 7:
            #ask the user to choose for an airline
            airLine = input("Enter a airline to search for: ")
            #check to see if what the user is searching for exists
            searchingFor = findExists(airLines, airLine)
            #find the indexes of the euqivalent to what they are searching for
            indexes = findEquivalent(airLines, searchingFor)
            #modify the data list to only include the indexes of what the user
            #is looking for
            modifiedData = modifyDataList(prices, indexes)
            #take the dollar sign off off all the data in the list
            modifiedData = listStrip(modifiedData, '$')
            #Call find average function to find all the data in the list
            average = findAverage(modifiedData)
            #print what the average is 
            print("The average price of", airLine,"flights is $", average)
        #if the users choice is not 6 or 7 print the results
        if choice <= 6 and choice >= 1:
            printResults(indexes, airLines, flightNums, deptTimes, arrTimes, prices)
    #if the user chooses option 7 exit the function        
    print("You have exited")
    #return the list of indexes and choice
    return indexes, choice

def main():
    #calls get file function functions and saves the file
    file = getFile()
    #saves all fo the data into lists
    airLines, flightNums, deptTimes, arrTimes, prices = getData(file)
    #calls exechoices and saves indexes and choice
    indexes, choice = exeChoices(airLines, flightNums, deptTimes, arrTimes, prices)
    return main

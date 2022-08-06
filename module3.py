# CSC200 Module 3 Python Program to outline Selection Sort Algorithm of a list of weekly salaries
# Content derived heavily from https://www.geeksforgeeks.org/selection-sort/
import sys

# My list of salaries I want to output in ascending then descending order
ListOfWeeklySalaries = [500, 300, 700, 400, 600, 550]

# go through each item (index) in the list
for item in range(len(ListOfWeeklySalaries)):

    # this looks for the smallest item in the remaining temporary array
    # basically, we are iterating through an iteration of the items.
    # for example, starting with item(0) 
    # set index(0) equal to item(0)
    # take the entire list again, only start at item(0+1)
    # then starting at item(1) is item(0) greater than item(1)
    # if not, change index(0) to be the same as item(1) 
    # repeat for this list until it ends
    # THEN, go back to the orginal list, and start over, only start at item(1)
    # You are comparing each value against each other value iteratively, constantly moving the higher number to the right 
    lowest_item = item
    # currentitem is essentially the current number in that iteration
    for currentitem in range(item+1, len(ListOfWeeklySalaries)):
        if ListOfWeeklySalaries[lowest_item] > ListOfWeeklySalaries[currentitem]:
            lowest_item = currentitem
    
    ListOfWeeklySalaries[item], ListOfWeeklySalaries[lowest_item] = ListOfWeeklySalaries[lowest_item], ListOfWeeklySalaries[item]

print ("List of Weekly Salaries in ascending order:")
for item in range(len(ListOfWeeklySalaries)):
    print ("%d" %ListOfWeeklySalaries[item], end=" ")

print ()
for item in range(len(ListOfWeeklySalaries)):
    #the only difference in this is that it is evaluating if currentitem is LESS THAN instead of GREATER THAN
    lowest_item = item
    for currentitem in range(item+1, len(ListOfWeeklySalaries)):
        if ListOfWeeklySalaries[lowest_item] < ListOfWeeklySalaries[currentitem]:
            lowest_item = currentitem
    
    ListOfWeeklySalaries[item], ListOfWeeklySalaries[lowest_item] = ListOfWeeklySalaries[lowest_item], ListOfWeeklySalaries[item]

print ("List of Weekly Salaries in descending order:")
for item in range(len(ListOfWeeklySalaries)):
    print ("%d" %ListOfWeeklySalaries[item], end=" ")

# On my honor:
#
# - I have not discussed the Python code in my program with
# anyone other than my instructor or the teaching assistants
# assigned to this course.
#
# - I have not used Python code obtained from another student,
# or any other unauthorized source, either modified or
# unmodified.
#
# - If any Python code or documentation used in my program
# was obtained from another source, such as a text book or
# course notes, that has been clearly noted with a proper
# citation in the comments of my program.

import matplotlib.pyplot as plot
import matplotlib.patches as patches
from scipy import math
import os
import subprocess as sub

devMode = False
newFileCounter = 0

#writes the py outline that the user will be able to edit
def writePy():
    global newFileCounter
    fileName  = "pythonTemp" + str(newFileCounter) + ".py"
    command = "touch " + fileName
    os.system(command)

    with open(fileName, "w") as newFile:
        newFile.write("import matplotlib.pyplot as plot\n")
        newFile.write("import matplotlib.patches as patches\n")
        newFile.write("def firstFunction():\n")
        newFile.write("\tfig = plot.figure()\n")
        newFile.write("\tsub = fig.add_subplot(111, aspect= 'equal')\n")
        newFile.write("\ttri = patches.Polygon([[0,0], [0,5], [5,0]], closed=True,fill=False)\n")
        newFile.write("\tsub.add_patch(tri)\n")
        newFile.write("\tplot.ylim(0, 10)\n")
        newFile.write("\tplot.xlim(0, 10)\n")
        newFile.write("\tsub.add_artist(tri)\n")
        newFile.write("\tplot.show()\n")
        newFile.write("firstFunction()\n")
    newFileCounter+=1
    return fileName
    
# Introduction info about the Calculator
# Prompts the user to pick a shape
def parser():
    print("Welcome to the Geometry Calculator.")
    print("Would you like to enable developer mode? (Y/N)")
    answer = input('>')
    if answer == "Y":
        developerMode()
    while True:
        print("Select a shape: rectangle, triangle, circle, rhombus")
        shape = input('>')
        if shape == "rectangle":
            print("What is the length: ")
            inp = input('>')
            print("What is the height: ")
            inp2 = input('>')
            rectangle(int(inp), int(inp2))
        elif shape == "dev":
            developerMode()
        elif shape == "triangle":
            triangle()
        elif shape == "circle":
            print("what is your radius")
            r = int(input('>'))
            circle(r)
        elif shape == "rhombus":
            rhombus()
        else:
            print("Shape not available")
        print("Do you want to exit the calculator? (Y/N)")
        v = input('>')
        if v == 'Y':
            break

#Asks for the needed measurements
#Print the area
#Call graph
#prints the perimeter and area as well as plots the rectangle with the appropriate length and height
def rectangle(length, height):
    area = length*height
    print("Area: " + str(area))
    fig = plot.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    ax1.add_patch(patches.Rectangle((3, 3), length, height))
    plot.ylim(0, height + 5)
    plot.xlim(0, length + 5)
    plot.show()

#Asks for the needed measurements
#Assumed Right Triangle
def triangle():
    print("Please enter the base length: ")
    b = int(input(">")) 
    print("Please enter the height: ")  
    h = int(input(">")) 
    
    fig = plot.figure()
    area = (1/2)* b * h
    print("Area: " + str(area))
    p1 = (0, h)
    p2 = (0, 0)
    p3 = (b, 0)
    tri = patches.Polygon([p1,p2,p3], closed=True,fill=True)
    sub = fig.add_subplot(111, aspect= 'equal')
    sub.add_patch(tri)
    plot.ylim(0, h + 5)
    plot.xlim(0, b+ 5)
    sub.add_artist(tri)
    plot.show()

#Asks for the needed measurements
#Print the area
#Call graph
#plots the circle based on the radius
def circle(radius):
    area = 3.14*(int(radius)**2)
    print("Area: " + str(area))
    
    fig = plot.figure()
    circle1 = patches.Circle((int(radius), int(radius)), radius, color = 'r')
    sub = fig.add_subplot(111, aspect= 'equal')
    sub.add_patch(circle1)
    plot.ylim(0, int(radius)*2)
    plot.xlim(0, int(radius)*2)
    sub.add_artist(circle1)
    plot.show()

#Asks for the needed measurements
#Print the area
#Call graph  
def rhombus():
    fig = plot.figure()
    p = int(input("Please enter the first diagonal length: "))
    q = int(input("Please enter the second diagonal length: "))
    area = (p*q) / 2
    print("Area: " + str(area))
    p1 = (0, p/2)
    p2 = (q/2, p)
    p3 = (q, p/2)
    p4 = (q/2, 0)
    tri = patches.Polygon([p1,p2,p3,p4], closed=True,fill=True)
    sub = fig.add_subplot(111, aspect= 'equal')
    sub.add_patch(tri)
    plot.ylim(0, p + 5)
    plot.xlim(0, q + 5)
    sub.add_artist(tri)
    plot.show()

#Checks if the user is finished editing
#Continues prompting the question until the Yes answer is returned
def finishedEdit():
    while (True):
        inp = input("Are you finished editing? (Y/N)")
        if (inp == "Y"):
            break
        elif (inp != "N"):
            print("That is not a valid answer")

#Provides information about python 
#and code used while developing the calculator 
#Is called right before the area and graph is printed
#for each shape so should provide information about the code that follows
def developerMode():
    fileName = writePy()
    sub.call(['python.exe', fileName])
    os.system("start notepad.exe pythonTemp.py") 
    finishedEdit()
    while(True):
        try:
            sub.check_call(['python.exe', fileName])
            break
        except sub.CalledProcessError:
            print("There was an error in your code, please try again.")
            os.system("start notepad.exe pythonTemp.py")
            finishedEdit()
        

parser()

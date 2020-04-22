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

newFileCounter = 0
fileList = []

#writes the py outline that the user will be able to edit
def writePy():
    global newFileCounter
    fileName  = "pythonTemp" + str(newFileCounter) + ".py"
    command = "touch " + fileName
    os.system(command)
    with open(fileName, "w") as newFile:
        newFile.write("#Keep in mind, any line with a \"#\" leading it is a comment which means it does not impact the code.\n\n")
        newFile.write("#These are import statements which import modules and allow the python code to access more functions\nimport sys\n")
        newFile.write("import matplotlib.pyplot as plot\t#pyplot provides plot for images, run these functions using \"plot\"\n")
        newFile.write("import matplotlib.patches as patches\t#2D images with color, run these functions with patches\n\n")
        newFile.write("#\"def\" is a keyword to declare a function in python. \n")
        newFile.write("#\"firstFunction\" is the name of the function and \"arg1\" is the parameter passed into the function.\n") 
        newFile.write("def firstFunction(arg1):\n\n\t#Creates a plot to hold created shape\n\tfig = plot.figure()\n")
        newFile.write("\tsub = fig.add_subplot(111, aspect= 'equal')\n\n")
        newFile.write("\t#Creates a new shape using Polygon function and stores in variable \"shape\". Try out others at https://matplotlib.org/api/patches_api.html\n")
        newFile.write("\tshape = patches.Polygon([[0,0], [0,arg1], [arg1,0]], closed=True,fill=True,color ='b', )\n\n")
        newFile.write("\t#Adds shape to the plot\n\tsub.add_patch(shape)\n\n")
        newFile.write("\t#The following lines sets the y and x axis limits for the pyplot.These values can be adjusted to change the size of your plot\n")
        newFile.write("\tplot.ylim(0, 10)\n\tplot.xlim(0, 10)\n\n")
        newFile.write("\t#This line displays the pyplot, do not remove this line. \n\tplot.show()\n\n")
        newFile.write("#Below calls the function using the function name \"firstFunction\". Remember if you change the function name change it here too!\n")
        newFile.write("#The function is called with one argument. If you change the number of parameters the function call changes as well.")
        newFile.write("\n#\tExample of function call w/ two param: firstfunction(sys.argv[1], sys.argv[2])\n\n")
        newFile.write("firstFunction(sys.argv[1])\n")
    newFileCounter+=1
    return fileName
    
# Introduction info about the Calculator
# Prompts the user to pick a shape
def parser():

    global fileList
    print("Welcome to the Geometry Calculator.")
    
    print("CALC -> Would you like to enable developer mode? (Y/N)")
    answer = input('CALC -> ')
    if answer == "Y":
        developerMode()
    while True:
        print("CALC -> Select a shape: rectangle, triangle, circle, rhombus:")
        shape = input('CALC -> ')
        if shape == "rectangle":
            rectangle()
        elif shape == "dev":
            developerMode()
        elif shape == "myFiles":
            for i in fileList:
                print("CALC -> " + i)
        elif shape == "triangle":
            triangle()
        elif shape == "circle":
            print("CALC -> Enter the radius: ")
            r = int(input('CALC -> '))
            circle(r)
        elif shape == "rhombus":
            rhombus()
        else:
            calcDev(shape)

        print("CALC -> Do you want to exit the calculator? (Y/N)")
        v = input('CALC -> ')
        if v == 'Y':
            break

#Asks for the needed measurements
#Print the area
#Call graph
#prints the perimeter and area as well as plots the rectangle with the appropriate length and height
def rectangle():
    print("CALC -> Enter the length: ")
    length = int(input('CALC -> '))
    print("CALC -> Enter the height: ")
    height = int(input('CALC -> '))
    perim = 2 * length + 2 * height
    area = length*height
    print("CALC -> Perimeter = 2 * (length + width) = %.3f" %perim)
    print("CALC -> Area = length * width = %.3f" %area)
    fig = plot.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    ax1.add_patch(patches.Rectangle((3, 3), length, height))
    plot.ylim(0, height + 5)
    plot.xlim(0, length + 5)
    plot.show()

#Asks for the needed measurements
#Assumed Right Triangle
def triangle():
    print("CALC -> Please enter the base length: ")
    b = int(input("CALC -> ")) 
    print("CALC -> Please enter the height: ")  
    h = int(input("CALC -> ")) 
    
    fig = plot.figure()
    area = (1/2)* b * h
    print("CALC -> Area: " + str(area))
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
    area = math.pi*(int(radius)**2)
    perim = 2 * int(radius) * math.pi
    print("CALC -> Area = pi * radius * radius = %.3f" %area)
    print("CALC -> Circumference = 2 * pi * radius = %.3f" %perim)
    
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
    p = int(input("CALC -> Please enter the first diagonal length: "))
    q = int(input("CALC -> Please enter the second diagonal length: "))
    area = (p*q) / 2
    print("CALC -> Area: " + str(area))
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

#Calculates the distance between two points
def pointDist(p1, p2):
    return ((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2)**.5
    
#Calls files that were created in developer mode
def calcDev(fileName):
    global fileList
    fileInfo = fileName.split()
    inList = False
    for files in fileList:
        if (fileInfo[0] == files):
            inList =True;

    if (not inList):
        print("CALC -> That input is not available")
        return
    command = ['python']
    command.extend(fileInfo)
    try:
        sub.check_call(command)
        
    except sub.CalledProcessError:
        print("CALC -> That input is not available")


#Checks if they are finished
def finishedDev():
    while (True):
        inp = input("DEV -> Would you like to continue editing your script or are you finished in Dev mode? (quit/cont): ")
        if (inp == "quit"):
            return True
        elif (inp == "cont"):
            return False        
        else:
            print("DEV -> That is not a valid answer")

#Adds to global list
def addToList(fileName):
    global fileList
    inList = False
    for i in fileList:
        if (fileName == i):
            inList = True
    if (not inList):
        fileList.append(fileName)

#Removes from global list
def removeFromList(fileName):
    global fileList
    try:
        fileList.remove(fileName)
    except ValueError:
        pass


#Gives the user to develop their own functions through python scripts
#Provides the user an outline and walks them through the script and lets them play around
#with the code to make their own calculator functions
def developerMode():
    
    #filename is the name of the written outline which is written in writePy() 
    fileName = writePy()

    commandArr = ['python', fileName, '1']
    #runs the outline code to show the user what the code originially displays
    print("DEV -> This image is what the current code script plots, have fun developing!")
    sub.call(commandArr)

    #Opens the outline code in the notepad and allows the user to edit the code
    print("DEV -> Please close and save file when you are finished editing")
    sub.run(['open', fileName], check = True)

    # if user saved file under a new name, prompts user for name and saves it 
    newFile = input("DEV -> If you have saved the file under a new name please enter here, otherwise press ENTER: ")
    if (len(newFile) > 0):
        fileName = newFile
    
    #gets user to input arguments and adds them to the command list
    paramNum = int(input("DEV -> How many arguments does you function have? "))
    commandArr = ['python', fileName]
    if (paramNum  > 0):
        params = input("DEV -> Please enter your function arguments seperated by spaces: ")
        params = params.split()
        commandArr.extend(params)

    
    #Loops through the developing process until the user wants to exit developer mode
    while(True):

        try:
            print("DEV -> Your code will now run and check for errors. If it is error free your graph will be displayed!")
            print("DEV -> If there are any errors in your code, they will be printed below and your plot will not display")
            sub.check_call(commandArr)
            addToList(fileName)

            if (finishedDev()):
                break

        except sub.CalledProcessError:
            
            removeFromList(fileName)
            print("\nDEV -> There was an error in your code, please try again.")
            #prompts user if they would like to fix their code
            inp = input("DEV -> Would you like to try to fix your code? (Y/N):  ")
            #If no then prompts user if they would like to stay in dev mode
            if (inp == "N" and finishedDev()):
                break
            
        #Opens the outline code in the notepad and allows the user to edit the code
        print("DEV -> Please save file before you are finished editing and the code is run")
        sub.run(['open', fileName], check=True)

        #If user saved file under a new name, prompts user for name and saves it 
        newFile = input("DEV -> If you have saved the file under a new name please enter here, otherwise press ENTER: ")
        if (len(newFile) > 0):
            fileName = newFile
        
        #gets user to input arguments and adds them to the command list
        paramNum = int(input("DEV -> How many arguments does you function have? "))
        commandArr = ['python', fileName]
        if (paramNum  > 0):
            params = input("DEV -> Please enter your function arguments seperated by spaces: ")
            params = params.split()
            commandArr.extend(params)
        


parser()

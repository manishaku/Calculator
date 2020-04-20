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

mode = False

# Introduction info about the Calculator
# Prompts the user to pick a shape
def parser():
    print("Welcome to the Geometry Calculator.")
    print("Would you like to enable developer mode? (Y/N)")
    answer = input('>')
    if answer == "Y":
        mode = True
    while True:
        print("Select a shape: rectangle, triangle, circle, rhombus")
        shape = input('>')
        if shape == "rectangle":
            l = int(input("what is the length"))
            h = int(input("what is the height"))
            rectangle(l, h)
        elif shape == "triangle":
            triangle()
        elif shape == "circle":
            circle()
        elif shape == "rhombus":
            rhombus()
        else:
            print("Shape not available")

#Asks for the needed measurements
#Checks if mode == True and calls developerMode("rectangle")
#Print the area
#Call graph
def rectangle(length, height):
    perim = 2 * length + 2 * height
    area = length*height
    print(perim)
    print(area)
    fig = plot.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    ax1.add_patch(
        patches.Rectangle((0, 0), length, height))
    plot.ylim(0, 10)
    plot.xlim(0, 10)
    plot.show()
    

    


#Asks for the needed measurements
#Checks if mode == True and calls developerMode("triangle")
#Print the area
#Call graph 
def triangle():
    pass

#Asks for the needed measurements
#Checks if mode == True and calls developerMode("circle")
#Print the area
#Call graph   
def circle():
    pass

#Asks for the needed measurements
#Checks if mode == True and calls developerMode("rhombus")
#Print the area
#Call graph  
def rhombus():
    pass

#Gets a list of information such as info = ["rectangle", 5, 8]   
#or info = ["circle", 5]   
#Uses the information to print a graph of the shape 
def graph(info):
    pass

#Provides information about python 
#and code used while developing the calculator 
#Is called right before the area and graph is printed
#for each shape so should provide information about the code that follows
def developerMode(shape):
    pass


parser()

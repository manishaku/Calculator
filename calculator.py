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
            inp = input("What is the length and height seperated by space: ")
            inp = inp.split()
            
            rectangle(int(inp[0]), int(inp[1]))
        elif shape == "triangle":
            h = int(input("what is the height"))
            b = int(input("what is the base length"))
            e = int(input("what is one other edge length"))
            triangle(h, b,e)

        elif shape == "circle":
            r = int(input("what is your radius"))
            circle(r)
        elif shape == "rhombus":
            rhombus()

        elif shape == "quit": #Added a quit feature to get out of the loop
            break
        else:
            print("Shape not available")

#Asks for the needed measurements
#Checks if mode == True and calls developerMode("rectangle")
#Print the area
#Call graph
#prints the perimeter and area as well as plots the rectangle with the appropriate length and height
def rectangle(length, height):
    perim = 2 * length + 2 * height
    area = length*height
    print(perim)
    print(area)
    fig = plot.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    ax1.add_patch(
        patches.Rectangle((3, 3), length, height))
    plot.ylim(0, 10)
    plot.xlim(0, 10)
    plot.show()
    


#Asks for the needed measurements
#Checks if mode == True and calls developerMode("triangle")
#
#Prints a triangle but is hardcoded currently, not sure of good parameters
#as there are so many ways triangles can be formated in geomtry 
def triangle(height, base, edge):
    fig = plot.figure()
    
    tri = patches.Polygon([[0,0],[0, 5],[5, 0]], closed=True,fill=True)
    sub = fig.add_subplot(111, aspect= 'equal')
    sub.add_patch(tri)
    plot.ylim(0, 10)
    plot.xlim(0, 10)
    sub.add_artist(tri)
    plot.show()

#Asks for the needed measurements
#Checks if mode == True and calls developerMode("circle")
#Print the area
#Call graph
#plots the circle based on the radius
def circle(radius):
    fig = plot.figure()
    circle1 = patches.Circle((5, 5), radius, color = 'r')
    sub = fig.add_subplot(111, aspect= 'equal')
    sub.add_patch(circle1)
    plot.ylim(0, 10)
    plot.xlim(0, 10)
    sub.add_artist(circle1)
    plot.show()


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

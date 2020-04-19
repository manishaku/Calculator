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
            rectangle()
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
def rectangle():
    pass

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

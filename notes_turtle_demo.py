# Python's turtle graphics simulates MIT professor Semour Papert's 1960's robotic turtle 
#   students would enter computer commands to move the turtle

# first step is to import the turtle module
#   the module uses tkinter for the underlying graphics, so the python version has to support tk

import turtle   #  using this type of import, all of the turtle methods must be prefaced with turtle dot (e.g. turtle.method)
# t = turtle.Turtle()  # this is a shortcut method, by assigning turtle to a variable, you can now use t instead of turtle for all of the methods
    # e.g. t.right(90)

from turtle import* # this allows the methods to be used without a preface.  This can get confusing if there is more than
    # one module open in a single program.

# turtle.showturtle()  # use this if in interactive mode, to display the turtle.
# By default, the turtle is facing East (to the right) which is 0 degrees on the coordinate plane, at "Home" (0,0)
turtle.shape('turtle')  # the dot is the "dot operator"

# draw a square:
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# change pen colors and move by setting the heading
turtle.pencolor('red')
turtle.setheading(0)
turtle.forward(100)
turtle.setheading(45)
turtle.forward(100)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(135)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(235)
turtle.forward(100)

# change pen color and use pen up and pen down
turtle.pencolor('blue')
turtle.setheading(0)
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)

# draw a circle and change the pen color and pen size
turtle.pencolor('yellow')
turtle.pensize(4)
turtle.circle(75)

# change the background color
turtle.bgcolor('gray')

# clear the screen and reset turtle
turtle.reset()

# move the turtle to a specific location
turtle.goto(0,100)
turtle.goto(-100,0)
turtle.goto(0,0)

# display text in the graphics window
turtle.write("Hello Steve!")
turtle.clear

# filling shapes
turtle.hideturtle()
turtle.fillcolor('magenta')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# end fill will fill even partially complete poygons by creating a boarder between two open points 
# (unless they are both on a single line, then no fill occurs)
turtle.home()
turtle.begin_fill()
turtle.fd(100)
turtle.rt(45)
turtle.fd(200)
turtle.end_fill()


# Create multiple turtles, assigned to different variables
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape('turtle')
t2.shape('turtle')
t1.fd(100)
t2.fd(200)
t1.rt(45)
t2.rt(90)
t1.fd(300)
t2.fd(200)

# Determine turtles location and redirect if too far away
if turtle.xcor() > 249 or turtle.ycor() > 349:
    turtle.goto(0, 0)

# Determine whether the pen is down, then raise or lower it
turtle.isdown # returns True if the pen is down

if turtle.isdown():
    turtle.penup()

if not(turtle.isdown()):
    turtle.pendown()

# Determining Whether the Turtle is Visible, then show or hide it

if turtle.isvisible():
    turtle.hideturtle()

if not(turtle.isvisible()):
    turtle.showturtle()

# Determining the Current Colors and changing them
# When you execute turtle.pencolor(), turtle.fillcolor(), or turtle.bgcolor() functions without an argument, it returns the current color.

if turtle.pencolor == 'red':
    turtle.pencolor('blue')

if turtle.fillcolor == 'blue':
    turtle.fillcolor('white')

if turtle.bgcolor == 'white':
    turtle.bgcolor('gray')

# Determining and changing the pen size

if turtle.pensize() < 3:
    turtle.pensize(3)

# Determine the turtle's animation speed and change it

if turtle.speed() > 0:
    turtle.speed(0)

if turtle.speed() == 0:
    turtle.pencolor('red')
elif turtle.speed() > 5:
    turtle.pencolor('blue')
else:
    turtle.pencolor('green')



turtle.done()

#**************************************************************
# build the Orion star chart
# This program draws the stars of the Orion constellation,
# the names of the stars, and the constellation lines.
#  This program file is from Gaddis

turtle.clear()

# Set the window size.
turtle.setup(500, 600)

# Setup the turtle.
turtle.penup()
turtle.hideturtle()

# Create named constants for the star coordinates.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Draw the stars.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)     # Left shoulder
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)   # Right shoulder
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)     # Left belt star
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) # Middle belt star
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)   # Right belt star
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)             # Left knee
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)           # Right knee
turtle.dot()

# Display the star names
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)     # Left shoulder
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)   # Right shoulder
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)     # Left belt star
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) # Middle belt star
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)   # Right belt star
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)             # Left knee
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)           # Right knee
turtle.write('Rigel')

# Draw a line from the left shoulder to left belt star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Draw a line from the right shoulder to right belt star
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Draw a line from the left belt star to middle belt star
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Draw a line from the middle belt star to right belt star
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Draw a line from the left belt star to left knee
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Draw a line from the right belt star to right knee
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

# Keep the window open. (Not necessary with IDLE.)
turtle.done()
#***********************************************************

#***********************************************************

# Hit the Target Game (Gaddis)
import turtle

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
else:
        print('You missed the target.')  # Not a great program, window doesn't stay open, cannot see the action from your choices.
#**************************************************

# Turtle methods include:

# Turtle motion
'''Move and draw
    forward(amount) | fd() which moves the turtle forward by the specified amount (in pixels)
    backward(amount) | bk() | back()  which move the turtle backward by the specified amount (in pixels)
    right(angle) | rt()  turns the turtle clockwise by the given degrees
    left(angle) | lt()    turns the turtle counterclockwise by the given degrees
    goto(0.00, 0.00) | setpos() | setposition()  moves the turtle to the position x,y
    setx()
    sety()
    setheading(angle) | seth()  set's the turtle's heading at a specific angle
    home()  returns the turtle to (0,0)
    circle(radius, extent=None, steps=None) radius is a number, extent is a number or None, steps is an integer or None
    dot(size,color)  returns a solid circle and leaves a dot at the current position
    stamp() leaves an icon at the location before executing the next step, returns an assigned number
    clearstamp() the argument is the number of the stamp you want to clear
    clearstamps() 
    undo()  Erases the previous action, useful when in interactive mode.  The number of "undos" that can be performed is based on what happens to be in 
            the buffer.  The special commands undobufferentries() will return the available number, and setundobuffer() allows you to designate how many
            entries will be kept until the buffer empties.
    speed() The argument is a value 0-10, 0 means turtle will do all comands instantaneously, 1 is the slowest
            If you don't place a value, the method returns the turtle's current speed.

position() | pos()  returns the current position by coordinates, used in interactive mode
    towards()
    xcor(0.00)
    ycor(0.00)
    heading()  returns the current heading, used in interactive mode
    distance()

Setting and measurement
    degrees()
    radians()'''

'''Pen control
Drawing state
    pendown() | pd() | down() puts the turtle's pen down
    penup() | pu() | up() picks up the turtle's pen (moves without drawing)
    pensize() | width() makes the drawing line larger in multiples pensize(5) is 5x bigger
    pen()  can be used to set multiple parameters at once
        pen(pencolor='red', fillcolor='blue', pensize=5, speed=7)
    isdown()
Color control
    color(colorname) changes both the pen color and the fill color, can use arguments to get two different colors color(pencolor,fillcolor) 
    pencolor() changes the color of the turtle's pen, color strings are used in the argument
    fillcolor(colorname)  changes the color the turtle will use to fill a polygon
Filling
    filling()
    begin_fill()  remember the starting point for a polygon that will be filled
    end_fill()   closes and fills the polygon with the current fill color
More drawing control
    reset()
    clear()     erases all of the drawings on the screen, turtle position and attributes, and background stays the same.
    write()  this method is used to dispay text in the window, it will display starting from the turtle's location and extend to the left.
            the argument is a string'''

'''Turtle state
Visibility
    showturtle() | st()  shows the turtle again after it has been hidden
    hideturtle() | ht()  hides the turtle icon, doesn't change how the lines are drawn
    isvisible()
Appearance
    shape()   (number,number), to resize by pixel, ('arrow'), ('circle'), ('square'), ('triangle'), ('turtle'), ('classic') 
    resizemode()
    shapesize() | turtlesize()
    shearfactor()
    settiltangle()
    tiltangle()
    tilt()
    shapetransform()
    get_shapepoly()'''

'''Using events
    onclick()
    onrelease()
    ondrag()'''
    
'''Special Turtle methods
    begin_poly()
    end_poly()
    get_poly()
    clone()
    getturtle() | getpen()
    getscreen()  opens a drawing window
    setundobuffer()
    undobufferentries()'''

'''Methods of TurtleScreen/Screen
Window control
    bgcolor() sets the background color
    bgpic()
    clear() erases all of the drawings on the screen, doesn't reset turtle's color, position, or variable, doesn't change background color
    clearscreen() resets the background color, pen color, and position to original/beginning state
    resetscreen() erases all of the drawings on the screen, leaves the background color the same, sets the turtle in original position, color black
    screensize()
    setworldcoordinates()
    done() keeps the window open if working in any ide besides IDLE
Animation control
    delay()
    tracer()
    update()
Using screen events
    listen()
    onkey() | onkeyrelease()
    onkeypress()
    onclick() | onscreenclick()
    ontimer()
    mainloop() | done()
Settings and special methods
    mode()
    colormode()
    getcanvas()
    getshapes()
    register_shape() | addshape()
    turtles()
    window_height()
    window_width()
Input methods
    textinput()
    numinput()
    Methods specific to Screen
    bye()
    exitonclick()
    setup()  sets the window size in pixels, the argument is width, height
    title()
    Turtle() creates and returns a new turtle object '''

 References:
#
# Gaddis, T. (2018). Starting out with Python (4th Ed) New York, NY: Pearson Educational.  pp 1-74
#
# Geeksforgeeks.com (2022, 16 Feb). Python Programming Language.
#   https://www.geeksforgeeks.org/python-programming-language/ 
#
# Silaparasetty, N. (2020, 26 Feb). The Beginner's Guide to Python Turtle. From RealPython.com
#   https://realpython.com/beginners-guide-python-turtle/

# turtle module 
# it is a built-in Python graphics library used to draw shapes, patterns, and pictures by controlling a virtual pen (called a turtle) on the screen.


#---Square------
import turtle
t=turtle.Turtle()
for i in range(4):    # Square has 4 sides, After 4 repetitions, the square is complete.
    t.forward(100)    # forward or backwoed used for draws each side (100 pixels long) 
    t.left(90)        # left or right used for turns 90° after each side
turtle.done


#----Rectanle----
import turtle
t=turtle.Turtle()
for i in range(2):    # repeats the pattern twice to complete all 4 sides 
    t.forward(100)    # forward or backwoed used for draws each side (100 pixels long)
    t.left(90)        # left or right used for turns 90° after each side
    t.forward(50)
    t.left(90)
turtle.done


#----circle------
import turtle
t=turtle.Turtle()      
t.circle(50)          # Draws a circle with a radius of 50 pixels.


#----star-------
import turtle
t=turtle.Turtle()
for i in range(5):    #repeats 5 times.
    t.backward(100)   #forward or backwoed used for draws each side (100 pixels long)
    t.left(144)       #left or right turns the turtle by 144°, creating the star shape.
turtle.done


t.color(red)         #used for courser color

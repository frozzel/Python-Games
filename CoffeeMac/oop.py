from turtle import Turtle, Screen

timmy = Turtle()    # Create a new turtle object
timmy.shape("turtle")    # Change the shape of the turtle
timmy.color("blue")    # Change the color of the turtle
timmy.forward(100)    # Move the turtle forward by 100 units

my_screen = Screen()    # Create a new screen object    
# print(my_screen.canvheight)    # Print the height of the screen

my_screen.exitonclick()    # Exit the screen on click

from turtle import *

#we want to paint a house

#steo 1: draw a square
speed(30)
width(7)
color("black")
forward (200)
left(90)

forward(200)
left(90)

forward (200)
left(90)

forward (200)
left(90)
#end of square

#drawing a door

forward(70)
color ("brown")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("black")

left(30)
forward(85)

penup()
goto(50, 110)
pendown()

color("brown")    #windows
forward(40)
right(90)
forward(40)

right(90)
forward(50)

right(90)
forward(40)
right(90)
forward(25)
right(90)
forward(40)
right(90)
forward(25)
right(90)
forward(20)
right(90)
forward(50)


penup()
goto(190, 70)
pendown()

right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(25)
right(90)
forward(40)

color("brown")
penup()
goto(125, 0)
pendown()

right(90)
forward(75)

color("yellow")
left(90)
forward(10)

color("yellow")
penup()
goto(180, 0)
pendown()
forward(185)

exitonclick()
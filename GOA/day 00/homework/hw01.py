from turtle import *
#we want to paint a hous

#step 1:draw a square
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#end of square

#drawing a door  

speed(30)
forward(70)
left(90)
forward(120) #heigh of the door
right(90)
forward(60)
right(90)
forward(120)

color("red")
penup()
goto(200,200)
pendown()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(30,140)
pendown()

begin_fill
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
exitonclick()
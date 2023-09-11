from turtle import *


#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#End of square

#Drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(90)      #height of the door
right(90)
forward(60)
right(90)
forward(90)
end_fill()

#Pengoto
penup()
goto(200, 200)
pendown()

#Roof
color("Red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window 1
penup()
goto(30, 125)
pendown()
color("brown")
begin_fill()
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()

#window 2
penup()
goto(130, 125)
pendown()
color("brown")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()




exitonclick()
'''
Some turtle functions you can use to make your shapes


forward(<distance>) - This function takes a positive or negative number and
will move the turtle forward.

back(<distance>) - This function takes a positive or negative numbers and
it will move the turtle back.

right(<angle>) - This function takes a number that represents
angle in degrees. It will turn the turtle to  its right

left(<angle>) - This functions takes an number that represents
 an angle in degrees. It will turn the turtle to its left.

pencolor(<color>) - This functions takes a string that represents a color. The
turtle's pen will draw in that color. The possible color values can be found
at https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

penup() - This function takes no parameters. When called it will
lift the turtle's pen up, the turtle will not draw when moved.

pendown() - This function takes no parameters. When called it will put the
turtle's pen down. It will draw when moved.

speed(<number>) - This function takes a number. It determines how fast the
turtle moves around the screen. Strangely enough if you want it to go as
fast as possible you have to pass it 0 as a parameter.

goto(<x>, <y>) - This function takes two numbers, a position along the x-axis
and a position along the y-axis. It will move the turtle to that position.

fillcolor(<color>) - This function takes a string that represents a color. The
color will be used to fill shape the turtle has made. In order to get the turtle
to fill the shape you have to use the begin_fill() function before the turtle
starts drawing the shape and the end_fill() function after it finishes for the
shape to be filled in.

begin_fill() - This function takes no parameters. It is put before the turtle
draws a shape that you want filled in.

end_fill() - This function takes no parameters. It is put after the turtle has
finished drawing a shape that you want filled in.

dot(<size>, <color>) - This function takes two parameters. The first is a
positive number that represents the diameter of the dot to be drawn by the
turtle. The second is a string that represents the color the dot should be.


BONUS:

circle(<radius>, <extent>, <steps>) - This function takes three parameters.
However you only have to put in the first one. The <radius> parameter is the
necessary parameter, it is a number that represents the radius of the circle.
The <extent> is optional. It represents an angle saying how much of the circle
should be drawn, if you don't put in anything for <extent> it will draw the whole
circle. If you put in 180, it will draw a half circle. The third parameter
<steps> is a number that represents how many steps the turtle should take to
draw the circle. Try setting <steps> as 5 to see what happens.


'''



from turtle import *

penup()
right(90)
forward(200)
left(90)

def square(color1, color2, color3, color4, side_length):
	pendown()
	pencolor(color1)
	forward(side_length)
	left(90)
	pencolor(color2)
	forward(side_length)
	left(90)
	pencolor(color3)
	forward(side_length)
	left(90)
	pencolor(color4)
	forward(side_length)
	left(90)
	
	penup()
	left(90)
	forward(120)
	right(90)
	
square("red", "coral", "lavender", "LemonChiffon2", 100)

square("misty rose", "medium sea green", "medium violet red", "NavajoWhite3", 100)

square("peru", "olive drab", "pale violet red", "peach puff", 100)


penup()
goto(200,200)
pencolor("DarkSalmon")


def triangle(side, color):
		pendown()
		pencolor(color)
		for i in range(3):
			forward(side)
			right(120)
		penup()
		forward(side + 20)
		
triangle(120, "thistle")

triangle(120, "tomato2")

triangle(120, "SeaGreen4")

penup()
goto(200, 0)

def polygon(n_sides, side_length, color):
	pencolor(color)
	for i in range(70):	
		pendown()
		for i in range(n_sides):
			speed(0)
			forward(side_length)
			right(360/n_sides)
		penup()
		forward(5)
	right(90)
	forward(50)
	right(90)
	forward(350)
	right(180)
		
polygon(8, 25, "orchid")

polygon(5, 40, "palevioletred2")

polygon(6, 35, "navy")

polygon(12, 20, "MintyRose3")


done()
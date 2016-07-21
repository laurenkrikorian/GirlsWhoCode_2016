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

pendown()
side_length = "20"
side_length = int(side_length)
print(side_length)

#Square
for i in range(4):
	speed(10)
	forward(side_length)
	right(90)
	
penup()
forward(200)

#Circle
pendown()
for i in range(90): 
	speed(0)
	forward(4)
	right(4)

penup()
left(90)
forward(100)

#Triangle
pendown()
for i in range(3):
	forward (100)
	right(120)
	
penup()
left(90)
forward(400)
left(90)
forward(500)
left(90)

def square(color1, color2, color3, color4, color5):
	pendown()
	pencolor(color1)
	forward(80)
	left(90)
	pencolor(color2)
	forward(80)
	left(90)
	pencolor(color3)
	forward(80)
	left(90)
	pencolor(color4)
	forward(80)
	left(90)
	fillcolor(color5)
	
	penup()
	left(90)
	forward(120)
	right(90)
	
square("red", "coral", "lavender", "LemonChiffon2", "salmon4")

square("misty rose", "medium sea green", "medium violet red", "NavajoWhite3", "seashell2")

square("peru", "olive drab", "pale violet red", "peach puff", "snow4")


done()
	


	
 
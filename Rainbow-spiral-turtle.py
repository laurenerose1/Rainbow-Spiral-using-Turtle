###import turtle
import turtle 
###set up turtle and the screen
t = turtle.Turtle()
s = turtle.Screen()
###prep colors
colors = ['pink', 'purple', 'lightblue', 'darkgreen', 'orange', 'yellow'] 
s.bgcolor('black') 
##set speed
t.speed('fastest')
t.hideturtle()

###get loop ready to go forward and reverse
while True:
  for x in range(200): 
    t.pencolor(colors[x%len(colors)]) 
    t.width(x/100 + 1)
    t.forward(x) 
    t.left(59)
  t.right(239)  
  for x in range(200, 0, -1): 
    t.pencolor('black') 
    t.width(x/100 + 7)
    t.forward(x) 
    t.right(59) 
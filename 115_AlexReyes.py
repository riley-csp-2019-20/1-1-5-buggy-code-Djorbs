import turtle as trtl

drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20) #Creates the spider body
legs = 4 #Configures the legs
leg_length = 38 #Configures the legs
angle = 120 / legs  #Configures the legs
drawer.pensize(5)
loops = 0
while (loops < legs): #This loops creates the legs
  drawer.goto(0,20)
  drawer.setheading(angle*loops + 90)
  drawer.pendown()
  drawer.circle(leg_length, 180)
  drawer.penup()
  loops = loops + 1
loops = 0
while (loops < legs): #This loops creates the legs
  drawer.goto(0,20)
  drawer.setheading(angle*loops + 180)
  drawer.pendown()
  drawer.circle(leg_length, -180)
  drawer.penup()
  loops = loops + 1
drawer.penup()
drawer.goto(10, 45)
drawer.pencolor("white")
drawer.pensize(5)
drawer.pendown()
drawer.circle(3)
drawer.penup()
drawer.goto(-5, 45)
drawer.pendown()
drawer.circle(3)
drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()


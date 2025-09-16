import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []  # creating a body of snake

# creating a screen
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("light blue")
s1.setup(width=600, height=600)

# creating a head
h1 = turtle.Turtle()
h1.shape("circle")
h1.speed(0)
h1.color("red")
h1.fillcolor("green")
h1.penup()
h1.goto(0, 0)
h1.direction = "stop"

# creating a food
f1 = turtle.Turtle()
f1.shape("square")
f1.speed(0)
f1.color("red")
f1.fillcolor("blue")
f1.penup()
f1.ht()
f1.goto(200, 200)
f1.st()

# scoreboard
s2 = turtle.Turtle()
s2.ht()
s2.penup()
s2.goto(-250, 250)
s2.write("Score: 0   |   Highest Score: 0")

# movement functions
def moveup():
    if h1.direction != "down":
        h1.direction = "up"

def movedown():
    if h1.direction != "up":
        h1.direction = "down"

def moveleft():
    if h1.direction != "right":
        h1.direction = "left"

def moveright():
    if h1.direction != "left":
        h1.direction = "right"

def movestop():
    h1.direction = "stop"


def move():
    if h1.direction == "up":
        y = h1.ycor()
        h1.sety(y + 20)
    if h1.direction == "down":
        y = h1.ycor()
        h1.sety(y - 20)
    if h1.direction == "left":
        x = h1.xcor()
        h1.setx(x - 20)
    if h1.direction == "right":
        x = h1.xcor()
        h1.setx(x + 20)


# event handling
s1.listen()
s1.onkey(moveup, "Up")
s1.onkey(movedown, "Down")
s1.onkey(moveright, "Right")
s1.onkey(moveleft, "Left")
s1.onkey(movestop, "space")

# mainloop
while True:
    s1.update()

    # check collision with border
    if h1.xcor() > 290:
        h1.setx(-290)
    if h1.xcor() < -290:
        h1.setx(290)
    if h1.ycor() > 290:
        h1.sety(-290)
    if h1.ycor() < -290:
        h1.sety(290)

    # check collision with food
    if h1.distance(f1) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        f1.goto(x, y)

        # increase the length of snake
        b1 = turtle.Turtle()
        b1.speed(0)
        b1.penup()
        b1.shape("square")
        b1.color("yellow")
        bodies.append(b1)

        sc = sc + 10
        if sc > hs:
            hs = sc
        s2.clear()
        s2.write("Score: {}   |   Highest Score: {}".format(sc, hs))

        # increase speed safely
        delay = max(0.01, delay - 0.001)

    # move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = h1.xcor()
        y = h1.ycor()
        bodies[0].goto(x, y)

    move()

    # check collision with snake body
    for b in bodies:
        if b.distance(h1) < 20:
            time.sleep(1)
            h1.goto(0, 0)
            h1.direction = "stop"

            # hide bodies
            for b in bodies:
                b.ht()
            bodies.clear()

            # reset score
            sc = 0
            s2.clear()
            s2.write("Score: {}   |   Highest Score: {}".format(sc, hs))

    time.sleep(delay)
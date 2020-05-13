import turtle
import time
import random

delay = 0.1

score = 0
highScore = 0

# setup

window = turtle.Screen()
window.title("Snake Game by AwsomemanNever")
window.bgcolor("green")
window.setup(600, 600)
window.tracer(0)
edge = 280

foodPosition = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]

# Snake Head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
x = random.choice(foodPosition)
y = random.choice(foodPosition)
food.goto(y, x)

segments = []

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# functions
def goUp():
    if head.direction != "down":
        head.direction = "up"


def goDown():
    if head.direction != "up":
        head.direction = "down"


def goRight():
    if head.direction != "left":
        head.direction = "right"


def goLeft():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)


# keyboard bindings

window.listen()
window.onkeypress(goUp, "w")
window.onkeypress(goUp, "Up")
window.onkeypress(goDown, "s")
window.onkeypress(goDown, "Down")
window.onkeypress(goRight, "d")
window.onkeypress(goRight, "Right")
window.onkeypress(goLeft, "a")
window.onkeypress(goLeft, "Left")

# main game loop
while True:
    window.update()

    # check for collision with border
    if head.xcor() > edge or head.xcor() < -edge or head.ycor() > edge or head.ycor() < -edge:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments

        for newSegment in segments:
            newSegment.goto(1000, 1000)

        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score: 0  High Score: {}".format(highScore), align="center", font=("Courier", 24, "normal"))

        delay = 0.1

    # check for collision
    if head.distance(food) < 20:
        # move food
        x = random.choice(foodPosition)
        y = random.choice(foodPosition)
        food.goto(x, y)

        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("grey")
        newSegment.penup()
        segments.append(newSegment)

        # increase the score

        score += 10

        if score > highScore:
            highScore = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))
        delay -= 0.001


    # move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for body hits

    for newSegment in segments:
        if newSegment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for newSegment in segments:
                newSegment.goto(1000, 1000)

            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: 0  High Score: {}".format(highScore), align="center", font=("Courier", 24, "normal"))
            delay = 0.1

    time.sleep(delay)

window.mainloop()

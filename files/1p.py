# Pong game by CuBeRJAN3
import time
import turtle
import random
from timeit import default_timer as timer


# Score values
global l_score
global r_score
l_score = 0
r_score = 0


# Creating window
win = turtle.Screen()
win.setup(900,600)
win.title("Pong")
win.bgcolor("black")
win.tracer(0)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.penup()
left_paddle.color("white")
left_paddle.shape("square")
left_paddle.shapesize(3,1)
left_paddle.goto(-435,0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.penup()
right_paddle.color("white")
right_paddle.shape("square")
right_paddle.shapesize(3,1)
right_paddle.goto(430,0)

# Separator
separator = turtle.Turtle()
separator.penup()
separator.color("white")
separator.shape("square")
separator.shapesize(100,0.2)
separator.goto(0,0)

# Ball
ball = turtle.Turtle()
ball.penup()
ball.color("white")
ball.shape("square")
ball.shapesize(0.6,0.6)
ball.goto(0,0)
global ball_dx
ball_dx = 3.6
global ball_dy
ball_dy = 3.6

# Pen
pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(-210,230)
pen.write('0          0',font=("Monospace", 45, "normal"))


global waited
waited=0
# Move the ball
def move_ball():
    global ball_dx
    global ball_dy
    global l_score
    global r_score
    global waited
    x = ball.xcor()
    y = ball.ycor()
    if x > 440:
        ball_dx *= -1
        l_score += 1
        x,y=0,0
        time.sleep(1)
        waited=1
        pen.clear()
        pen.write('{}          {}'.format(l_score,r_score),font=("Monospace", 45, "normal"))
    if x < -440:
        ball_dx *= -1
        r_score += 1
        x,y=0,0
        time.sleep(1)
        waited=1
        pen.clear()
        pen.write('{}          {}'.format(l_score,r_score),font=("Monospace", 45, "normal"))
    if y > 290 or (y < -290):
        ball_dy *= -1
    x += ball_dx
    y += ball_dy
    ball.goto(x,y)

# Move the left paddle up
def move_lu():
    y = left_paddle.ycor()
    left_paddle.sety(y+30)
    if (y > 245):
        left_paddle.sety(260)
        
# Move the right paddle up
def move_ru():
    y = right_paddle.ycor()
    right_paddle.sety(y+6)
    if (y > 245):
        right_paddle.sety(260)

# Move the left paddle down
def move_ld():
    y = left_paddle.ycor()
    left_paddle.sety(y-30)
    if (y < -245):
        left_paddle.sety(-260)

# Move the right paddle down
def move_rd():
    y = right_paddle.ycor()
    right_paddle.sety(y-6)
    if (y < -245):
        right_paddle.sety(-260)

# Check for collision of paddle and ball
def check_collision():
    global ball_dx
    global ball_dy
    global l_score
    global r_score
    l_y = left_paddle.ycor()
    r_y = right_paddle.ycor()
    l_x = left_paddle.xcor()
    r_x = right_paddle.xcor()
    l_xl = l_x+15
    l_xm = l_x-15
    l_yl = l_y+30
    l_ym = l_y-30
    r_xr = r_x+15
    r_xm = r_x-15
    r_yr = r_y+30
    r_ym = r_y-30
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    if ball_x > l_xm and (ball_x < l_xl) and (ball_y > l_ym) and (ball_y < l_yl):
        ball_dx *= -1
    if ball_x > r_xm and (ball_x < r_xr) and (ball_y > r_ym) and (ball_y < r_yr):
        ball_dx *= -1

# AI
def move_ai():
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    r_x = right_paddle.xcor()
    r_y = right_paddle.ycor()
    dist = random.randint(15,42)
    r_yp = r_y+dist
    r_ym = r_y-dist
    if ball_x > 200:
        if ball_y < r_yp:
            move_rd()
        elif ball_y > r_ym:
            move_ru()

# Keybindings
win.listen()
win.onkeypress(move_lu,"Up")
win.onkeypress(move_ld,"Down")

# Main loop
while True:
    start = timer()

    # Move the ball
    move_ball()

    # Check for collision
    check_collision()

    # Move AI
    move_ai()

    # Update window
    win.update()

    end = timer()
    # Framerate
    diff=end-start
    if waited == 0:
        wait=0.01-diff
    else:
        wait=1.508-diff
        waited=0
    time.sleep(wait)

import turtle #bib qui sert a faire une interface de debutant

Wd = turtle.Screen()
Wd.title("Pong game")
Wd.bgcolor('black')
Wd.setup(width=800, height=600)
Wd.tracer(0)
#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0    Player B : 0", align="center", font=("courrier", 24, "normal"))
#scores
score_a = 0
score_b = 0
#functions
# *paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
#Controle avec clavier
Wd.listen()
Wd.onkeypress(paddle_a_up, "z")
Wd.onkeypress(paddle_a_down, "s")


#*paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
#Controle avec clavier
Wd.listen()
Wd.onkeypress(paddle_b_up, "Up")
Wd.onkeypress(paddle_b_down, "Down")
#paddles and ball collisions




#la boucle du jeu
while True:
    Wd.update()
    #Bouger thee ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    #UP
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
    #DOWN
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
    #LEFT
    if ball.xcor() > 390 :
        ball.setx(390)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A : {}    Player B : {}".format(score_a, score_b), align="center", font=("courrier", 24, "normal"))

    #RIGHT
    if ball.xcor() < -390 :
        ball.setx(-390)
        ball.dx *= -1
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A : {}    Player B : {}".format(score_a, score_b), align="center", font=("courrier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        score_b = score_b + 1
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
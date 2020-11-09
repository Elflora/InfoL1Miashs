import turtle
from math import *
#Il se passe des choses bizarre dans ce code
#PAS FINI

def spiral(n) :
    turtle.pencolor("red")
    for i in range(n):
        turtle.forward(i * 10)
        turtle.right(144)

def carre(n) :
    turtle.pencolor("black")
    for i in range(4) :
        turtle.forward(n)
        turtle.right(90)

def cinqCarre(n) :
    turtle.pencolor("black")
    for i in range(5) :
        carre(n)
        n += 10

def cinquanteCarre(n) :
    turtle.pencolor("black")
    for i in range(50) :
        carre(n)
        n += 10

def dixCarre() :
    for i in range(10) :
        carre(50)
        turtle.up()
        turtle.goto(55*i, turtle.ycor())
        turtle.down()

def centCarre() :
    for i in range(10) :
        dixCarre()
        turtle.up()
        turtle.goto(0, (i+1)*55)
        turtle.down()
        
def carreTournant(n) :
    for i in range(n+1) :
        carre(100)
        turtle.up()
        turtle.setheading((360/n)*i)
        turtle.down()

def carreEmboite(n) :
    longueur = 50
    angle = atan(0.5 / (1 - 0.5)) * 180 / pi
    coeff = sqrt(2)
    
    for i in range(n+1) :
        carre(longueur)
        turtle.forward(0.5 * longueur)
        turtle.right(angle)
        longueur /= coeff
        
        
        
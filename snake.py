from turtle import *
from random import randrange
from time import sleep

snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
apple_x=randrange(-20,18)*10
apple_y=randrange(-19,19)*10

aim_x=10
aim_y=0

def square(x,y,size,color_name):
    up()
    goto(x,y)
    down()
    color(color_name)
    begin_fill()

    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    end_fill()

def game_Loop():
    global apple_x,apple_y,aim_y,aim_x,snake
    
    snake.append([snake[-1][0]+aim_x,snake[-1][1]+aim_y])
    
    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else:
        apple_x=randrange(-20,18)*10
        apple_y=randrange(-19,19)*10
    
    if not inside() or snake_inside():
        square(snake[-1][0],snake[-1][1],10,"red")
        update()
        sleep(2)
        snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
        apple_x=randrange(-20,18)*10
        apple_y=randrange(-19,19)*10
        aim_x=10
        aim_y=0

    clear()
    square(-210,-200,410,"black")
    square(-200,-190,390,"white")

    square(apple_x,apple_y,10,"red") 
    for n in range(len(snake)):
        square(snake[n][0],snake[n][1],10,"black")
    
    ontimer(game_Loop,300)
    update()

def change(x,y):
    global aim_x,aim_y
    aim_x=x
    aim_y=y

def inside():
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True
    else:
        return False

def snake_inside():
    for n in range(len(snake)-1):
        if snake[-1][0]==snake[n][0] and snake[-1][1]==snake[n][1]:
            return True
    return False

setup(420,420,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda:change(0,10),"w")
onkey(lambda:change(0,-10),"s")
onkey(lambda:change(10,0),"d")
onkey(lambda:change(-10,0),"a")
game_Loop()
done()
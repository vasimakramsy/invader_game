#import dependencies
import turtle
import os
import math
import random 

#Set up the screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title("Space Invader")


#Draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#create a player

player = turtle.Turtle()
player.color("red")
player.speed(0)
player.shape('triangle')
player.penup()
player.setposition(0, -262)
player.setheading(90)

#Create Enemy

enemySpeed = 5

enemy = turtle.Turtle()
enemy.speed(0)
enemy.color('white')
enemy.shape('circle')
enemy.penup()
x = random.randint(-200,200)
y = random.randint(100, 250)
enemy.setposition(x,y)
enemy.setheading(90)

# bullets

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()


#player movement

playerSpeed = 15

def move_left():
    x = player.xcor()
    x-=playerSpeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x+=playerSpeed
    if x > 280:
        x = 280
    player.setx(x)

bulletSpeed = 20 

bulletState = "ready"

def fireBullet():
    global bulletState
    #move the bullet above the player
    if bulletState == "ready":
        bulletState = "fire"
        x = player.xcor()
        y = player.ycor() + 20
        bullet.setposition(x,y)
        bullet.showturtle()

#collision Course

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance <15:
        return True
    else:
        return False

#keyboard bidding

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fireBullet, "space")




#game Loop

if __name__ == "__main__":
    while True:
        #Move the enemy
        
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)


        if enemy.xcor()>280:
            y = enemy.ycor()
            y -= 40
            enemySpeed *= -1
            enemy.sety(y)

        if enemy.xcor()<-280:
            y = enemy.ycor()
            y -= 40
            enemySpeed *= -1
            enemy.sety(y)

        if bulletState == "fire":
            y = bullet.ycor()
            y += bulletSpeed
            bullet.sety(y)

        if bullet.ycor()>= 280:
            bullet.hideturtle()
            bulletState ="ready"

        #check for collision
        if isCollision(bullet, enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0,-400)

            enemy.setposition(-200, 250)
            enemySpeed += 1

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!!!")
            break
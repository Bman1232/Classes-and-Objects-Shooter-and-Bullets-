from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key, health, outline_color):
        super().__init__()
        self.ht()
        self.speed(0)
        self.player_color = color
        self.pencolor(outline_color)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        self.health = 3
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())
    
    def fire(self):
        self.bullets.append(Bullet(self))
    
    def damage(self, outline_color):
        self.health -= 1
        if self.health == 2:
            self.color("yellow")
            self.pencolor(outline_color)
        elif self.health == 1:
            self.color("red")
            self.pencolor(outline_color)

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.player = player
        self.speed(0)
        self.color(player.player_color)
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.seth(player.heading())
        self.speed(5)
        self.st()

    def move(self, player):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230:
            self.kill()
        if self.ycor() > 230 or self.ycor() < -230:
            self.kill()

    def kill(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullets.remove(self)

    def die(self):
        pass
screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()


playing_area()

p1 = Player(-100, 0, "red",screen, "d", "a", "w", 3, "red")
p2 = Player(100,0,"blue",screen, "Right","Left", "Up", 3, "blue")

while p1.alive and p2.alive:
    p1.move()
    p2.move()
    for bullet in p1.bullets:
        bullet.move(p1)
        if p2.distance(bullet) < 20:
            bullet.kill()
            p2.damage("blue")
            print("Damage taken")

    for bullet in p2.bullets:
        bullet.move(p2)
        if p1.distance(bullet) < 20:
            bullet.kill()
            p1.damage("red")
            print("Damage taken")
    
    if p1.health < 1:
        p1.hideturtle()
        p1.remove()
    if p2.health < 1:
        p2.hideturtle()
        p2.remove()




screen.exitonclick()
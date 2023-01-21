#Building Maze Game
import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A MongoDB New Year")
wn.setup(700,700)
wn.tracer(0)

#Register shapes
images = ["Maze_Leaf.gif", "Maze_Redpacket.gif", "Maze_Wall_2.gif", "Maze_Rabbit.gif"]
for image in images:
    turtle.register_shape(image)

#Create Pen to draw squares
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Create Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Maze_Leaf.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        #Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def go_down(self):
        #Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        #Calculate the spot to move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape("Maze_Leaf.gif")
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        #Calculate the spot to move to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape("Maze_Leaf.gif")
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

#Create treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Maze_Redpacket.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Create Enemy
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Maze_Rabbit.gif")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        #Check if player is close
        #If so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
        
        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose different direction
            self.direction = random.choice(["up,", "down", "left", "right"])
        
        #Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100,300))
    
    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Create levels list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXX         EXXXXXXXX",
"XX XXXX              XXTX",
"XX             XX       X",
"XX   XXXXXXXXXXXXXXXX   X",
"XXXXXX XX               X",
"XXE                 XXXXX",
"XXXXXX     XXXXXXXXXXXXXX",
"X          XXXXXXXXXXXXXX",
"XT XXX   XXXXXXXXXXXXXXXX",
"XXXXXX    XXXXXXXXXXXXXXX",
"XXXXXX         XXXXXXXXXX",
"XXXXXX      XXXXXXXXXXXXX",
"XXXXX     XXXXXX        X",
"XXX       XXXXXX  XXXX  X",
"XXX     XXXXXXXX  XXXX  X",
"XXXXX     X       XXXXX X",
"XXXX          E   XX    X",
"X            XXXXXXXXX TX",
"X   XXXXXXXXXXXXXXXXXXXXX",
"X   XXXXXXXXXXXX       TX",
"XX   E   XXXXXXX     XXXX",
"XX            XX    XXXXX",
"XXXX                XXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Add a treasures list
treasures = []

#Add enemies list
enemies = []

#Add maze to maze list
levels.append(level_1)

#Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            #Note the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("Maze_Wall_2.gif")
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))

            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #Check if it is a T (representing treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            #Check if it is an E (representing enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

#Create class instance
pen = Pen()
player = Player()

#Create wall coordinate list
walls = []

#Set up the level
setup_maze(levels[1])

#Keyboard Bining
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

#Turn off screen updates
wn.tracer(0)

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

#Main game loop
while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the treasure gold to the player gold
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            #Destroy treasure
            treasure.destroy()
            #Remove the treasure from the treasures list
            treasures.remove(treasure)

    #Iterate through enemy list to see if the player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            print ("Player dies!")

    #Update screen
    wn.update()
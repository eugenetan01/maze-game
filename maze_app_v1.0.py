#Building Maze Game
import turtle
import math

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("A MongoDB New Year")
wn.setup(700,700)

#Register shapes
turtle.register_shape("Maze_Leaf_Right.gif")
turtle.register_shape("Maze_Leaf_Left.gif")
turtle.register_shape("Maze_Redpacket.gif")
turtle.register_shape("Maze_Wall.gif")

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
        self.shape("Maze_Leaf_Right.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def go_down(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape("Maze_Leaf_Left.gif")

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.shape("Maze_Leaf_Right.gif")
        
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

#Create levels list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXX         XXXXXXXX",
"XX XXXXXX   XXXX    XXXXT",
"X   XX    X XXXXXXX    X ",
"XXX    XXXXXXXXX  XXXX   ",
"XXXXXX                   ",
"XXXXXXXXXXXXXX      XXXXX",
"XXXXXXX  XXXXXXX  XXXXXXX",
"X        XXXXXXX  XXXXXXX",
"X   XXX XXXXXX    XXXXXXX",
"XXXXXXX   XXXX XX   XXXX ",
"XXXXXXXX       X  XXXXXX ",
"XXXXXXXXXXXXXXXX  XXXXXX ",
"X   XX   XXXXXXX  XXXXXX ",
"X   XX   XXXXXXX  XXXXXX ",
"X   XX   XXXXXXX  XXXXXX ",
"X   XX   XXXXXXX  XXXXXX ",
"X   XX   XXXXXXX  XXXXXX ",
"X   XX   XXXXXXX  XXXXXX ",
"X   XX   XXXXXXX        X",
"X   XX   XXXXXXX        X",
"XX      XXXXX      XXXXXX",
"X   XX      XXXX  XXXXXXX",
"XXXX                   XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Add a treasures list
treasures = []

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
                pen.shape("Maze_Wall.gif")
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))

            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #Check if it is a T (representing treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

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

    #Update screen
    wn.update()




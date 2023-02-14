import turtle
import time
import random

# Define Global Variables
delay = 0.2
score = 0
high_score = 0
segments = []

#Setting up the screen, title, background color, width etc.
# must return the window created
def setUpScreen():
    # Set up the screen
    wn = turtle.Screen()
    # Set background color
    wn.bgcolor('turquoise')
    # Set height and width
    wn.setup(600, 600)
    #title of the screen
    wn.title('Snake game')
    # Turns off the screen updates
    wn.tracer(False)
    return wn

# Write score and highscore on the screen
def trackScoreOnScreen():
    pen = turtle.Turtle()
    # Set color
    pen.color('white', 'black')
    # penup and hide turtle
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    # Move the score to top of screen
    pen.write("Score: 0  High Score: 0", align="center", font=("Comic sans", 24, "normal"))
    return pen

# Create and return the Head of the snake
def createSnakeHead():
    # Snake head
    head = turtle.Turtle()
    # Set speed, shape, color and move it center of the screen
    head.speed(0)
    head.shape('square')
    head.color('black')
    head.penup()
    head.goto(0, 0)
    # Set direction as stop
    head.direction = 'stop'
    return head

# Create and return the first food on the screen
def createFood():
    # Create Snake food
    food = turtle.Turtle()
     # Set speed, shape, color and move it some location of the screen
    food.speed(0)
    food.shape('triangle')
    food.color('brown')
    food.penup()
    food.goto(0, 100)
    return food

# Function to call when up key is pressed
# Snake can go up only when the direction is right or left and not down
def go_up():
    # remove print statement after implementing this function
    if head.direction!='down':
        head.direction = 'up'
    print("go_up function called")


# Function to call when down key is pressed
# Snake can go down only when the direction is right or left and not up
def go_down():
    # remove print statement after implementing this function
    if head.direction!='up':
        head.direction = 'down'
    print("go_down function called")


# Function to call when left key is pressed
# Snake can go left only when the direction is up or down and not right
def go_left():
     # remove print statement after implementing this function
    if head.direction!='right':
        head.direction = 'left'
    print("go_left function called")

# Function to call when right key is pressed
# Snake can go right only when the direction is up or down and not left
def go_right():
    # remove print statement after implementing this function
    if head.direction!='left':
        head.direction = 'right'
    print("go_right function called")
        

# Bind Up, Down, Left and Right keys with their function
def bindKeyboardKeys(win):
    # remove print statement after implementing this function
    win.listen()
    win.onkeypress(go_up, 'Up')
    win.onkeypress(go_down, 'Down')
    win.onkeypress(go_right,'Right')
    win.onkeypress(go_left,'Left')
    print("bindKeyboardKeys function called")

# Function to call to move the snake, based on the direction of the snake
# snake body should move automatically in that direction
# should be called from the main loop. 
def moveHead():
    # remove print statement after implementing this function
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)
    print("moveHead function called")

# Move segments

def moveSegments():
    global segments
    
     # Move the end segments first in reverse order
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
     # Using for loop move the segments
     # For example if there are 3 segments 2, 1, and 0
     # Move second segment to location of first and move first segment to location of zero

    # Move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


# Detect collision of snake head with the screen borders
# If collision detected return True else return False
def detectCollisionWithBorder(head):
    # remove print statement after implementing this function
    print("detectCollisionWithBorder function called")
    x = head.xcor()
    y = head.ycor()
    if x>280 or x<-280 or y> 280 or y<-280:
        return True
    return False

# Handle the collision if detected true
def handleCollisionWithBorder(head, trackScore):
    global delay
    global score
    
    # Make head goto center of the screen
    head.goto(0,0)
    # Make head direction dummy so that it do not move
    head.direction = 'stop'
    # Hide the segments
    for seg in segments:
        seg.goto(1000,1000)
    # Clear the segments list
    segments.clear()
    # Reset the score
    score = 0
    # Reset the delay
    delay = 0.2
    # Clear trackscore and start from 0
    trackScore.clear()
    trackScore.write("score: {} High score: {}".format(score, high_score), align="center", font=("Comic sans", 24, "normal"))
# Detect collision of snake head with food
# If collision detected return True else return False
def detectCollisionWithFood(head, food):
    # remove print statement after implementing this function
    print("detectCollisionWithFood function called")
    if head.distance(food)<20:
        return True
    return False


# Handle the collision if detected true
def handleCollisionWithFood(head, trackScore, food):
    global delay
    global score
    global high_score
    
    # Move the food to a random spot
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)
    
    # Add a segment, define its shape and color
    segment = turtle.Turtle()
    segment.shape('square')
    segment.speed(0)
    segment.color('grey')
    segment.penup()
    
    # append it to the segments list
    segments.append(segment)
    
    # Shorten the delay, to move snake faster
    delay = delay-0.001
    # Increase the score by 10
    score = score+10
    # check for high score and update it if player made a new high score
    if high_score < score:
        high_score = score
    # Update trackScore
    trackScore.clear()
    trackScore.write("Score:{} High Score:{}".format(score, high_score), align="center",font=("Comic Sans", 24,"normal"))

# Detect collision of snake head with its body
# needs to check for all segment, thus will use for loop
# If collision detected return True else return False
def detectCollisionOfHeadWithSegment(head):
    # remove print statement after implementing this function
    for segment in segments:
        if head.distance(segment)<20:
            return True
    print("moveHead function called")
    
    return False


####################################
#                                  #
#   Start of the main function     #
#                                  #
####################################

#Call Functions in main program
wn = setUpScreen()
head = createSnakeHead()
food = createFood()
trackScore = trackScoreOnScreen()
bindKeyboardKeys(wn)

# Start of main game loop
while True:
    wn.update()
    
    # Check for a collision of head with the screen border
    if detectCollisionWithBorder(head):
        time.sleep(1)
        handleCollisionWithBorder(head, trackScore)

    # Check for a collision with the food
    if detectCollisionWithFood(head, food):
        handleCollisionWithFood(head, trackScore, food)
        
    moveSegments()
    moveHead()    

    # Detect collision of snake body with its head
    if detectCollisionOfHeadWithSegment(head):
        time.sleep(1)
        handleCollisionWithBorder(head, trackScore)
        
    # Sleep for time equal to delay to add delay
    time.sleep(delay)


wn.mainloop()
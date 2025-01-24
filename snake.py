from uib_inf100_graphics.event_app import run_app
from snake_view import draw_board
import random
from tkinter import Tk, font


def app_started(app):
    
    app.debug_mode = False
    app.state = "welcome"
    app.score = 0

def initialize_board(app):
    if app.level == "normal":
        app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
         ]
    elif app.level == "small":
        app.board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0,-1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0],
        ]
    elif app.level == "large":
        app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    app.snake_size = 3
    app.head_pos = (3, 4)
    app.direction = "east"
    
    
    


def timer_fired(app):
    if app.debug_mode == False and app.state == "active":
        move_snake(app)
    app.timer_delay = 150

#Kontroller for tastetrykk
def key_pressed(app, event):

    if event.key.lower() == "space" and app.state == "welcome":
        app.state = "menu"

    if event.key.lower() == "1" and app.state == "menu":
        app.level = "small"
        app.state = "active"
        initialize_board(app)

    if event.key.lower() == "2" and app.state == "menu":
        app.level = "normal"
        app.state = "active"
        initialize_board(app)

    if event.key.lower() == "3" and app.state == "menu":
        app.level = "large"
        app.state = "active"
        initialize_board(app)
        
    if event.key == "q":
        app.debug_mode = not app.debug_mode

    if event.key.lower() == "return":
        app_started(app)
        app.state = "menu"
        
    

    if app.state == "active":
        if event.key.lower() == "w":
            app.direction = "north"
    
        if event.key.lower() == "s":
            app.direction = "south"

        if event.key.lower() == "a":
            app.direction = "west"

        if event.key.lower() == "d":
            app.direction = "east"

        if event.key == "Space" and app.debug_mode:
            move_snake(app)

#Ny hodeposisjon
def get_next_head_position(head_pos, direction):
    liste = list(head_pos)
    if direction == "north":
        liste[0] -= 1
    if direction == "south":
        liste[0] += 1
    if direction == "west":
        liste[1] -= 1
    if direction == "east":
        liste[1] += 1
    return tuple(liste)
    

#Flyttingen av slangen
def subtract_one_from_all_positives(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                grid[i][j] -= 1

def add_apple_at_random_location(grid):
    while True:
        i = random.randint(0, len(grid) - 1)
        j = random.randint(0, len(grid[0])- 1)
        if grid[i][j] == 0:
            grid[i][j] = -1
            return
    



    
def is_legal_move(pos, board):
    x, y = pos
    if x < 0 or y < 0 or x >= len(board) or y >=len(board[0]):
        return False
    
    if board[x][y] > 0:
        return False
    
    return True
    
    

def move_snake(app):
    new_head_pos = get_next_head_position(app.head_pos, app.direction)
    app.head_pos = new_head_pos
    while not is_legal_move(app.head_pos, app.board):
        app.state = "gameover"
        return

    
    if app.board[app.head_pos[0]][app.head_pos[1]] == -1:
        app.snake_size +=1
        app.score += 1
        add_apple_at_random_location(app.board)
    else: subtract_one_from_all_positives(app.board)
    
    app.board[app.head_pos[0]][app.head_pos[1]] = app.snake_size

def redraw_all(app, canvas):
    if app.state == "active":
        draw_board(canvas, 25 , 25 , app.width -25, app.height -25, app.board, app.debug_mode)
        canvas.create_text(app.width/2, 10 , text = f'score = {app.score}')
    elif app.state == "gameover":
        canvas.create_rectangle(0, 0 , app.width, app.height, fill = "#f1807e")
        canvas.create_text(app.width/2, app.height/2, text = "Game Over", font = ('Times', 50, 'italic bold'))
        canvas.create_text(app.width/2, app.height/2 + 70, text = "Press enter to retry", font = ('Times', 30, 'italic bold'))
    elif app.state == "welcome":
        canvas.create_rectangle(0, 0 , app.width, app.height, fill = "green")
        canvas.create_text(app.width/2, app.height/2 - 100, text = "Welcome to snake!!", font = ('Times', 50, 'italic bold'))
        canvas.create_text(app.width/2, app.height/2 -50  , text = "Collect all the apples to grow", font = ('Times', 15, 'italic bold'))
        canvas.create_text(app.width/2, app.height/2 -20, text = "Try not to crash!", font = ('Times', 15, 'italic bold'))
        canvas.create_text(app.width/2, app.height/2 + 30, text = "Press space to start", font = ('Times', 30, 'italic bold'))
        canvas.create_text(app.width/2, app.height - 60 , text = "Controls:", font = ('Times', 20, 'italic bold'))
        canvas.create_text(app.width/2, app.height - 40, text = "w = up | s = down | a = left | d = right", font = ('Times', 15, 'italic bold'))
    elif app.state == "menu":
        canvas.create_rectangle(0, 0 , app.width, app.height, fill = "#90ee90")
        canvas.create_text(app.width/2, app.height/2 - 100, text = "Choose a level", font = ('Times', 50, 'italic bold'))
        canvas.create_text(100, app.height/2 , text = "Small [1]", font = ('Times', 30, 'italic bold'))
        canvas.create_text(app.width/2, app.height/2 , text = "Normal [2]", font = ('Times', 30, 'italic bold'))
        canvas.create_text(app.width - 100, app.height/2 , text = "Large [3]", font = ('Times', 30, 'italic bold'))
  
        

    

    if app.debug_mode == True:
        canvas.create_text(app.width/2, 15, text = f'app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction={app.direction}')


run_app(width=500, height=400, title="Snake")


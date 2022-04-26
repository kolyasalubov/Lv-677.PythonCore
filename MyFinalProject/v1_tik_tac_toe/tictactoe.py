import pygame as pg
import sys
from pygame.locals import *
import time
import os

#initialize global variables
winner = None
draw = False
XO = 'x'
xo_width = 80
xo_height = 80
width = 400
height = 400
extra_height = height/4
white = (255, 255, 255)
gray = (38, 38, 43)
yellow = (191, 243, 12)
blue = (7, 4, 130)
line_color = gray
rose = (214, 4, 67)
m_color = None
message = None
posx = None
posy = None
start_button = False

#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]

#initializing pygame window
pg.init()
fps = 100
CLOCK = pg.time.Clock()
game_screen = pg.display.set_mode((width, height+extra_height), pg.RESIZABLE, 32)
pg.display.set_caption("Tic Tac Toe")

#getting absolute path sounds
dir_path = os.path.dirname(__file__)
turn_sound_file = os.path.join(dir_path, 'turn_sound.wav')
draw_sound_file = os.path.join(dir_path, 'draw_sound.wav')
win_sound_file = os.path.join(dir_path, 'win_sound.wav')

#getting absolute path images
opening_path = os.path.join(dir_path, "TicTacOpening.png")
x_path = os.path.join(dir_path, "X.png")
o_path = os.path.join(dir_path, "O.png")

#loading the images
opening = pg.image.load(opening_path)
x_img = pg.image.load(x_path)
o_img = pg.image.load(o_path)

#resizing images
x_img = pg.transform.scale(x_img, (xo_width,xo_height))
o_img = pg.transform.scale(o_img, (xo_width,xo_height))


class Music():
    def __init__(self, sound: str):
        self.sound = sound

    def play_sound(self):
        pg.mixer.music.load(self.sound)
        pg.mixer.music.play(0)

turn_sound = Music(turn_sound_file)
draw_sound = Music(draw_sound_file)
win_sound = Music(win_sound_file)


class Button():
    def __init__(self, b_size: tuple, b_color: tuple, t_color: tuple, text: str):
        self.b_size = b_size
        self.b_color = b_color
        self.t_color = t_color        
        self.text = text

    def draw_button(self):
        t_font = pg.font.Font(None, 60)
        t_message = t_font.render(self.text, 1, (self.t_color))

        # copy the rendered message onto the board
        game_screen.fill (self.b_color, self.b_size)
        text_rect = t_message.get_rect(center=(width/2, height+(extra_height/2)))
        game_screen.blit(t_message, text_rect)
        pg.display.update()       

    def activate_button(self, input_action, output_action):
        pass
        

def game_opening():
    global opening

    opening = pg.transform.scale(opening, (width, height))
    game_screen.blit(opening,(0,0))
    text = "START"
    start_button = Button((0, height, width+extra_height, extra_height), gray, yellow, text)
    start_button.draw_button()


def grid():
    game_screen.fill(white)
    # Drawing vertical lines
    pg.draw.line(game_screen,line_color,(width/3,0),(width/3, height),7)
    pg.draw.line(game_screen,line_color,(width/3*2,0),(width/3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(game_screen,line_color,(0,height/3),(width, height/3),7)
    pg.draw.line(game_screen,line_color,(0,height/3*2),(width, height/3*2),7)
    draw_status()


def userClick():
    #get coordinates of mouse click
    global start_button
    x, y = pg.mouse.get_pos()

    if 0 < x < width and height < y < height+extra_height:        
        start_button = True

    elif start_button == True:
        #get column of mouse click (1-3)
        if x < width/3:
            col = 1
        elif (x < width/3*2):
            col = 2
        elif x < width:
            col = 3
        else:
            col = None
            
        #get row of mouse click (1-3)
        if y < height/3:
            row = 1
        elif y < height/3*2:
            row = 2
        elif y < height:
            row = 3
        else:
            row = None

        if(row and col and TTT[col-1][row-1] is None):
            global XO
            
            fill_TTT(col, row)
            set_position(col, row)
            drawXO(posx, posy)
            check_win()


def set_position(col, row):
    global posx, posy

    if col == 1:
        posx = width/6 - (xo_width/2)
    if col == 2:
        posx = width/2 - (xo_width/2)
    if col == 3:
        posx = width/6*5 - (xo_width/2)

    if row == 1:
        posy = height/6 - (xo_height/2)
    if row == 2:
        posy = height/2 - (xo_height/2)
    if row == 3:
        posy = height/6*5 - (xo_height/2)


def fill_TTT(x, y):
    global TTT
    TTT[x-1][y-1] = XO


def drawXO(x, y):
    global XO
    if XO == 'x':
        game_screen.blit(x_img, (x, y))
        XO = 'o'
    else:
        game_screen.blit(o_img, (x, y))
        XO = 'x'
    
    pg.display.update()


def check_win():
    global TTT, winner, draw

    # check for winning columns
    for col in range (0,3):
        if ((TTT [col][0] == TTT[col][1] == TTT[col][2]) and(TTT [col][0] is not None)):
            # this row won
            winner = TTT[col][0]
            pg.draw.line(game_screen, yellow, ((col+1)/3*width - width/6, height/9), 
                                              ((col+1)/3*width - width/6, height/9*8), 10)
            break

    # check for winning rows
    if winner == None:
        for row in range (0, 3):
            if (TTT[0][row] == TTT[1][row] == TTT[2][row]) and (TTT[0][row] is not None):
                # this column won
                winner = TTT[0][row]
                #draw winning line
                pg.draw.line (game_screen, yellow, (width/9, (row+1)/3*height - height/6),\
                                                (width/9*8, (row+1)/3*height - height/6), 10)
                break

    # check for diagonal winners
    if winner == None:
        if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
            # game won diagonally left to right
            winner = TTT[0][0]
            pg.draw.line (game_screen, yellow, (width/9, height/9), 
                                            (width/9*8, height/9*8), 10)
       
    if winner == None:
        if (TTT[2][0] == TTT[1][1] == TTT[0][2]) and (TTT[2][0] is not None):
            # game won diagonally right to left
            winner = TTT[2][0]
            pg.draw.line (game_screen, yellow, (width/9*8, height/9), 
                                            (width/9, height/9*8), 10)
    if winner == None:
        if all([all(row) for row in TTT]):
            draw = True
    draw_status()


def draw_status():
    global draw, m_color, message

    if winner is None:
        message = XO.upper() + "'s Turn"
        if XO == 'x':                  
            m_color = rose
        else:
            m_color = blue
    else:
        message = winner.upper() + " won!"
        m_color = yellow
        
    if draw:
        message = 'Game Draw!'
        m_color = yellow
    
    status_button = Button((0, height, width+extra_height, extra_height), gray, m_color, message)
    status_button.draw_button()


def copy_XO():
    for x in range(3):
        for y in range(3):
            if TTT[x][y] is None:
                continue
            else:
                set_position(x+1, y+1)
                if(TTT[x][y] == 'x'):
                    game_screen.blit(x_img,(posx, posy))                               
                else:
                    game_screen.blit(o_img,(posx, posy))
  
               
def reset_game():
    global TTT, winner, XO, draw, start_button
    time.sleep(2)
    XO = 'x'
    draw = False
    winner = None  
    start_button = False   
    TTT = [[None]*3,[None]*3,[None]*3]
    game_opening()
 

game_opening()

# run the main loop
while(True):    
    for action in pg.event.get():   
        if action.type == QUIT:
            pg.quit()
            sys.exit()

        elif action.type == pg.VIDEORESIZE:
            if action.w < 300:
                action.w = 300
            if action.h < 300:
                action.h = 300                               
            game_screen = pg.display.set_mode((action.w, action.h), pg.RESIZABLE)      
            width = action.w
            extra_height = action.h/5
            height = action.h - extra_height
            if start_button:
                grid()
                copy_XO()
            else:
                game_opening()
            pg.display.update()
            CLOCK.tick(fps)  
           
        elif action.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O  
            if start_button == False:        
                userClick()               
                if start_button:            
                    grid()
                else: continue
            userClick()
            turn_sound.play_sound()
            if winner:
                win_sound.play_sound()
                reset_game()              
            elif draw:
                draw_sound.play_sound()
                reset_game()
             

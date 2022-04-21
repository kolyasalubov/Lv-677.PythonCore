import pygame
import random

FPS = 60

#resolution
WIDTH_DISPLAY=670 #670
HEIGHT_DISPLAY=600 #600

#color
LIGHT_BEIGE = (245, 245, 220)
BEIGE = (205, 205, 185)
ORANGE = (255, 153, 51)
DARK_GREY = (40,40,40)
LIGHT_GREY = (120, 120, 120)
GREEN = (64,169,64)
LIGHT_GREEN = (100,150,100)
RED = (200, 70, 50)

#main var

numa_try = 5 #кількість спроб


alphabets = None
word_list = []
keys_log = []
checks = False


#initing obj
pygame.init()
pygame.font.init()

#font


#setting graph
gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("Wordl")
clock = pygame.time.Clock()

#-----------------------------------------------------


def import_word():
    """Import word from file"""
    global alphabets
    file = open("MyGame/words.txt", encoding = 'utf-8')
    for line in file:
        if line.startswith("|"):
            alphabets = line.removeprefix("|").removesuffix("\n")
        else:
            word_list.append(line.removesuffix("\n"))
    file.close()

def rolling_word():
    """Randomize word for game"""
    global word, word_char, numa_char
    word = random.choice(word_list)
    word_char = list(word.upper())
    numa_char = len(word_char)
    print(word)

def iterator():
    global row_ite, itr
    iters = list({x for x in range(numa_char)})
    row_ite = iter(iters)
    itr = 0

def clearing_var():
    """Clearing variables"""
    global field, missmatch_char, hits_char, matched_char, key
    field = []
    key = []
    missmatch_char = set()
    hits_char = set()
    matched_char = set()



class Button:
   

    def __init__(self, text = "None", 
                        pos =  (0, 0),
                        bg = BEIGE, 
                        width_height = (50, 60), 
                        event = "Keyboard", 
                        font = "None", 
                        size_font = 48):
        
        self.x, self.y = pos
        self.bg_color = bg
        self.char = text
        self.width, self.height = width_height
        self.event = event 
        self.font = pygame.font.SysFont(font, size_font)
        self.change_text(text)
    def change_text(self, text):
        self.text = self.font.render(text, 1, DARK_GREY)
        self.text_rect = self.text.get_rect(center=(self.x+self.width //2, self.y+ self.height //2))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def show(self):
        pygame.draw.rect(gameDisplay, self.bg_color, [self.x, self.y, self.width, self.height])
        gameDisplay.blit(self.text, self.text_rect)

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if self.event == "Keyboard":
                        KeyEvent.key_input(self.char.upper())
                    elif self.event == "Clear":
                        KeyEvent.clear()
                    elif self.event == "Erase":
                        KeyEvent.erase()
                    elif self.event == "Check":
                        KeyEvent.check()


class KeyEvent:

    def key_input(char):
        keys_log.append(char)

    def clear():
        global checks
        checks = False
        keys_log.clear()
    
    def erase():
        global checks
        if len(keys_log) != 0: 
            checks = False
            keys_log.pop()

    def check():
        global checks
        if len(keys_log) == numa_char:
            checks = True


class Keyboard:

    def create():
        global key
        for i in range(len(alphabets)):
            key.append(Button())

    def show():
        for i in range(len(alphabets)):
            key[i].show()

    def update(space = 10,
                key_w = 30, 
                key_h = 40):
        global key

        numa_key = gameDisplay.get_width() // (key_w + space + 1)
        key_y = gameDisplay.get_height()
        
        for i in range(len(alphabets)):
            if i % numa_key != 0:
                key_x += key_w + space
            elif (len(alphabets)-i) < 8:
                key_x = (gameDisplay.get_width() / (key_w + space/2) - (len(alphabets)-i)) * key_w / 2 #- key_w
                key_y -= (key_h + space)
            elif (len(alphabets)-i) < (numa_key): 
                #key_x = gameDisplay.get_width() / (len(alphabets)-i) + key_w/2
                key_x = (gameDisplay.get_width() / (key_w + space/2) - (len(alphabets)-i)) * key_w / 2 - key_w
                key_y -= (key_h + space)
            else:
                key_x = gameDisplay.get_width() / numa_key - key_w / 2
                key_y -= (key_h + space)


            color_key = BEIGE

            for char in hits_char:
                if alphabets[i].upper() == char:
                    color_key = ORANGE

            for char in matched_char:
                if alphabets[i].upper() == char:
                    color_key = GREEN

            for char in missmatch_char:
                if alphabets[i].upper() == char:
                    color_key = LIGHT_GREY

                
            key[i] = Button(alphabets[i], (key_x, key_y), color_key, (key_w, key_h))


class AdditionalButton():

    def create():
        global clear_button
        global check_button
        global erase_button

        clear_button = Button("Clr",(10,10), RED, (60, 60), "Clear")
        erase_button = Button("Erase",(80,10), ORANGE, (100, 60), "Erase")
        check_button = Button("Check",((gameDisplay.get_width()-170),10), GREEN, (160, 60), "Check")

    def show():
        clear_button.show()
        check_button.show()
        erase_button.show()

    def update():
        global check_button
        check_button = Button("Check",((gameDisplay.get_width()-170),10), GREEN, (160, 60), "Check")


class Checking:

    #Добавити функцію для перевірки наявності слова в словнику

    def check_char():
        global hits_char
        global missmatch_char
        global matched_char
        
        if checks == True:
            for char in keys_log:
                for i in range(numa_char):
                    
                    if char == word_char[i]:
                        hits_char.add(char)

                    elif keys_log[i] == word_char[i]:
                        matched_char.add(keys_log[i])

                    else:
                        missmatch_char.add(keys_log[i])
                        missmatch_char = missmatch_char.difference(hits_char)

    
    def check_word():
        game_word = "".join(keys_log)
        if game_word == word.upper() and checks == True:
            return True

    def check_char_i(i, wrd, another_check = False):
        if  checks == True or another_check == True:
            for j in range(numa_char):
                if wrd[i] == word_char[j]:
                    return True
    def check_word_i(i, wrd, another_check = False):
        if checks == True or another_check == True:
            if wrd[i] == word_char[i]:
                return True

class VisualWord():

    def __init__(self, 
                char_h = 60, 
                char_w = 40, 
                space = 10, 
                char_y = 100,
                row = 1):
        
        self.h = char_h
        self.w = char_w
        self.space = space
        self.row = row
        self.y = char_y + (self.h + self.space) * self.row
        self.x = (gameDisplay.get_width() / self.w - numa_char) * self.w / 2 - self.w/2
        self.font = pygame.font.SysFont(None, 48)
        self.frozen = False
        self.check = False        

    def create_frame(self):
        for i in range(numa_char):
            for j in range(numa_try):
                self.x = (gameDisplay.get_width() / self.w - numa_char) * self.w / 2 - self.w/2
                pygame.draw.rect(gameDisplay, BEIGE, [self.x+i*(self.w+10), self.y + j*(self.h + self.space), self.w, self.h])
    
    def show(self):
        self.x = (gameDisplay.get_width() / self.w - numa_char) * self.w / 2 - self.w/2
        if checks == True and self.frozen == False:
            self.word = "".join(keys_log)
            self.frozen = True
            self.check = True
        elif self.frozen != True:
            self.word = keys_log


        for i in range(len(self.word)):   
            if Checking.check_word_i(i, self.word, self.check) == True:
                cell_color = GREEN
            elif Checking.check_char_i(i, self.word, self.check) == True:
                cell_color = ORANGE
            else: cell_color = BEIGE

            pygame.draw.rect(gameDisplay, cell_color, [self.x+i*(self.w+10), self.y, self.w, self.h])

            text = self.font.render(self.word[i], 1, DARK_GREY)
            text_rect = text.get_rect(center=(self.x+i*(self.w+10) + self.w //2, self.y + self.h //2))
            gameDisplay.blit(text, text_rect)

    
    def get_frozen(self):
        return self.frozen


class Fields:

    def create():
        for i in range(numa_try):
            field.append(VisualWord(row = i))
            

    def show():
        global keys_log
        global checks, lose
        global itr
        for i in range(itr):
            field[i].show()
        field[itr].show()
        if field[itr].get_frozen() == True:
            checks = False
            keys_log.clear()
            try: itr = next(row_ite)
            except: lose = True
           
            
def new_game():
    clearing_var()
    import_word()
    rolling_word()
    iterator()


def mainloop():
    global keys_log
    global checks, lose
    global play
    run = True
    lose = False
    Keyboard.create()
    AdditionalButton.create()
    Fields.create()
    while run:
        pygame.time.delay(100)
        #Event
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                play = False
            elif event.type == pygame.KEYDOWN:
                # get pressed key
                if event.key == 8:
                    KeyEvent.erase()
                elif event.key == 13:
                    KeyEvent.check()
                elif len(keys_log) < numa_char and event.unicode != '' and event.unicode.lower() in alphabets.lower():
                    checks = False
                    KeyEvent.key_input(event.unicode.upper())
                else: checks = False
            elif len(keys_log) < numa_char:
                for i in range(len(alphabets)):
                    key[i].click(event)
            clear_button.click(event)
            check_button.click(event)
            erase_button.click(event)

        #Game


        Checking.check_char()
        gameDisplay.fill(LIGHT_BEIGE) 
        field[0].create_frame()
        Keyboard.update()
        AdditionalButton.update()
        Keyboard.show()
        AdditionalButton.show()

        if Checking.check_word():
            gameDisplay.fill(LIGHT_GREEN)
            run = False
        elif lose:
            gameDisplay.fill(RED)
            run = False


        Fields.show()

        pygame.display.update()
        clock.tick(FPS)

play = True
score = 0
while play:
    new_game()
    mainloop()
    if lose:
        score -= 1
    else:
        score += 1
    last_word = word
    pygame.display.set_caption(f"Wordl SCORE: {score}  Last word: {last_word}")

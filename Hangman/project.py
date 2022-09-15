import pygame
import math
import random

#set up display
pygame.init()
WIDTH, HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman!')

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH- (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

#fonts 
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont("comicsans", 40)
TITLE_FONT = pygame.font.SysFont("comicsans", 50)
BG = pygame.image.load('hangman0.png')
SCORE_FONT = pygame.font.SysFont('comicsans', 10)

#Load Images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#game variables
hangman_status = 0
words = ['TODAY', "TOMORROW", 'NEVER', "HELLO", "BEAT", 'NEW', "CODING", "OOPS", "HELP", 'PANCAKES', "SUZY", "BIRDBATH", "DEXTER", "FOREST", "CRITICAL", "LUNCHBOX"]
word = random.choice(words)
guessed = []




#colors
SILVER= (170,169,173)
BLACK = (0,0,0)


def draw():
    win.fill(SILVER)
    wins = 0
    losses = 0

    #draw title
    text = TITLE_FONT.render("DO NOT HANG THIS MAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/ 2, 20))

    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400,200))

    #wins and losses counter
    wins_label = SCORE_FONT.render(f'Wins: {wins}', 1, (BLACK))
    loss_label = SCORE_FONT.render(f'Losses: {losses}', 1, (BLACK))

    win.blit(wins_label, (10,10))
    win.blit(loss_label, (WIDTH - loss_label.get_width()- 10,10))

    #draw buttons
    for letter in letters:
        x  , y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150,100))
    pygame.display.update()
    
def reset_game():
    global hangman_status
    global word
    global guessed
    global letters
    global i
    global x
    global y
    hangman_status = 0
    word = random.choice(words)
    guessed = []
    letters = []
    for i in range(26):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])



def display_message(message):
    pygame.time.delay(1000)
    win.fill(SILVER)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1500)

def main():
    global hangman_status
    losses = 0
    wins = 0

    FPS = 60
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS :
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
                draw()

            won = True
            for letter in word:
                if letter not in guessed:
                    won = False
                    break           
        
            if won:
                display_message("You Won!")
                if display_message("You Won!") is True:
                    wins += 1
                reset_game()
                main_menu()

            if hangman_status == 6:              
                display_message('You lost, your word was....')
                display_message(word)
                losses += 1
                reset_game()
                main_menu()        
    
    
        
    
def main_menu():
    play_game = True
    while play_game:
        win.fill(SILVER)
        text = TITLE_FONT.render("Click the Mouse Button to Play", 1, BLACK)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
main_menu()






    


    




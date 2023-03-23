import pygame
import random

pygame.init()
windowHeight = 480
windowWidth = 700
window=pygame.display.set_mode((windowWidth,windowHeight))

# Global variables
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
guessed = []

hangmanPics = [pygame.image.load('assets/hangman0.png'), 
               pygame.image.load('assets/hangman1.png'), 
               pygame.image.load('assets/hangman2.png'), 
               pygame.image.load('assets/hangman3.png'), 
               pygame.image.load('assets/hangman4.png'), 
               pygame.image.load('assets/hangman5.png'),
               pygame.image.load('assets/hangman6.png')]

limbs = 0


def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    window.fill(GREEN)
    
    # Buttons 
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(window, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(window, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            window.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    window.blit(label1,(windowWidth/2 - length/2, 400))

    pic = hangmanPics[limbs]
    window.blit(pic, (windowWidth/2 - pic.get_width()/2 + 20, 150))
    pygame.display.update()


def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
            

def buttonHit(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None


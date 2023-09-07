
#Benötigte Module importieren
import pygame
import random

pygame.init()

#Fenstergröße festlegen
width = 800
height = 600

#Fenster erstellen
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

#Farben festlegen
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#Tetrominos
Tetrominos = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[2, 2, 0],
     [0, 2, 2]],

    [[3, 0, 0],
     [3, 3, 3]],

    [[4, 4, 4],
     [4, 0, 0]],

    [[0, 5, 5],
     [5, 5, 0]],

    [[6, 6, 6],
     [0, 0, 6]],

    [[7, 7],
     [7, 7]]
]

#Aktueller Tetromino
current_tetromino = []

#Position des aktuellen Tetrominos
current_x_pos = 0
current_y_pos = 0

#Nächster Tetromino
next_tetromino = []

#Bildschirm auffüllen
def draw_grid():
    for x in range(width // 10):
        for y in range(height // 10):
            rect = (x*10, y*10, 10, 10)
            pygame.draw.rect(win, gray, rect, 1)

#Tetromino anzeigen
def draw_tetromino(tetromino, x, y):
    color = (white, red, green, blue, yellow)
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            rect = (x + j*10, y + i*10, 10, 10)
            if tetromino[i][j] != 0:
                pygame.draw.rect(win, color[tetromino[i][j] - 1], rect)

#Neuen Tetromino erstellen
def new_tetromino():
    global current_tetromino, next_tetromino, current_x_pos, current_y_pos
    current_tetromino = next_tetromino
    next_tetromino = random.choice(Tetrominos)
    current_x_pos = 4
    current_y_pos = 0

#Neuen Tetromino erstellen
new_tetromino()

#Spiel läuft
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and current_x_pos > 0:
        current_x_pos -= 1
    if keys[pygame.K_RIGHT] and current_x_pos < 10 - len(current_tetromino[0]):
        current_x_pos += 1
    if keys[pygame.K_DOWN] and current_y_pos < 20 - len(current_tetromino):
        current_y_pos += 1
    if keys[pygame.K_UP]:
        new_tetromino()

    #Bildschirm leeren
    win.fill(black)

    #Grid anzeigen
    draw_grid()

    #Tetromino anzeigen
    draw_tetromino(current_tetromino, current_x_pos * 10, current_y_pos * 10)
    draw_tetromino(next_tetromino, 500, 200)

    #Bildschirm aktualisieren
    pygame.display.update()

#Beenden
pygame.quit()
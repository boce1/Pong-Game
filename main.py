from utils import *
from player import p1, p2
from ball import ball
import pygame

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Pong Game")
window = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Consolas", 60)

def main(win):
    #window.fill(BLACK)
    window.blit(background, (0, 0))
    p1.show(win)
    p2.show(win)
    ball.show(win)
    ball.end_scene(win)
    pygame.display.update()

clock = pygame.time.Clock()

main_screen_message = font.render("Press any key to start a game", True, WHITE)
def start_message(win, mes):
    win.blit(background_main_menu, (0, 0))
    win.blit(mes, (WIDTH // 2 - mes.get_width() // 2, HEIGHT // 2 - mes.get_height() // 2))
    pygame.display.update()

up = True
x = WIDTH // 2 - main_screen_message.get_width() // 2
y = HEIGHT // 2 - main_screen_message.get_height() // 2
center_y = HEIGHT // 2 - main_screen_message.get_height() // 2
speed = 0.5
def main_menu(win, mes):
    global main_screen, run, up, y
    while main_screen:
        #start_message(win, mes)
        if up:
            y -= speed
        if y <= center_y - 25git :
            up = False
        if not up:
            y += speed
        if y >= center_y + 25git :
            up = True
        win.blit(background_main_menu, (0, 0))
        win.blit(mes, (x, y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_screen = False
                run = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                main_screen = False
        continue

run = True
main_screen = True
pygame.mixer.music.load("music\Digestive biscuit.wav")
pygame.mixer.music.play(-1)
while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    main_menu(window, main_screen_message)

    p1.move(keys)
    p2.move(keys)
    ball.win_situation(window, keys)
    main(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
pygame.quit()
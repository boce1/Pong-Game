from utils import *
from player import p1, p2
from ball import ball
import pygame

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Pong Game")
window = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Consolas", 60)
font2 = pygame.font.SysFont("Consolas", 20)

pause_message = font.render("Pause", True, WHITE)
def main(win, pause_index):
    #window.fill(BLACK)
    window.blit(background, (0, 0))
    p1.show(win)
    p2.show(win)
    ball.show(win)
    ball.end_scene(win)
    if pause_index == 1:
        win.blit(pause_message, (WIDTH // 2 - pause_message.get_width() // 2, pause_message.get_height() // 2))
    pygame.display.update()

clock = pygame.time.Clock()

main_screen_message = font.render("Press any key to start a game", True, WHITE)

up = True
x = WIDTH // 2 - main_screen_message.get_width() // 2
y = HEIGHT // 2 - main_screen_message.get_height() // 2
center_y = HEIGHT // 2 - main_screen_message.get_height() // 2
speed = 0.5
controls_message = font2.render("Player1: up-\"W\", down-\"S\"||Player2: up-\"up arrow\", down-\"down arrow\"||pause - \"P\"", True, WHITE)
controls_message_x = WIDTH // 2 - controls_message.get_width() // 2
controls_message_y = HEIGHT - controls_message.get_height()
def main_menu(win):
    global main_screen, run, up, y
    while main_screen:
        if up:
            y -= speed
        if y <= center_y - 25:
            up = False
        if not up:
            y += speed
        if y >= center_y + 25:
            up = True
        win.blit(background_main_menu, (0, 0))
        win.blit(main_screen_message, (x, y))
        win.blit(controls_message, (controls_message_x, controls_message_y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_screen = False
                run = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                main_screen = False
        continue

pause_index = 0
p1_speed = (p1.speed, 0)
p2_speed = (p2.speed, 0)
ball_speed = [ball.vel, 0]

def pause_game(event):
    global pause_index, prev_ball_vel
    if not main_screen:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if ball.vel != 0: #and not (ball.overlap_p1() or ball.overlap_p2()):
                    prev_ball_vel = ball.vel
                    ball_speed[0] = prev_ball_vel
                    #ball_speed[0] = ball.prev_vel
                if not ball.win:
                    pause_index += 1
                if pause_index > 1:
                    pause_index = 0
                p1.speed = p1_speed[pause_index]
                p2.speed = p2_speed[pause_index]
                ball.vel = ball_speed[pause_index] 

run = True
main_screen = True
pygame.mixer.music.load("music\Digestive biscuit.wav")
pygame.mixer.music.play(-1)
while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    main_menu(window)

    p1.move(keys)
    p2.move(keys)
    ball.win_situation(keys, pause_index)
    main(window, pause_index)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pause_game(event)    

pygame.quit()

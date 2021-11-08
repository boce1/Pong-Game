from math import radians, sin, cos
from random import randint, choice
import pygame
from player import p1, p2
from utils import WIDTH, HEIGHT, ball_pic, WHITE, BLACK

pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont("Consolas", 50)
boing_sound = pygame.mixer.Sound(".\\music\\Boing.wav")

masks = (pygame.mask.from_surface(p1.pic), pygame.mask.from_surface(p2.pic))

players = (p1, p2)

angles = []
angles_p1 = []
angles_p2 = []
for i in range(-45, 46):
    angles.append(i)
    angles_p1.append(i)
for i in range(135, 226):
    angles.append(i)
    angles_p2.append(i)

class Ball:
    def __init__(self):
        self.pic = ball_pic
        self.mask = pygame.mask.from_surface(self.pic)
        self.width = self.pic.get_width()
        self.height = self.pic.get_height()
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT // 2 - self.height // 2
        self.vel = 10
        self.prev_vel = self.vel
        self.max_speed = 25
        self.angle = choice(angles)
        self.radians_angle = radians(self.angle)
        self.right = True
        self.up = True
        self.interacted_with_player1 = 0
        self.interacted_with_player2 = 0
        self.player1_score = 0
        self.player2_score = 0
        self.win = False

    def track_score(self):
        if self.x < -self.width:
            self.player2_score += 1
        if self.x > WIDTH:
            self.player1_score += 1
        
    def show_score(self, win):
        self.track_score()
        score_p1 = font.render(f"{self.player1_score}", True, WHITE)
        score_p2 = font.render(f"{self.player2_score}", True, WHITE)
        gap = 10
        win.blit(score_p1, (gap, gap))
        win.blit(score_p2, (WIDTH - gap - score_p2.get_width(), gap))

    def is_off_screen(self):
        if self.x < -self.width or self.x > WIDTH:
            self.x = WIDTH // 2 - self.width // 2
            self.y = HEIGHT // 2 - self.height // 2
            self.vel = 10
            self.interacted_with_player1 = 0
            self.interacted_with_player2 = 0
            self.angle = choice(angles)
            self.radians_angle = radians(self.angle)

    def is_wall_touched(self):
        return self.y <= 0 or self.y >= HEIGHT - self.height

    def overlap_p1(self):
        offset_x_p1 = p1.x - self.x
        offset_y_p1 = p1.y - self.y
        overlap_p1 = self.mask.overlap(masks[0], (int(offset_x_p1), int(offset_y_p1)))
        return overlap_p1 

    def overlap_p2(self):
        offset_x_p2 = p2.x - self.x
        offset_y_p2 = p2.y - self.y
        overlap_p2 = self.mask.overlap(masks[1], (int(offset_x_p2), int(offset_y_p2)))
        return overlap_p2

    def bounce(self):
        if self.interacted_with_player1 == 1 or self.interacted_with_player2 == 1:
            self.right = not self.right
            self.vel += 0.5
            self.vel = min(self.max_speed, self.vel)

    def change_angle(self, player_num):
        if player_num == 1:
            self.angle = choice(angles_p1)
        else:
            self.angle = choice(angles_p2)
        self.radians_angle = radians(self.angle)

    def move(self):
        self.is_off_screen()
        #self.prev_vel = self.vel
        if self.overlap_p1():
            self.bounce()
            self.interacted_with_player2 = 0
            self.interacted_with_player1 += 1
            if self.interacted_with_player1 == 1:
                self.change_angle(1)
                pygame.mixer.Sound.play(boing_sound)

        if self.overlap_p2():
            self.bounce()
            self.interacted_with_player1 = 0
            self.interacted_with_player2 += 1
            if self.interacted_with_player2 == 1:
                self.change_angle(2)
                pygame.mixer.Sound.play(boing_sound)


        if self.is_wall_touched():
            self.up = not self.up

        if self.right:        
            change_x = cos(self.radians_angle) * self.vel
        else:
            change_x = -cos(self.radians_angle) * self.vel

        if self.up:
            change_y = sin(self.radians_angle) * self.vel
        else:
            change_y = -sin(self.radians_angle) * self.vel
    
        self.x += change_x
        self.y += change_y 

    def end_scene(self, win):
        if self.player1_score >= 10 or self.player2_score >= 10:
            if self.player1_score > self.player2_score:
                message = font.render("Player 1 won!", True, WHITE)
            else:
                message = font.render("Player 2 won!", True, WHITE)
            win.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(1000)
            self.player1_score = 0
            self.player2_score = 0
            self.win = True

    def win_situation(self, keys, pause_index):
        if self.win:
            self.vel = 0
        if keys[pygame.K_SPACE] and pause_index == 0:
            self.win = False
            self.vel = 10

    def show(self, win):
        if self.win:
            #if pause_index == 0:
            message = font.render("Press SPACE to continue playing", True, WHITE)
            win.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
            pygame.display.update()
            #else:

        else:
            self.move()
            win.blit(self.pic, (self.x, self.y))
            self.show_score(win)

ball = Ball()
from utils import WIDTH, HEIGHT, p1_pic, p2_pic
import pygame

class Player:
    def __init__(self, x, num, pic):
        self.x = x
        self.num = num
        self.pic = pic
        self.width = self.pic.get_width()
        self.height = self.pic.get_height()
        self.y = HEIGHT // 2 - self.height // 2
        self.speed = 10
        self.controls = ((pygame.K_w, pygame.K_s), (pygame.K_UP, pygame.K_DOWN))

    def move(self, keys):
        if self.y > 0:
            if keys[self.controls[self.num - 1][0]]:
                self.y -= self.speed

        if self.y < HEIGHT - self.height:
            if keys[self.controls[self.num - 1][1]]:
                self.y += self.speed             

    def show(self, win):
        win.blit(self.pic, (self.x, self.y))

p1_x = 10
p2_x = WIDTH - p2_pic.get_width() - p1_x

p1 = Player(p1_x, 1, p1_pic)
p2 = Player(p2_x, 2, p2_pic) 
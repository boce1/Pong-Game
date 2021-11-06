import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

p1_pic = pygame.image.load(".\\imgs\\p1.png")
p2_pic = pygame.image.load(".\\imgs\\p2.png")
ball_pic = pygame.image.load(".\\imgs\\ball.png")
background = pygame.image.load(".\\imgs\\background.jpg")
background_main_menu = pygame.image.load(".\\imgs\\main_menu.png")

WIDTH = background.get_width()
HEIGHT = background.get_height()

FPS = 60

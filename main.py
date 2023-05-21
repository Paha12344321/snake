import pygame
import time
import random

pygame.init()

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

title = "Snake"
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

clock = pygame.time.Clock()

segment_size = 20
font_size = 30

def display_message(message):
    font = pygame.font.Font("freesansbold.ttf", font_size)
    text_surface = font.render(message, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (width / 2, height / 2)
    window.blit(text_surface, text_rect)
    pygame.display.flip()
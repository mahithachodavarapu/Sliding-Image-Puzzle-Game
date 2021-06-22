import pygame

pygame.init()
WIDTH = HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 14)


def write(text, x, y, color="Coral",):
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(WIDTH//2, y))
    return text, text_rect

text, text_rect = write("Hello", 10, 10) 
loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
    screen.blit(text, text_rect)
    pygame.display.update()

pygame.quit()
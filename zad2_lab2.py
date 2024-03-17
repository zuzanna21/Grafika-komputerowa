import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill("white")
    polygon_surface = pygame.Surface((600, 600), pygame.SRCALPHA)
    triangle_surface = pygame.Surface((600, 600), pygame.SRCALPHA)

    w = 100
    x,y=300,300
   
    def draw_square(surface,color, x, y, side_length):
        pygame.draw.rect(surface, color, (x, y, side_length, side_length), 0)

    def draw_triangle(surface,color, x, y, w):
        pygame.draw.polygon(surface, color, ((x-(w/2), y - (w+w/2)), (x+(w/2), y-(w + w/2)), (x, y-(w/2))), 0)

    draw_square(polygon_surface,NIEBIESKI, 300, 250, 100)
    scaled_rectangle = pygame.transform.scale_by(polygon_surface, (2, 1))
    rect = scaled_rectangle.get_rect(center=(200, 300))
    win.blit(scaled_rectangle, rect)
  
    draw_triangle(triangle_surface,NIEBIESKI, x, y, w)
    fliped_triangle = pygame.transform.flip(triangle_surface, 1, 0)
    triangle = fliped_triangle.get_rect(center=(300, 300))
    win.blit(fliped_triangle, triangle)
    
    draw_triangle(triangle_surface,NIEBIESKI, x, y, w)
    fliped_triangle = pygame.transform.flip(triangle_surface, 0, 1)
    triangle2 = fliped_triangle.get_rect(center=(300, 300))
    win.blit(fliped_triangle, triangle2)
   
    pygame.display.update()

    """
    # rysowanie kwadratów
    pygame.draw.rect(win, CZERWONY , (10, 30, 100, 100))
    pygame.draw.rect(win, ZOLTY, (160, 30, 100, 100))
    pygame.draw.rect(win, ZIELONY, (310, 30, 100, 100))
    # rysowanie kół
    pygame.draw.circle(win, FIOLETOWY, (60, 200), 50, 0)
    pygame.draw.circle(win, JASNY_NIEBIESKI, (210, 200), 50, 25)
    pygame.draw.circle(win, POMARANCZOWY, (360, 200), 50, 5)
    # linia pozioma
    pygame.draw.line(win, NIEBIESKI, (10, 325), (110, 325), 15)
    # linia pionowa
    pygame.draw.line(win, SZARY, (210, 275), (210, 375), 5)
    # rysowanie plusa
    pygame.draw.line(win, NIEBIESKI, (310, 325), (410, 325), 10)
    pygame.draw.line(win, SZARY, (360, 275), (360, 375), 10)
    # wypisywanie tekstu
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Tekst do wyświetlania ', 1, (255, 255, 255))
    win.blit(label, (100, 425))
    """
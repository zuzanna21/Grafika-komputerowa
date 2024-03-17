import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Septagon")

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
    pygame.draw.rect(win, ZOLTY , (10, 45, 580, 545))
    font = pygame.font.SysFont('bitstreamverasans', 30)
    septagon_surface = pygame.Surface((400, 400), pygame.SRCALPHA)

    def draw_septagon(surface, color, center, size): #funkcja rysujaca siedmiokat
        angle = 360 / 7 #pojedynczy kat
        coordinates = []
        for i in range(7):
            x = center[0] + size * math.cos(math.radians(i * angle))
            y = center[1] + size * math.sin(math.radians(i * angle))
            coordinates.append((x, y))
        pygame.draw.polygon(surface, color, coordinates, 0)

    def shear_septagon(surface, color, center, size, shear_amount_x, shear_amount_y):
        n = 7
        angle = 360 / n
        coordinates = []
        for i in range(n):
            x = center[0] + size * math.cos(math.radians(i * angle))
            y = center[1] + size * math.sin(math.radians(i * angle))
            x_sheared = x + shear_amount_x * (y - center[1]) / size
            y_sheared = y + shear_amount_y * (x - center[0]) / size
            coordinates.append((x_sheared, y_sheared))
        pygame.draw.polygon(surface, color, coordinates, 0)



    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        label = font.render('1.', 1, (0, 0, 0))
        win.blit(label, (10, 10))

        draw_septagon(win,NIEBIESKI, (300, 300), 100)
        
    if keys[pygame.K_2]:
        label = font.render('2.', 1, (0, 0, 0))
        win.blit(label, (10, 10))

        draw_septagon(septagon_surface, NIEBIESKI, (200, 200), 100) 

        rotated_septagon = pygame.transform.rotozoom(septagon_surface, 45, 2)
        rect = rotated_septagon.get_rect(center=(300, 300))
        win.blit(rotated_septagon, rect)

    if keys[pygame.K_3]:

        label = font.render('3.', 1, (0, 0, 0))
        win.blit(label, (10, 10)) 

        draw_septagon(septagon_surface, NIEBIESKI, (200, 200), 100)

        flipped_septagon = pygame.transform.flip(septagon_surface, flip_x=1, flip_y=0)
        rect = flipped_septagon.get_rect(center=(300, 300))
       
        scaled_septagon = pygame.transform.scale_by(flipped_septagon, (0.5, 2))
        rect = scaled_septagon.get_rect(center=(300, 300))
        win.blit(scaled_septagon, rect)

    if keys[pygame.K_4]:
        label = font.render('4.', 1, (0, 0, 0))
        win.blit(label, (10, 10))

        shear_amount_x = 20.0
        shear_amount_y = 20.0
        shear_septagon(win, NIEBIESKI, (300, 300), 100, shear_amount_x, shear_amount_y)
    
    if keys[pygame.K_5]:
        label = font.render('5.', 1, (0, 0, 0))
        win.blit(label, (10, 10))
        draw_septagon(septagon_surface, NIEBIESKI, (200, 200), 100)
        scaled_septagon = pygame.transform.scale_by(septagon_surface, (2, 0.5))
        rect = scaled_septagon.get_rect(center=(300, 100))
        win.blit(scaled_septagon, rect)

    if keys[pygame.K_6]:
        label = font.render('6.', 1, (0, 0, 0))
        win.blit(label, (10, 10))

        shear_amount_x = 20.0
        shear_amount_y = 20.0
        shear_septagon(septagon_surface, NIEBIESKI, (300, 300), 100, shear_amount_x, shear_amount_y)

        rotated_septagon2 = pygame.transform.rotate(septagon_surface, 90)
        rect = rotated_septagon2.get_rect(center=(200, 400))
        win.blit(rotated_septagon2, rect)
    
    if keys[pygame.K_7]:
        label = font.render('7.', 1, (0, 0, 0))
        win.blit(label, (10, 10))

        draw_septagon(septagon_surface, NIEBIESKI, (200, 200), 100)

        flipped_septagon = pygame.transform.flip(septagon_surface, 0, 1)
        rect = flipped_septagon.get_rect(center=(300, 300))
       
        scaled_septagon = pygame.transform.scale_by(flipped_septagon, (0.5, 2))
        rect = scaled_septagon.get_rect(center=(300, 300))
        win.blit(scaled_septagon, rect)
    
    if keys[pygame.K_8]:
        label = font.render('8.', 1, (0, 0, 0))
        win.blit(label, (10, 10))

        draw_septagon(septagon_surface, NIEBIESKI, (200, 200), 100)

        scaled_septagon = pygame.transform.scale_by(septagon_surface, (2, 0.5))
        rect = scaled_septagon.get_rect(center=(300, 100))
        
        rotated_septagon = pygame.transform.rotate(scaled_septagon, -45)
        rect = rotated_septagon.get_rect(center=(300, 400))
        win.blit(rotated_septagon, rect) 

    if keys[pygame.K_9]:
        label = font.render('9.', 1, (0, 0, 0))
        win.blit(label, (10, 10))

        shear_amount_x = 20.0
        shear_amount_y = 20.0
        shear_septagon(septagon_surface, NIEBIESKI, (300, 300), 100, shear_amount_x, shear_amount_y)
        
        rotated_septagon = pygame.transform.rotate(septagon_surface, -30)
        rect = rotated_septagon.get_rect(center=(470, 100))
        win.blit(rotated_septagon, rect) 

    pygame.display.update()

    # rysowanie kwadratów
    #pygame.draw.rect(win, CZERWONY , (10, 30, 100, 100))
    #pygame.draw.rect(win, ZOLTY, (160, 30, 100, 100))
    #pygame.draw.rect(win, ZIELONY, (310, 30, 100, 100))
    # rysowanie kół
    #pygame.draw.circle(win, FIOLETOWY, (60, 200), 50, 0)
    #pygame.draw.circle(win, JASNY_NIEBIESKI, (210, 200), 50, 25)
    #pygame.draw.circle(win, POMARANCZOWY, (360, 200), 50, 5)
    # linia pozioma
    #pygame.draw.line(win, NIEBIESKI, (10, 325), (110, 325), 15)
    # linia pionowa
    #pygame.draw.line(win, SZARY, (210, 275), (210, 375), 5)
    # rysowanie plusa
    #pygame.draw.line(win, NIEBIESKI, (310, 325), (410, 325), 10)
    #pygame.draw.line(win, SZARY, (360, 275), (360, 375), 10)
    # wypisywanie tekstu
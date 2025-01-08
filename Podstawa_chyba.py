import pygame
import sys
import random

pygame.init()


screen = pygame.display.set_mode((800, 600))  # Okno o rozdzielczości 800x600
pygame.display.set_caption("Kwadrat w Pygame")  

# Kolory
WHITE = (255, 255, 255)  # Biały
BLACK = (0,0,0) #czarny
RED = (255, 0, 0)  # Czerwony
high=20
random_gap= random.randint(10, 350)   #500 max odleglosc, wykorzystamy też do policzenia przesunięcia
random_size= random.randint(40,140)


clock = pygame.time.Clock()
# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # TŁO
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLACK, (0, 500, 100,450)) #blok startowy
    pygame.draw.rect(screen, BLACK, (100+random_gap, 500, random_size,450)) #blok drugi
    
    
   
    pygame.draw.rect(screen, RED, (80, 500-high, 20,high))  #(x, y,szerokosc,wysokosc)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: #nacisniecie spacji
            
             high=high+5
   

    if high>random_gap:
        if high<random_gap+random_size:
            print("wygrana")
        else:
            print("Przegrana")
    else:
        print("Przegrana")
    # Odświeżenie ekranu
    pygame.display.flip()
    clock.tick(60)

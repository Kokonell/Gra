import pygame
import sys
import random

pygame.init()

# Ustawienia ekranu
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kwadrat w Pygame")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Czcionka
font = pygame.font.Font(None, 36)

# Zmienna wysokości skoku
high = 20

# Funkcja do rysowania platformy
def platform():
    random_gap = random.randint(10, 350)
    random_size = random.randint(40, 140)
    return random_size, random_gap

# Funkcja do rysowania przycisku
def draw_button(screen, text, x, y, width, height, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0]:  # Kliknięcie lewego przycisku myszy
            return True
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

    return False

# Zmienne stanu gry
gen = 1
gen_next = 1
st = 0  # 0: ekran początkowy, 1: gra
random_size, random_gap = 0, 0  # Platforma
clock = pygame.time.Clock()

# Pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ekran początkowy
    if st == 0:
        screen.fill(WHITE)
        if draw_button(screen, "Start", 350, 250, 100, 50, WHITE, BLACK):
            st = 1  # Zmieniamy stan na grę
            random_size, random_gap = platform()  # Generujemy platformę po kliknięciu
    else:
        # Ekran gry
        screen.fill(WHITE)

        # Rysowanie platformy
        pygame.draw.rect(screen, BLACK, (0, 500, 100, 450))  # Blok startowy
        pygame.draw.rect(screen, BLACK, (100 + random_gap, 500, random_size, 450))  # Platforma
        pygame.draw.rect(screen, RED, (80, 500 - high, 20, high))  # Gracz
        pygame.draw.rect(screen, GREEN, (60, 465, 15, 35))  # Ludzik

        # Sterowanie
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            high += 5

        # Warunki wygranej/przegranej
        if high > random_gap:
            if high < random_gap + random_size:
                print("Wygrana")
            else:
                print("Przegrana")
                gen += 1
                high = 20  # Reset wysokości po przegranej
                random_size, random_gap = platform()  # Generujemy nową platformę
        else:
            print("Przegrana")

        # Wyświetlanie wyniku
        text = font.render(f"Wynik: {gen}", True, BLACK)
        screen.blit(text, (10, 10))

    # Odświeżanie ekranu
    pygame.display.flip()
    clock.tick(60)

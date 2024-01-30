# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:48:27 2024

@author: Aramis
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import numpy as np

# Initialisation de pygame
pygame.init()

# Paramètres du jeu de la vie
width, height = 800, 600
cell_size = 10
rows, cols = height // cell_size, width // cell_size
grid = np.random.choice([0, 1], size=(rows, cols), p=[0.9, 0.1])

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)

# Initialisation de la fenêtre
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de la Vie")

# Fonction pour mettre à jour la grille
def update_grid():
    global grid
    new_grid = grid.copy()

    for i in range(rows):
        for j in range(cols):
            neighbors = (
                grid[i - 1:i + 2, j - 1:j + 2].sum() -
                grid[i, j]
            )
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    grid = new_grid

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Vérifiez si une touche du clavier est pressée
            running = False
    # Mise à jour de la grille
    update_grid()

    # Affichage de la grille
    screen.fill(black)
    for i in range(rows):
        for j in range(cols):
            color = white if grid[i, j] == 1 else black
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    pygame.display.flip() #met a jour la grille
    clock.tick(10)  # Vitesse de mise à jour (10 générations par seconde)

# Quitter pygame
pygame.quit()

import pygame
import random
import sys
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dots = []
#dot_num = random.randint(5, 50)
#for x in range(dot_num):
#    x = random.randint(1, 10)
#    y = random.randint(1, 10)
#    dots.append((x*10, y*10))

dots.extend([(100, 100), (110, 100), (120, 100), (110, 90), (100, 90), (90, 90)])
#dots.append((110, 100))
#dots.append((120, 100))
#dots.append((110, 90))
#dots.append((100, 90))
#dots.append((90, 90))
run = True
def draw_dot(coords, red, green, blue):
    screen.set_at(coords, (red, green, blue))

def populate_list(k, dot):
#    k.extend([
    k.append((dot[0] + 10, dot[1]))
    k.append((dot[0] - 10, dot[1]))
    k.append((dot[0], dot[1] + 10))
    k.append((dot[0], dot[1] - 10))
    k.append((dot[0] + 10, dot[1] + 10))
    k.append((dot[0] - 10, dot[1] - 10))
    k.append((dot[0] - 10, dot[1] + 10))
    k.append((dot[0] + 10, dot[1] - 10))


def find_new():
    dots_new = set()

    for dot in dots: 
        k = []
        populate_list(k, dot)
        for elem in k:
            if elem not in dots:
                n = calculate_neighbours(elem)
                if n == 3:
                    dots_new.add(elem)
    return dots_new

def calculate_neighbours(dot):
    neighbours = 0
    k = []
    populate_list(k, dot)
   
    for elem in k:
        if elem in dots:
            neighbours += 1
    return neighbours


while run:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    for dot in dots:
        draw_dot(dot, red, green, blue)
    pygame.display.flip()

    dots_new = find_new()
    dots_to_remove = [dot for dot in dots if calculate_neighbours(dot) not in [2, 3]]
    [draw_dot(dot, 0, 0, 0) for dot in dots_to_remove]
    dots = [dot for dot in dots if dot not in dots_to_remove] 
    dots = dots + list(dots_new)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(1)

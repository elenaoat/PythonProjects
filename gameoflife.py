import pygame
import random
import sys
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dots = set()
#dot_num = random.randint(5, 50)
#for x in range(dot_num):
#    x = random.randint(1, 10)
#    y = random.randint(1, 10)
#    dots.append((x*10, y*10))

dots.update({(100, 100), (110, 100), (120, 100), (110, 90), (100, 90), (90, 90)})
run = True
def draw_dot(coords, red, green, blue):
    """ 
    Draw a dot with respective
    coords and supplied color.
    """
    screen.set_at(coords, (red, green, blue))

def populate_list(k, dot):
    """
    Populate given list with all adjacent
        dots for a given dot.

    There are 8 adjacent dots for any dot.
    """
    k.extend([(dot[0] + 10, dot[1]), (dot[0] - 10, dot[1]), (dot[0], dot[1] + 10), 
              (dot[0], dot[1] - 10), (dot[0] + 10, dot[1] + 10), (dot[0] - 10, dot[1] - 10), 
              (dot[0] - 10, dot[1] + 10), (dot[0] + 10, dot[1] - 10)]);

def find_new():
    """
    For existing dots at the moment,
    calculate if any new dots will
    become alive. If number of adjacent dots for
    a currently dead dots equals 3, the dot
    becomes alive.        
    """
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
    """
    Calculate the number of alive dots
    that are adjacent to a given dot.
    """
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
    dots_to_remove = {dot for dot in dots if calculate_neighbours(dot) not in [2, 3]}
    for dot in dots_to_remove:
        draw_dot(dot, 0, 0, 0)
    dots = dots - dots_to_remove
    dots = dots | dots_new

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(1)

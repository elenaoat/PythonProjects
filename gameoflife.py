import pygame
import random
import sys
width = 640
height = 400

i=0


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dots = []
dots.append((100, 100))
dots.append((110, 100))
dots.append((120, 100))
dots.append((110, 90))
dots.append((100, 90))
dots.append((90, 90))
run = True
def draw_dot(coords, red, green, blue):
    screen.set_at(coords, (red, green, blue))

def find_new():
    dots_new = set()
    for dot in dots: 
        k = []
        k.append((dot[0] + 10, dot[1]))
        k.append((dot[0] - 10, dot[1]))
        k.append((dot[0], dot[1] + 10))
        k.append((dot[0], dot[1] - 10))
        k.append((dot[0] + 10, dot[1] + 10))
        k.append((dot[0] - 10, dot[1] - 10))
        k.append((dot[0] - 10, dot[1] + 10))
        k.append((dot[0] + 10, dot[1] - 10))
        for elem in k:
            if elem not in dots:
                n = calculate_neighbours(elem)
                if n == 3:
                    dots_new.add(elem)
    return dots_new

def calculate_neighbours(dot):
    neighbours = 0
    k = []
    k.append((dot[0]-10, dot[1]))
    k.append((dot[0]+10, dot[1]))
    k.append((dot[0], dot[1]-10))
    k.append((dot[0], dot[1]+10))
    k.append((dot[0]-10, dot[1]-10))
    k.append((dot[0]+10, dot[1]+10))
    k.append((dot[0]-10, dot[1]+10) )
    k.append((dot[0]+10, dot[1]-10))
    for elem in k:
        if elem in dots:
            neighbours += 1
    return neighbours


while run:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    i += 1
#    if i == 4:
#        pygame.quit()
#        sys.exit()
    for dot in dots:
        print dot
        draw_dot(dot, red, green, blue)
    pygame.display.flip()

    dots_to_remove = []
    dots_new = find_new()
    for dot in dots:        
        neigh = calculate_neighbours(dot)
        if neigh not in [2, 3]:
            dots_to_remove.append(dot)
            draw_dot(dot, 0, 0, 0)
    dots = [dot for dot in dots if dot not in dots_to_remove] 
    
    for dot in dots_new:
       dots.append(dot)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(1)

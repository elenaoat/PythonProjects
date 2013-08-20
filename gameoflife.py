import pygame
import random
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dots = []
dots.append((100, 100))
dots.append((110, 100))
dots.append((90, 100))
dots.append((80, 100))
run = True
def draw_dot(coords, red, green, blue):
    screen.set_at(coords, (red, green, blue))

def find_new():
    dots_new = []
    for dot in dots: 
        if (dot[0] + 10, dot[1]) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
        if (dot[0] - 10, dot[1]) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
        if (dot[0], dot[1] + 10) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
        if (dot[0], dot[1] - 10) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
        if (dot[0] + 10, dot[1] + 10) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
        if (dot[0] - 10, dot[1] - 10) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
        if (dot[0] - 10, dot[1] + 10) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
        if (dot[0] + 10, dot[1] - 10) not in dots:
            n = calculate_neighbours(dot[0], dot[1])
            if n == 3:
                dots_new.append(dot[0] + 10, dot[1])
    return dots_new

def calculate_neighbours(dot):
    neighbours = 0
    if (dot[0]-10, dot[1]) in dots: 
        neighbours += 1
    if (dot[0]+10, dot[1]) in dots: 
        neighbours += 1
    if (dot[0], dot[1]-10) in dots: 
        neighbours += 1
    if (dot[0], dot[1]+10) in dots: 
        neighbours += 1
    if (dot[0]-10, dot[1]-10) in dots: 
        neighbours += 1
    if (dot[0]+10, dot[1]+10) in dots: 
        neighbours += 1
    if (dot[0]-10, dot[1]+10) in dots: 
        neighbours += 1
    if (dot[0]+10, dot[1]-10) in dots: 
        neighbours += 1
    print dot, neighbours
    return neighbours

    #if neighbours in [0, 1] or neighbours > 3:
    #    draw_dot(dot, 0, 0, 0)
    #    dots.remove(dot)
    

while run:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    for dot in dots:
        draw_dot(dot, red, green, blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(1)
    for dot in dots:
        print dot
        dots_new = find_new()
        print dots_new
        calculate_neighbours(dot)

import math
import random
import pygame

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    
def abs(x):
    if x < 0:
        return -x
    else:
        return x
    
def max(*x):
    i = x[0]

    for y in x:
        if y > i:
            i = y
    return i

def min(*x):
    i = x[0]

    for y in x:
        if y < i:
            i = y
    return i

def repeat(x, _function):
    for i in range(0, x):
        _function()

def frac(x):
    return x - int(x)

def real(x):
    if (abs(frac(float(x))) > 0):
        return float(x)
    else:
        return int(x)

def string(x):
    return str(x)

def clamp(va, x, y):
    if va > y:
        return y
    elif va < x:
        return x
    else:
        return va

def sqr(x):
    return x * x

def lerp(a, b, t):
    return a + (b - a) * t

def point_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
def floor(x):
    i = int(x)

    if x < i:
        return i - 1

    return i

def ord(x):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(x.upper()) + 65

def keyboard_check(tecla):
    teclas = pygame.key.get_pressed()
    return teclas[tecla]


def keyboard_check_pressed(eventos, tecla):
    for evento in eventos:
        if evento.type == pygame.KEYDOWN and evento.key == tecla:
            return True
    return False


def keyboard_check_released(eventos, tecla):
    for evento in eventos:
        if evento.type == pygame.KEYUP and evento.key == tecla:
            return True
    return False

def place_meeting(x, y, w, h, colisao):
    return (
        x < colisao[0] + colisao[2] and
        x + w > colisao[0] and
        y < colisao[1] + colisao[3] and
        y + h > colisao[1]
    )


def place_meeting_all(x, y, w, h, colisoes):
    for colisao in colisoes:
        if place_meeting(x, y, w, h, colisao):
            return True

    return False

def point_direction(x1, y1, x2, y2):
    return math.degrees(math.atan2(-(y2 - y1), x2 - x1))

def lengthdir_x(distancia, direcao):
    return math.cos(math.radians(direcao)) * distancia

def lengthdir_y(distancia, direcao):
    return -math.sin(math.radians(direcao)) * distancia

def choose(*args):
    return random.choice(args)

def irandom(x):
    return random.randint(0, x)

def move_towards_point(x1, y1, x2, y2, vel):
    direcao = point_direction(x1, y1, x2, y2)
    return (lengthdir_x(vel, direcao), lengthdir_y(vel, direcao))

def random_range(a, b):
    return random.uniform(a, b)

def irandom_range(a, b):
    return random.randint(a, b)

def array_insert(array, posicao, valor):
    array.insert(posicao, valor)

def array_delete(array, posicao, quantidade=1):
    del array[posicao:posicao + quantidade]

def array_length(array):
    return len(array)

def array_push(array, valor):
    array.append(valor)

def array_pop(array):
    return array.pop()

def array_find_index(array, valor):
    try:
        return array.index(valor)
    except:
        return -1
def array_contains(array, valor):
    return valor in array
def make_color_rgb(r, g, b):
    r = clamp(r, 0, 255)
    g = clamp(g, 0, 255)
    b = clamp(b, 0, 255)

    return "#" + string(hex(r)[2:]).zfill(2) + string(hex(g)[2:]).zfill(2) + string(hex(b)[2:]).zfill(2)
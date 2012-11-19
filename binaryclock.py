#! /usr/bin/python
#version: 0.3 (first release)
#license: GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)
#author: Antonius Frie
"""Definitively geeky binary clock

    This program is a simulation of an RGB-LED binary clock. It uses
    binary notation for displaying the time and mixes the colors for
    each bit. Red means hours, green minutes and blue seconds. Pressing
    p pauses the clock, pressing it again continues. Holding h, m or s
    shows only either hours, minutes and seconds. Help can also be found in
    binaryclock.png. Have fun using it!
    ----------------------------
    Copyright 2012 Antonius Frie

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""
import pygame
from pygame.locals import *
from time import localtime
import sys

def dec2bin(dec):
    """Converts a decimal number to a binary (list) 'number', using the 'Hornerschema'"""
    l = []
    while dec > 0:
        mod = dec%2
        dec = dec//2
        l.insert(0, mod)
    return l

def get_time(he,me,se):
    """Returns time in hours, minutes and seconds"""
    h = localtime()[3]*he
    m = localtime()[4]*me
    s = localtime()[5]*se
    return h, m, s

def get_colors(hms):
    """Returns a list of colors for a given time tupel (hours,minutes,seconds)"""
    h, m, s = hms
    r = []
    g = []
    b = []
    r = dec2bin(h)
    g = dec2bin(m)
    b = dec2bin(s)
    while len(r) < 6:
        r.insert(0, 0)
    while len(g) < 6:
        g.insert(0, 0)
    while len(b) < 6:
        b.insert(0, 0)
    colors = [[["black", "blue"], ["green", "cyan"]], [["red", "magenta"], ["yellow", "white"]]]
    color = []
    for i in range(1,7):
        acolor = colors[r[-i]][g[-i]][b[-i]]
        color.insert(0, acolor)
    return color

def main():
    """Main Function"""
    actualise_time = True
    ext_enable = True
    he = 1
    me = 1
    se = 1
    pygame.init()
    window = pygame.display.set_mode((444,100))
    pygame.display.set_caption('Binary Clock v0.3')
    red = pygame.image.load('pixel_red.png')
    green = pygame.image.load('pixel_green.png')
    blue = pygame.image.load('pixel_blue.png')
    yellow = pygame.image.load('pixel_yellow.png')
    magenta = pygame.image.load('pixel_magenta.png')
    cyan = pygame.image.load('pixel_cyan.png')
    white = pygame.image.load('pixel_white.png')

    while True:
        if actualise_time == True:
            colors = get_colors(get_time(he,me,se))
            for i in range(0,6):
                if colors[i] == 'red':
                    window.blit(red, (18+i*68, 18))
                if colors[i] == 'green':
                    window.blit(green, (18+i*68, 18))
                if colors[i] == 'blue':
                    window.blit(blue, (18+i*68, 18))
                if colors[i] == 'yellow':
                    window.blit(yellow, (18+i*68, 18))
                if colors[i] == 'magenta':
                    window.blit(magenta, (18+i*68, 18))
                if colors[i] == 'cyan':
                    window.blit(cyan, (18+i*68, 18))
                if colors[i] == 'white':
                    window.blit(white, (18+i*68, 18))
                if colors[i] == 'black':
                    window.fill((0,0,0),(18+i*68,18,64,64))
            pygame.display.update((18,18,472,64))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if (event.key == K_w) and ((event.mod == KMOD_LCTRL) or (event.mod == KMOD_RCTRL)):
                    pygame.quit()
                    sys.exit(0)
                if event.key in [K_h, K_m, K_s]:
                    ext_enable = True
                    he = 1
                    me = 1
                    se = 1
            if event.type == KEYDOWN:
                if event.key == K_p:
                    actualise_time ^= True
                if event.key == K_h and ext_enable == True:
                    me = 0
                    se = 0
                    ext_enable = False
                if event.key == K_m and ext_enable == True:
                    he = 0
                    se = 0
                    ext_enable = False
                if event.key == K_s and ext_enable == True:
                    he = 0
                    me = 0
                    ext_enable = False
        pygame.time.wait(500)

if __name__ == "__main__":
    main()

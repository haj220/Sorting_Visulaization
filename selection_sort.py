

import random
import pygame
from pygame.locals import *

pygame.init()
size = (width,height) = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
black = (128,120,150)
white = (200,150,220)
pygame.display.set_caption('selection Sort')
font_name = pygame.font.match_font('arial')
#create listay
def listay(length):
    list = []
    for i in range(0,length):
        list.append(i*10)
    random.shuffle(list)
    return list
#create sort class
class sort():
    font_name = pygame.font.match_font('arial')
    count = 0
    def __init__(self,list):
        self.list = list
        self.length = len(list)
        self.initial = 0
        self.image = pygame.Surface((width/5*3,height/5*3))
        self.rect = self.image.get_rect(center = (900/2,600/3))
        self.count = 0
        self.unitwidth = self.rect.width / self.length
    #for count
    def draw_text(self, surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, white)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
    def draw(self):
        screen.blit(self.image,self.rect)

    def vis(self):
        #algo for selection sort
        if self.initial < self.length:
            self.image.fill(black)
            
            small = self.initial
            for k in range(self.initial,self.length):
                if self.list[k] < self.list[small]:
                    small=k
            self.list[small],self.list[self.initial] = self.list[self.initial],self.list[small]
            self.initial += 1
            self.count += 1
            index = 0
            #rectangle for each number
            for k in range(0,self.rect.width,self.unitwidth+2):
                unit = pygame.Surface((self.unitwidth,self.list[index]))
                unit_rect = unit.get_rect()
                unit_rect.left = k
                self.image.blit(unit,unit_rect)
                index += 1
        return self.count
def main():
    list = listay(20)
    bubble_sort = sort(list)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
        count = bubble_sort.vis()
        screen.fill(black)
        print bubble_sort.list
        bubble_sort.draw()
        bubble_sort.draw_text(screen, str(count), 50, 300, 400)
        pygame.display.update()
        clock.tick(600)

main()

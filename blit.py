import pygame
from random import randint

WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE = (0 , 0 , 255)


class Blit():
    blit_width  =  10
    @staticmethod
    def row_draw(blits , x , y):
        for i , obj  in enumerate(blits)  :
            if(i == x or i == y):obj.get_rect(i , RED)
            else : obj.get_rect(i , BLUE)

    def __init__(self , screen , window_size):
        self.blit_height =  randint(1 , 334)
        self.y = window_size[-1] - self.blit_height
        self.color = (0 , 0 , 255) 
        self.screen = screen

    def get_rect(self ,  x , COLOR): 
        pygame.draw.rect(self.screen , COLOR ,((Blit.blit_width + 10) * x   , self.y , Blit.blit_width ,self.blit_height))

    def H(self):
        return self.blit_height

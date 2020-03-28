import pygame
from font import text
from blit import Blit


clock = pygame.time.Clock()
blits = []
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE = (0 , 0 , 255)
blen = 0

class Sort:
    @staticmethod
    def show(Text , screen ,  i ,  j ):
        clock.tick(5)
        Blit.row_draw(blits ,i ,  j)
        text(Text , screen).display()
        pygame.display.flip()  
        screen.fill(WHITE)

    def __init__(self , screen , window_size):
        global blen 
        global blits
        self.screen = screen
        blits = [Blit(self.screen , window_size) for _ in range(40)]
        blen = 40

    def __str__(self):
        return ("We out here sorting bruh")

    def bubble(self):
        self.name = "BUBBLE SORT"
        for i in range(blen - 1) : 
            for j in range(blen - 1) :
                if blits[j].H() > blits[j+1].H(): 
                    blits[j] , blits[j+1]  = blits[j+1]  , blits[j]
                    self.show(self.name , self.screen , j , j+1)

    def insertion(self):
        self.name = "INSERTION SORT"
        self.Text = text(self.name , self.screen)
        for i in range(1 , blen):
            temp = blits[i]
            pos = i-1 
            while pos != 0 and temp.H() < blits[pos].H():
                blits[pos+1] = blits[pos]
                pos -= 1
            blits[pos] = temp
            Sort.show(self.name , self.screen , pos , i)

class qicksort(Sort):
    def __init__(self , screen , window_size):
        super().__init__(self , screen , window_size)

    def partioning(self):
        pass

    def sort(self):
        pass

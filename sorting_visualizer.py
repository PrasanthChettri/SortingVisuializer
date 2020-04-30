import pygame  
from random import randint
from sort import *

pygame.init()  
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE = (0 , 0 , 255)
WS =(1000, 500)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WS)

obj = mergesort(screen , WS)
#obj = Sort(screen , WS) 
def mainloop():
    done = False  
    obj.sort()
    obj.sorted()
    #obj.insertion()
    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  
        Sort.show("FINISHED" , screen , -1 , -1)
mainloop()

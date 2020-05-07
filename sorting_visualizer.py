import pygame  
from random import randint
from sort import *
from sys import argv

pygame.init()  
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE = (0 , 0 , 255)
WS =(1000, 500)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WS)

def endloop():
    done = False  
    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  
        Sort.show("FINISHED" , screen , -1 , -1)

if __name__ == "__main__" : 
    try : 
        st = argv[1]
    except Exception : 
        endloop()
        exit()
    obj = None 
    if st  == "bubblesort" : 
        obj = bubblesort(screen , WS)
    if st  == "insertionsort" : 
        obj = insertionsort(screen , WS)
    if st  == "quicksort" : 
        obj = quicksort(screen , WS)
    if st == "mergesort" :
        obj = mergesort(screen , WS) 
    else :
        obj = bogosort(screen , WS)
    obj.sort()
    endloop()

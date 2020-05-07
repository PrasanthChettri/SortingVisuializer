import pygame

pygame.font.init()

class text():
    def __init__(self , string , screen):
        self.string = string 
        self.screen = screen

    def display(self) :
        try:
            font = pygame.font.Font("comici.ttf", 30)
            text = font.render(self.string, True, (0 , 0 , 0))
            self.screen.blit(text, (20, 20))

        except Exception as e:
            print("comici.ttf download")
            raise e

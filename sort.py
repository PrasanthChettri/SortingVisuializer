import pygame
from font import text
from blit import Blit
import random


clock = pygame.time.Clock()
blits = []
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE = (0 , 0 , 255)
blen = 0

class Sort:
    @staticmethod
    def sorted():
        print(* [blit.H() for blit in blits])
    @staticmethod
    def show(Text , screen ,  i ,  j ):
        clock.tick(60)
        Blit.row_draw(blits ,i ,  j)
        text(Text , screen).display()
        pygame.display.flip()  
        screen.fill(WHITE)

    def __init__(self , screen , window_size):
        global blen 
        global blits
        self.screen = screen
        blits = [Blit(self.screen , window_size) for _ in range(91)]
        blen = 91 

    def __str__(self):
        return ("We out here sorting bruh")

    #O(N^2) algos
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


#0(Nlogn) algos
class quicksort(Sort):
    def __init__(self, screen , window_size):
        self.name = "QUICK SORT"
        super().__init__(screen , window_size)
        self.arr = blits 

    def partition(self, s ,  l):
        i = s - 1
        for index in range(s , l):
            if  self.arr[index].H() < self.arr[l].H() :
                i += 1
                self.arr[index] , self.arr[i]  = self.arr[i] , self.arr[index]
                Sort.show(self.name , self.screen , i , index)

        self.arr[i + 1] , self.arr[l] = self.arr[l] , self.arr[i+1]
        Sort.show(self.name , self.screen , i+1 , l)
        return i + 1
        
    def sort(self  ,start = -1  , end = -1):
        if start == -1 and  end == -1 : start = 0 ; end = len(self.arr) - 1
        if start < end : 
            pivot = end 
            p = self.partition(start,pivot)
            self.sort(p + 1,  end)
            self.sort(start, p - 1)

class mergesort(Sort):
    def __init__(self , screen , window_size):
        super().__init__(screen , window_size)
        self.arr = blits
        self.name = "Merge Sort"

    def merge(self , left , right , middle):
        temp1 = self.arr[left:middle + 1].copy()
        temp2 = self.arr[middle+1:right+1].copy()
        cnt = 0
        i , j = 0 , 0
        l1 = len(temp1)
        l2 = len(temp2)
        while i < l1 and j < l2 :
            Sort.show(self.name , self.screen , -1 , -1)
            if(temp1[i].H() < temp2[j].H()):
                self.arr[left+cnt] = temp1[i]
                i += 1
                cnt += 1

            elif (temp1[i].H() > temp2[j].H()):
                self.arr[left+cnt] = temp2[j]
                j += 1
                cnt += 1

            else :
                self.arr[left+cnt] = temp1[i]
                self.arr[left+cnt+1] = temp2[j]
                i += 1
                j += 1
                cnt += 2

        for f in range(i , l1):
                self.arr[left+cnt] = temp1[f]
                cnt += 1

        for f in range(j , l2):
                self.arr[left+cnt] = temp2[f]
                cnt+=1
                
                
    def sort(self , left =  -69 , right =  -69):
        if(left  == -69 and right == -69): left , right =  0  , len(self.arr) - 1 ;
        if(left < right):
            middle = (left+right)//2
            self.sort(left , middle)
            self.sort(middle + 1, right)
            self.merge(left , right , middle)

#the greatest sorting algo of all : B O G O S O R T
class bogosort(Sort):
    def __init__(self, screen , window_size):
        self.name = "B O G O SORT the chaddest sort"
        super().__init__(screen , window_size)
        self.arr = blits
        self.l = len(self.arr)

    def is_sorted(self): 
        for i in range(0, self.l-1): 
            if (self.arr[i].H() > self.arr[i+1].H()): 
                return False
        return True

    def sort(self): 
        while (self.is_sorted() == False): 
            self.shuffle() 

    def shuffle(self): 
        for i in range (0,self.l): 
            r = random.randint(0,self.l-1) 
            self.arr[i], self.arr[r] = self.arr[r], self.arr[i] 
            self.show(self.name , self.screen ,i , r)

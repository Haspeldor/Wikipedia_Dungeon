import pygame

class Character():

    # creates a new character
    def __init__(self, color=(0, 0, 255), x_size=50, y_size=50, x_pos=935, y_pos=300, speed=15):
        self.color = color
        self.x_size = x_size
        self.y_size = y_size
        self.x_pos = x_pos 
        self.y_pos = y_pos 
        self.speed = speed
    
    # moves up 
    def move_up(self):
        self.y_pos -= self.speed
        if self.y_pos < 100:
            self.y_pos = 100

   
    # moves down
    def move_down(self):
        self.y_pos += self.speed
        if self.y_pos > 880 + self.y_size:
            self.y_pos = 880 + self.y_size


    # moves left
    def move_left(self):
        self.x_pos -= self.speed
        if self.x_pos < 100:
            self.x_pos = 100


    # moves right 
    def move_right(self):
        self.x_pos += self.speed
        if self.x_pos > 1720 + self.x_size:
            self.x_pos = 1720 + self.x_size

    # moves character around freely
    def spawn(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
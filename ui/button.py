import pygame
import input.input as input

from graphics import gui

class Button:
    def __init__(self, text, x, y, width, height, color, textColor, onClick):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.scale = 1
        self.scaler = 1.5
        
        self.textColor = textColor
        self.onClick = onClick
    
    def draw(self):
        x = self.x - (self.width * (self.scale - 1) / 2)
        y = self.y - (self.height * (self.scale - 1) / 2)
        width = self.width * self.scale
        height = self.height * self.scale
        pygame.draw.rect(gui.screen, self.color, (x, y, width, height))
        gui.drawText(self.text, x+width//2, y+height//2, int(20*self.scale), self.textColor)
        
    def isOver(self, x, y):
        if x is None or y is None:
            return False
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height
    
    def update(self):
        self.draw()
        
        if self.isOver(input.mousePos.x, input.mousePos.y):
            if input.mouseBindings["lmb"].justPressed:
                self.onClick()
            self.scale = self.scaler
        else:
            self.scale = 1
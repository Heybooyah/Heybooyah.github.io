from graphics import gui
from ui.button import Button
from ui.text import Text
from logic.game import game

def show():
    gui.clear()
    update()

def hide():
    gui.clear()

def draw():
    for object in objects:
        object.draw()
    for text in texts:
        text.draw()
    
def update():
    for object in objects:
        object.update()
        
title = "Settings Menu"
objects = []
texts = [Text(title, 200, 100, (255, 0, 0), 50)]
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
    objects.sort(key = lambda x : x.z)
    for object in objects:
        object.draw()
    for text in texts:
        text.draw()

def startGame():
    hide()
    gui.setScreen("game")
    
def update():
    for object in objects:
        object.update()
        
def settings():
    hide()
    gui.setScreen("settings")
        
title = "Main Menu"
objects = [Button("Start", 100, 175, 100, 50, (0, 255, 0), (255, 0, 0), startGame), Button("Settings", 100, 250, 100, 50, (0, 255, 0), (255, 0 ,0), settings),Button("Quit", 100, 325, 100, 50, (0, 255, 0), (255, 0, 0), quit)]
texts = [Text(title, 200, 100, (255, 0, 0), 50)]
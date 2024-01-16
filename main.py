import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blue Square")

# Set up the blue color
blue = (0, 0, 255)

# Set up the square position and size
square_size = 50
square_x = (width - square_size) // 2
square_y = (height - square_size) // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the blue square
    screen.fill((255, 255, 255))  # Fill the screen with white color
    pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)

# #the main file, where everything starts

# #external imports
# import pygame
# import asyncio

# # internal imports
# import graphics.gui as gui #for drawing
# from input import input #for input handling
# from images import images #for loading images

# async def main(): # main function, where everything starts
#     init() # initialize
#     while True: #loop forever
#         for event in pygame.event.get(): #for every pygame event
#             if event.type == pygame.QUIT: #if the user tries to quit
#                 pygame.quit() #quit pygame
#                 quit() #quit python
#             input.handleEvent(event) #else handle the event
#         update() #update the game
#         await asyncio.sleep(0) #wait for a frame

# def update(): #updates the game
#     input.updateFrameTimes() #update the frame times in input
    
#     gui.update() #update the gui
#     pygame.display.update() #update pygame

# def init(): #initializes the game
#     pygame.init() #initialize pygame
#     gui.init() #initialize the gui
#     images.init() #initialize the images
#     input.init() #initialize the input

# # if __name__ == "__main__": # if this file is being run directly
# asyncio.run(main()) # run the main function
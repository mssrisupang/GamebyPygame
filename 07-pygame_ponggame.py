# Import necessary libraries
import pygame
import sys

# Initialize PyGame
pygame.init()

# Initialize a font object
font = pygame.font.Font(None, 36)  

# Define game window settings
WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PongGame')

# Define colors
color = (0, 0, 0)  #black
# Initialize the score
score = 0

# Define the render_text function
def render_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect) 

### Create Sprite ################
    
# 1. Class Paddle
    





# 2. Class Ball














# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Check collision
    #score +=1
    


    # Render game objects
    screen.fill(color)
    render_text(f"Score: {score}", (255,255,255), WIDTH//2, 20)  
    
    

    pygame.display.flip()
    pygame.display.update()

# Clean up and quit
pygame.quit()
sys.exit()

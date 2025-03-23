import pygame
import sys
pygame.init()

# Set the dimensions of your GUI window 
window_size = (400, 300) # Width, Height
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("GUI Controller with PyGame")

# Choose a color for the background and fill the screen with it.
background_color = (255, 255, 255) # White
screen.fill(background_color)

# Update the display 
pygame.display.flip()

# Main Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")
    button_color = (0, 255, 0) # Green
    button_rect = pygame.Rect(150, 125, 100, 50) # x, y, width, height
    pygame.draw.rect(screen, button_color, button_rect)
    
    # Update the display 
    pygame.display.flip()

# Clean up and quite
pygame.quit()
sys.exit()




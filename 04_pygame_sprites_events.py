# Import necessary libraries
import pygame
import sys

# Initialize PyGame
pygame.init()

# Define game window settings
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My PyGame with Musk')

# Define colors
color = (255, 255, 255)  #white
#color = (0,0,255)       #blue

# Sprite Class
class MySprite(pygame.sprite.Sprite):
    def __init__(self,x, y, image_path):            # constructor
      super().__init__()
      original_image = pygame.image.load(image_path).convert_alpha()
      new_width, new_height = 86, 86  # The new size you want for the image
      self.image = pygame.transform.scale(original_image, (new_width, new_height))
      self.rect = self.image.get_rect(topleft=(x, y))

      ### add clickable even
    def handle_mouse_event(self, pos, button):
        if self.rect.collidepoint(pos):
            print(f"Sprite at ({self.rect.x}, {self.rect.y}) clicked with button {button}")

# Create sprite instance and sprite group
sprite1 = MySprite(10, 10, 'musk.png')  
sprite2 = MySprite(100, 100, 'mas.png')  
sprites = pygame.sprite.Group()
sprites.add(sprite1,sprite2)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        ### Add more events here
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_button = event.button
            for sprite in sprites:
                if isinstance(sprite, MySprite):
                    sprite.handle_mouse_event(mouse_pos, mouse_button)

    # Update game objects
    # (Add code to update game objects' states)
    sprites.update()


    # Render game objects
    screen.fill(color)
    # (Add code to draw game objects on the screen)
    sprites.draw(screen)

    #pygame.display.flip()
    pygame.display.update()

# Clean up and quit
pygame.quit()
sys.exit()

# Import necessary libraries
import pygame
import sys

# Initialize PyGame
pygame.init()

# Define game window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My PyGame with MultiPlayers')

# Define colors
color = (255, 255, 255)  #white
#color = (0,0,255)       #blue

# Sprite Class
class MySprite(pygame.sprite.Sprite):
    def __init__(self,x, y, image_path, speed):            # constructor
      super().__init__()
      original_image = pygame.image.load(image_path).convert_alpha()
      new_width, new_height = 86, 86  # The new size you want for the image
      self.image = pygame.transform.scale(original_image, (new_width, new_height))
      self.rect = self.image.get_rect(topleft=(x, y))
      self.speed = speed   # add speed

      ### add clickable even
    def handle_mouse_event(self, pos, button):
        if self.rect.collidepoint(pos):
            print(f"Sprite at ({self.rect.x}, {self.rect.y}) clicked with button {button}")

    # Method to move the sprite
    def move(self, dx=0, dy=0):
        self.rect.x += dx*self.speed
        self.rect.y += dy*self.speed

    

# Create sprite instance and sprite group
sprite1 = MySprite(10, 10, 'musk.png', 0.6)  
sprite2 = MySprite(100, 100, 'mas.png', 0.6)  
sprite3 = MySprite(300, 300, 'car.png', 0.6)  
sprites = pygame.sprite.Group()
sprites.add(sprite1,sprite2,sprite3)

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
    
    # Check pressed keys to move sprites
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.move(dx=-1)  # Move sprite1 left
    if keys[pygame.K_RIGHT]:
        sprite1.move(dx=1)   # Move sprite1 right
    if keys[pygame.K_UP]:
        sprite1.move(dy=-1)  # Move sprite1 up
    if keys[pygame.K_DOWN]:
        sprite1.move(dy=1)   # Move sprite1 down

    if keys[pygame.K_a]:
        sprite2.move(dx=-1)  # Move sprite2 left with 'A'
    if keys[pygame.K_d]:
        sprite2.move(dx=1)   # Move sprite2 right with 'D'
    if keys[pygame.K_w]:
        sprite2.move(dy=-1)  # Move sprite2 up with 'W'
    if keys[pygame.K_s]:
        sprite2.move(dy=1)   # Move sprite2 down with 'S'

    if keys[pygame.K_b]:
        sprite3.move(dx=-1)  # Move sprite2 left with 'z'
    if keys[pygame.K_m]:
        sprite3.move(dx=1)   # Move sprite2 right with 'c'
    if keys[pygame.K_h]:
        sprite3.move(dy=-1)  # Move sprite2 up with 'W'
    if keys[pygame.K_n]:
        sprite3.move(dy=1)   # Move sprite2 down with 'S'

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

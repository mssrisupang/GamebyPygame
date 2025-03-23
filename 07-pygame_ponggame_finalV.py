# Import necessary libraries
import pygame
import sys
import random

# Initialize PyGame
pygame.init()

# Initialize a font object
font = pygame.font.Font(None, 36)  

# Define game window settings
WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PongGame')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Initialize the score
score = 0

clock = pygame.time.Clock()

# Define the render_text function
def render_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect) 

### Create Sprite ################
    
# 1. Class Paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self,x, y, color):            # constructor
        super().__init__()
        self.image = pygame.Surface((250, 20))
        self.image.fill((color))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x< 0:
                self.rect.x = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > WIDTH - self.rect.width:
                self.rect.x = WIDTH - self.rect.width

# 2. Class Ball

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        ## Initial ball speed
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.y <= 0 or self.rect.y >= HEIGHT - self.rect.height:
            self.speed_y = -self.speed_y

        # Reset ball and update score if it goes off the left or right side of the screen
        if self.rect.x < 0:
            self.reset()
            # Update player 2 score
        if self.rect.x > WIDTH - self.rect.width:
            self.reset()
            # Update player 1 score
    
    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])
   


# Initialize the player paddle and ball
player = Paddle(WIDTH // 2 - 30, HEIGHT - 20, WHITE)
ball = Ball(WIDTH // 2 - 5, HEIGHT // 2 - 5)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, ball)



# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Check collision
    #score +=1
            
    # Update game objects
    all_sprites.update()

    # Check for collisions between the ball and paddle
    if pygame.sprite.collide_rect(ball, player):
        ball.speed_x = -ball.speed_x

    # Render game objects
    screen.fill(BLACK)
    all_sprites.draw(screen)
    render_text(f"Score: {score}", (255,255,255), WIDTH//2, 20)  
    
    

    pygame.display.flip()
    clock.tick(60)  # 30 FPS

# Clean up and quit
pygame.quit()
sys.exit()

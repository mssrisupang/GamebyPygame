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
pygame.display.set_caption('Pong Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((150, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))

        # Initial ball speed
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])  # Changed for vertical collision logic

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y

        # Reset ball if it goes off the left or right side of the screen
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.reset()

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])

# Initialize the player paddle and ball
player = Paddle(WIDTH // 2 - 75, HEIGHT - 30)  # Adjusted x position for centering
ball = Ball(WIDTH // 2, HEIGHT // 2)

# Create a sprite group for all sprites
all_sprites = pygame.sprite.Group(player, ball)

def render_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))  # Center the text
    screen.blit(text_surface, text_rect)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    all_sprites.update()

    # Check for collisions between the ball and paddle
    collision = pygame.sprite.collide_rect(ball, player)
    if collision:
        ball.speed_y = -ball.speed_y  # Change direction vertically

    # Render game objects
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Render centered text
    render_text("Pong", WHITE, WIDTH // 2, 10)

    pygame.display.flip()

# Clean up and quit
pygame.quit()
sys.exit()

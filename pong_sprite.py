import pygame
import random
pygame.init()

# Game window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Pong")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle properties
paddle_width = 15
paddle_height = 90
paddle_speed = 6

# Ball properties
ball_width = 20
ball_x_speed = 4
ball_y_speed = 4

# Initial positions
paddle1_x_pos = 20
paddle1_y_pos = screen_height // 2 - paddle_height // 2
paddle2_x_pos = screen_width - 20 - paddle_width
paddle2_y_pos = screen_height // 2 - paddle_height // 2
ball_x_pos = screen_width // 2 - ball_width // 2
ball_y_pos = screen_height // 2 - ball_width // 2

# Font setup for scoring
pygame.font.init()
font_size = 30
game_font = pygame.font.SysFont("Arial", font_size)

# Target properties
target_width = 100
target_height = 100
target_color = (255, 0, 0)  # Red
target_x_pos = screen_width // 2 - target_width // 2
target_y_pos = screen_height // 2 - target_height // 2

running = True
clock = pygame.time.Clock()

score_player1 = 0
score_player2 = 0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Game logic for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y_pos > 0:
        paddle1_y_pos -= paddle_speed
    if keys[pygame.K_s] and paddle1_y_pos < screen_height - paddle_height:
        paddle1_y_pos += paddle_speed
    if keys[pygame.K_UP] and paddle2_y_pos > 0:
        paddle2_y_pos -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y_pos < screen_height - paddle_height:
        paddle2_y_pos += paddle_speed

    # Ball movement
    ball_x_pos += ball_x_speed
    ball_y_pos += ball_y_speed

    # Collision detection with walls
    if ball_y_pos <= 0 or ball_y_pos >= screen_height - ball_width:
        ball_y_speed *= -1

    # Collision detection with paddles
    if (ball_x_pos <= paddle1_x_pos + paddle_width and 
        paddle1_y_pos < ball_y_pos + ball_width and 
        ball_y_pos < paddle1_y_pos + paddle_height) or \
       (ball_x_pos + ball_width >= paddle2_x_pos and 
        paddle2_y_pos < ball_y_pos + ball_width and 
        ball_y_pos < paddle2_y_pos + paddle_height):
        ball_x_speed *= -1

    # Scoring
    if ball_x_pos < 0:
        score_player2 += 1
        ball_x_pos = screen_width // 2 - ball_width // 2
        ball_y_pos = screen_height // 2 - ball_width // 2
        ball_x_speed = -ball_x_speed
    elif ball_x_pos > screen_width:
        score_player1 += 1
        ball_x_pos = screen_width // 2 - ball_width // 2
        ball_y_pos = screen_height // 2 - ball_width // 2
        ball_x_speed = -ball_x_speed

    if (target_x_pos < ball_x_pos + ball_width and
        target_x_pos + target_width > ball_x_pos and
        target_y_pos < ball_y_pos + ball_width and
        target_y_pos + target_height > ball_y_pos):
        # This condition checks if the rectangles are overlapping
        # Update the score
        score_player1 += 1  # Or score_player2, depending on your game rules

        # Optionally, reset or move the target
        target_x_pos = random.randint(0, screen_width - target_width)
        target_y_pos = random.randint(0, screen_height - target_height)

    # Drawing code (clear screen, draw paddles, ball, etc.)
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle1_x_pos, paddle1_y_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x_pos, paddle2_y_pos, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x_pos, ball_y_pos, ball_width, ball_width))
    
    # Draw the target
    pygame.draw.rect(screen, target_color, (target_x_pos, target_y_pos, target_width, target_height))
    
    # Render and draw scores
    score_text = f"Player 1: {score_player1}    Player 2: {score_player2}"
    score_surface = game_font.render(score_text, True, white)
    score_rect = score_surface.get_rect(center=(screen_width / 2, 30))
    screen.blit(score_surface, score_rect)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()


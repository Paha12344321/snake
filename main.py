import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set segment size and game speed
segment_size = 20
game_speed = 10

clock = pygame.time.Clock()

# Function to display score
def display_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, white)
    window.blit(text, (10, 10))

# Game loop
def game_loop():
    game_over = False
    game_quit = False

    # Snake initial position and movement
    snake_x = width / 2
    snake_y = height / 2
    snake_x_change = 0
    snake_y_change = 0

    # Snake segments
    snake_segments = []
    segment_length = 1

    # Food position
    food_x = round(random.randrange(0, width - segment_size) / segment_size) * segment_size
    food_y = round(random.randrange(0, height - segment_size) / segment_size) * segment_size

    while not game_quit:
        while game_over:
            window.fill(black)
            font = pygame.font.Font(None, 72)
            text = font.render("Game Over", True, red)
            text_rect = text.get_rect(center=(width / 2, height / 2))
            window.blit(text, text_rect)
            display_score(segment_length - 1)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -segment_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = segment_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -segment_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = segment_size
                    snake_x_change = 0

        snake_x += snake_x_change
        snake_y += snake_y_change

        # Check for boundaries
        if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
            game_over = True

        # Check for self-collision
        for segment in snake_segments[1:]:
            if segment == [snake_x, snake_y]:
                game_over = True

        # Add new segment to the snake
        snake_segments.append([snake_x, snake_y])
        if len(snake_segments) > segment_length:
            del snake_segments[0]

        # Draw game elements
        window.fill(black)
        for segment in snake_segments:
            pygame.draw.rect(window, green, (segment[0], segment[1], segment_size, segment_size))
        pygame.draw.rect(window, red, (food_x, food_y, segment_size, segment_size))
        display_score(segment_length - 1)
        pygame.display.update()

        # Check if the snake eats the food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, width - segment_size) / segment_size) * segment_size
            food_y = round(random.randrange(0, height - segment_size) / segment_size) * segment_size
            segment_length += 1

        # Control game speed
        clock.tick(game_speed)

    pygame.quit()

# Start the game
game_loop()

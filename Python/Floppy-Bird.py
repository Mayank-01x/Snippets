import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game variables
BIRD_WIDTH, BIRD_HEIGHT = 40, 30
bird_x, bird_y = WIDTH // 4, HEIGHT // 2
bird_y_change = 0

GRAVITY = 0.5
FLAP_STRENGTH = -10

PIPE_WIDTH = 60
PIPE_GAP = 150
pipe_speed = 4

score = 0
font = pygame.font.SysFont(None, 35)

# Function to draw bird
def draw_bird(x, y):
    pygame.draw.rect(SCREEN, BLACK, [x, y, BIRD_WIDTH, BIRD_HEIGHT])

# Function to draw pipes
def draw_pipes(pipe_list):
    for pipe in pipe_list:
        pygame.draw.rect(SCREEN, GREEN, pipe)

# Function to check for collision
def check_collision(bird_rect, pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_y <= 0 or bird_y >= HEIGHT:
        return True
    return False

# Function to display score
def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(text, [10, 10])

# Game loop
def game_loop():
    global bird_y, bird_y_change, score
    clock = pygame.time.Clock()

    pipe_x = WIDTH
    pipe_height = random.randint(150, 400)
    pipes = [
        pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_height),
        pygame.Rect(pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT)
    ]

    running = True
    while running:
        SCREEN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_change = FLAP_STRENGTH

        # Bird movement
        bird_y_change += GRAVITY
        bird_y += bird_y_change

        # Draw bird
        bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)
        draw_bird(bird_x, bird_y)

        # Move and draw pipes
        for pipe in pipes:
            pipe.x -= pipe_speed

        if pipes[0].x + PIPE_WIDTH < 0:
            score += 1
            pipe_height = random.randint(150, 400)
            pipes = [
                pygame.Rect(WIDTH, 0, PIPE_WIDTH, pipe_height),
                pygame.Rect(WIDTH, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT)
            ]

        draw_pipes(pipes)

        # Check for collision
        if check_collision(bird_rect, pipes):
            running = False

        # Display score
        display_score(score)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Start the game
game_loop()

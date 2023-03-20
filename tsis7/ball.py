import pygame

# Initialize Pygame
pygame.init()

# Define the screen size
screen_width = 500
screen_height = 500

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption for the window
pygame.display.set_caption("Moving Ball")

# Define the colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set the initial position and velocity of the ball
x = screen_width // 2
y = screen_height // 2
velocity = 20

# Define the function to draw the ball
def draw_ball(x, y):
    pygame.draw.circle(screen, red, (x, y), 25)

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= velocity
            elif event.key == pygame.K_DOWN:
                y += velocity
            elif event.key == pygame.K_LEFT:
                x -= velocity
            elif event.key == pygame.K_RIGHT:
                x += velocity

    # Check if the ball is still within the screen boundaries
    if x < 25:
        x = 25
    elif x > screen_width - 25:
        x = screen_width - 25
    if y < 25:
        y = 25
    elif y > screen_height - 25:
        y = screen_height - 25

    # Fill the screen with white color
    screen.fill(white)

    # Draw the ball
    draw_ball(x, y)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()

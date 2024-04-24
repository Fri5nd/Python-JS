import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960
GROUND_HEIGHT = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Load images
dino_img = pygame.image.load('Spill/assets/dino.png')
cactus_img = pygame.image.load('Spill/assets/cactus.png')
game_over_img = pygame.image.load('Spill/assets/game_over.png')

# Scale images
dino_img = pygame.transform.scale(dino_img, (100, 100))
cactus_img = pygame.transform.scale(cactus_img, (100, 100))
game_over_img = pygame.transform.scale(game_over_img, (800, 400))  # Increased size

# Game variables
dino_x = 100
dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - dino_img.get_height()
dino_vel_y = 0
gravity = 0.5
jump_strength = 15

cactus_list = []
cactus_vel_x = -8
cactus_min_interval = 1250  # Minimum interval for cactus spawn
cactus_max_interval = 2000  # Maximum interval for cactus spawn
next_cactus_time = pygame.time.get_ticks() + random.randint(cactus_min_interval, cactus_max_interval)

score = 0
high_score = 0
font = pygame.font.Font(None, 60)

clock = pygame.time.Clock()
running = True
game_over = False
speed_bonus_active = False
speed_bonus_count = 0  # Track the number of speed bonuses earned

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def spawn_cactus():
    cactus_x = SCREEN_WIDTH
    cactus_y = SCREEN_HEIGHT - GROUND_HEIGHT - cactus_img.get_height()
    cactus_list.append((cactus_x, cactus_y))

def check_collision():
    dino_rect = pygame.Rect(dino_x, dino_y, dino_img.get_width(), dino_img.get_height())
    for cactus_x, cactus_y in cactus_list:
        cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_img.get_width(), cactus_img.get_height())
        if dino_rect.colliderect(cactus_rect):
            return True
    return False

def update_high_score(score):
    global high_score
    if score > high_score:
        high_score = score

def increase_speed():
    global cactus_vel_x, speed_bonus_active, speed_bonus_count
    cactus_vel_x -= 3  # Increase speed by 3 units
    speed_bonus_active = True
    speed_bonus_count += 1

def reset_speed_bonus():
    global cactus_vel_x, speed_bonus_active, speed_bonus_count
    cactus_vel_x = -8
    speed_bonus_active = False
    speed_bonus_count = 0

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_y >= SCREEN_HEIGHT - GROUND_HEIGHT - dino_img.get_height():
                dino_vel_y = -jump_strength
            elif event.key == pygame.K_r and game_over:
                # Restart the game
                dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - dino_img.get_height()
                dino_vel_y = 0
                cactus_list = []
                score = 0
                game_over = False
                next_cactus_time = pygame.time.get_ticks() + random.randint(cactus_min_interval, cactus_max_interval)
                reset_speed_bonus()

    if not game_over:
        dino_vel_y += gravity
        dino_y += dino_vel_y

        if dino_y >= SCREEN_HEIGHT - GROUND_HEIGHT - dino_img.get_height():
            dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - dino_img.get_height()
            dino_vel_y = 0

        screen.blit(dino_img, (dino_x, dino_y))

        current_time = pygame.time.get_ticks()
        if current_time > next_cactus_time:
            next_cactus_time = current_time + random.randint(cactus_min_interval, cactus_max_interval)
            spawn_cactus()

        for cactus in cactus_list[:]:
            cactus_x, cactus_y = cactus
            cactus_x += cactus_vel_x
            if cactus_x < -cactus_img.get_width():
                cactus_list.remove(cactus)
                score += 1
                if score % 5 == 0:  # Increase speed every 5 score points
                    increase_speed()
            else:
                screen.blit(cactus_img, (cactus_x, cactus_y))
                cactus_list[cactus_list.index(cactus)] = (cactus_x, cactus_y)

        if check_collision():
            update_high_score(score)
            game_over = True

        draw_text(f"Score: {score}", font, BLACK, 100, 50)
        if speed_bonus_active:
            draw_text(f"Speed Bonus! x{speed_bonus_count}", font, BLACK, SCREEN_WIDTH // 2, 50)

    else:  # Game over
        screen.blit(game_over_img, (SCREEN_WIDTH // 2 - 400, SCREEN_HEIGHT // 2 - 200))  # Centered and larger
        draw_text(f"Score: {score}", font, BLACK, 100, 50)
        draw_text(f"High Score: {high_score}", font, BLACK, SCREEN_WIDTH - 250, 50)
        draw_text("Press R to Restart", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

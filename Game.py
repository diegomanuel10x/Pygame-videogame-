
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1184, 660))
pygame.display.set_caption("I'm not supper!(game)",)
clock = pygame.time.Clock()
t1 = pygame.font.Font(None, 50)

sky = pygame.image.load('sky.png')
ground = pygame.image.load('greeness.png')

score = 0

char1 = pygame.image.load('piglet.png').convert_alpha()
char2 = pygame.image.load('evilpig (2).png').convert_alpha()
char3 = pygame.image.load('Bigbadwolf.png').convert_alpha()
char4 = pygame.image.load('Viking.png').convert_alpha()
char5 = pygame.image.load('bird.png').convert_alpha()

char1_rect = char1.get_rect(midbottom=(140, 610))
char2_rect = char2.get_rect(midbottom=(500, 610))
char3_rect = char3.get_rect(midbottom=(800, 610))
char4_rect = char4.get_rect(midbottom=(1300, 610))
char5_rect = char5.get_rect(midbottom=(1000, 300))

char1_rect.inflate_ip(-40, -20)
char2_rect.inflate_ip(-40, -20)
char3_rect.inflate_ip(-40, -20)
char4_rect.inflate_ip(-40, -20)
char5_rect.inflate_ip(-30, -30)

char2_prev_x = char2_rect.x
char3_prev_x = char3_rect.x
char4_prev_x = char4_rect.x
char5_prev_x = char5_rect.x

# ----- NEW JUMP PHYSICS VARIABLES -----
char1_velocity_y = 0
gravity = 1  # Gravity acceleration per frame
jump_strength = -20  # Negative because y increases downward
on_ground = True
# --------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    text = t1.render(f"Score: {score}", True, "Black")

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 480))
    screen.blit(text, (100, 2))

    screen.blit(char1, char1_rect)
    screen.blit(char2, char2_rect)
    screen.blit(char3, char3_rect)
    screen.blit(char4, char4_rect)
    screen.blit(char5, char5_rect)

    char2_prev_x = char2_rect.x
    char3_prev_x = char3_rect.x
    char4_prev_x = char4_rect.x
    char5_prev_x = char5_rect.x

    char2_rect.x -= 9
    char3_rect.x -= 9
    char4_rect.x -= 9
    char5_rect.x -= 9

    if char2_prev_x >= char1_rect.left and char2_rect.right < char1_rect.left:
        score += 1
    if char3_prev_x >= char1_rect.left and char3_rect.right < char1_rect.left:
        score += 1
    if char4_prev_x >= char1_rect.left and char4_rect.right < char1_rect.left:
        score += 1
    if char5_prev_x >= char1_rect.left and char5_rect.right < char1_rect.left:
        score += 1

    if char2_rect.right < 0:
        char2_rect.left = 1184
    if char3_rect.right < 0:
        char3_rect.left = 1184
    if char4_rect.right < 0:
        char4_rect.left = 1184
    if char5_rect.right < 0:
        char5_rect.left = 1184

    # ----- APPLY GRAVITY -----
    char1_velocity_y += gravity
    char1_rect.y += char1_velocity_y

    # ----- CHECK GROUND COLLISION -----
    if char1_rect.bottom >= 610:
        char1_rect.bottom = 610
        char1_velocity_y = 0
        on_ground = True
    else:
        on_ground = False

    if (
        char1_rect.colliderect(char2_rect) or
        char1_rect.colliderect(char3_rect) or
        char1_rect.colliderect(char4_rect) or
        char1_rect.colliderect(char5_rect)
    ):
        score -= 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and on_ground:
        char1_velocity_y = jump_strength
        on_ground = False

    pygame.display.update()
    clock.tick(120)

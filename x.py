import sys

import pygame


def ball_animation():
    global ball_speed_x, ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    ball.x += ball_speed_x
    ball.y += ball_speed_y


pygame.init()

screen_width = 1200
screen_height = 800
fps = 60

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping-Pong")
clock = pygame.time.Clock()

# Window color
bg_color = pygame.Color("grey12")

# figures colors
light_grey = (200, 200, 200)


# Pygame Rects
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 25, 30, 30)
opponent = pygame.Rect(10, screen_height / 2 - 70, 16, 140)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 16, 140)


ball_speed_x = 5
ball_speed_y = 5

player_speed = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key == pygame.K_UP:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed += 10

    window.fill(bg_color)

    pygame.draw.ellipse(window, light_grey, ball)
    pygame.draw.rect(window, light_grey, opponent)
    pygame.draw.rect(window, light_grey, player)

    pygame.draw.aaline(window, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    player.y += player_speed

    ball_animation()

    pygame.display.flip()
    clock.tick(fps)
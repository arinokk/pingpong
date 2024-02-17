import pygame
import time
import sys
import random



def ball_animation():
    global ball_speedy, ball_speedx, player_score, computer_score
    if ball.left <= 0 or ball.right >= screen_w:
        ball.center = screen_w / 2, screen_h / 2
        time.sleep(1)
        ball_speedx *= -1
    if ball.top <= 0 or ball.bottom >= screen_h:
        ball_speedy *= -1

    if ball.colliderect(bar2) or ball.colliderect(bar1):
        ball_speedx *= -1




    ball.x += ball_speedx
    ball.y += ball_speedy

def player_animation():
    bar2.y += bar2_speed

    if bar2.top <= 0:
        bar2.top = 0
    if bar2.bottom >= screen_h:
        bar2.bottom = screen_h

def computer_animation():
    if bar1.top <= ball.top:
        bar1.top += bar1_speed
    if bar1.bottom >= ball.bottom:
        bar1.bottom -= bar1_speed


pygame.init()

screen_w = 900
screen_h = 500
fps = 60

window = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("PING-PONG")

clock = pygame.time.Clock()
bg_color = pygame.Color("light pink")
ball = pygame.Rect(screen_w / 2 - 15, screen_h / 2 - 15, 30, 30)
bar1 = pygame.Rect(10, screen_h / 2 - 70, 10, 140)
bar2 = pygame.Rect(screen_w - 20, screen_h / 2 - 70, 10, 140)
bar_c = pygame.Color("white")

ball_color = pygame.Color("white")
ball_speedx = 5 * random.choice((1, -1))
ball_speedy = 5 * random.choice((1, -1))
bar2_speed = 0
bar1_speed = 6
player_score = 0
computer_score = 0
font = pygame.font.Font(None, 50)
# start_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bar2_speed += 10
            if event.key == pygame.K_UP:
                bar2_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                bar2_speed -= 10
            if event.key == pygame.K_UP:
                bar2_speed += 10

    window.fill(bg_color)

    pygame.draw.aaline(window, bar_c, (screen_w / 2, 0), (screen_w / 2, screen_h))

    pygame.draw.ellipse(window, ball_color, ball)

    pygame.draw.rect(window, bar_c, bar1)

    pygame.draw.rect(window, bar_c, bar2)

    ball_animation()
    player_animation()
    computer_animation()
    if ball.left <= 0:
        player_score += 1
        print(player_score)
    if ball.right >= screen_w:
        computer_score += 1
        print(computer_score)
    ps = font.render(str(player_score), True, pygame.Color("white"))
    cs = font.render(str(computer_score), True, pygame.Color("white"))
    window.blit(ps, (screen_w - 100, 50))
    window.blit(cs, (50, 50))

    # if time.time() - start_time >= 3:
    #     ball_speedx += 10
    #     ball_speedy += 10
    #     start_time += 2
    #     print("speed change", start_time)

    pygame.display.flip()
    clock.tick(fps)

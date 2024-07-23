# House Drawing
import pygame

def draw_triangle(screen, center, length, color):
    x, y = center
    centroid = (3/4)**0.5 / length

    pygame.draw.polygon(screen, color, [
        (x, y - centroid),
        (x + length/2, y + (length - centroid)),
        (x - length/2, y + (length - centroid))
    ])

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    pygame.draw.rect(screen, (200, 70, 20), pygame.Rect(300, 200, 200, 200))
    pygame.draw.rect(screen, (50, 150, 200), pygame.Rect(325, 225, 50, 50))
    pygame.draw.rect(screen, (50, 150, 200), pygame.Rect(425, 225, 50, 50))
    pygame.draw.rect(screen, (50, 200, 50), pygame.Rect(375, 300, 50, 100))
    draw_triangle(screen, (400, 0), 200, (10, 10, 200))

    pygame.display.update()
    
pygame.quit()

# Moving Box
import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

box = pygame.Rect(375, 275, 50, 50)

box_velocity_x = 1
box_velocity_y = 1

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

        # Use this for keypress
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box.x -= box_velocity_x

            if event.key == pygame.K_RIGHT:
                box.x += box_velocity_x

            if event.key == pygame.K_UP:
                box.y -= box_velocity_y

            if event.key == pygame.K_DOWN:
                box.y += box_velocity_y

    # Or use this for keypress (not both)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box.x -= box_velocity_x

    if keys[pygame.K_RIGHT]:
        box.x += box_velocity_x

    if keys[pygame.K_UP]:
        box.y -= box_velocity_y

    if keys[pygame.K_DOWN]:
        box.y += box_velocity_y

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (40, 100, 200), box)

    pygame.display.update()
    
pygame.quit()

# DVD Logo Bouncing
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 600])

dvd_logo = pygame.image.load("dvd logo.png")
dvd_rect = dvd_logo.get_rect()
dvd_rect.x = 100
dvd_rect.y = 100

dvd_velocity_x = 5
dvd_velocity_y = 5

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    screen.fill((255, 255, 255))

    if dvd_rect.left <= 0 or dvd_rect.right >= screen.get_width():
        dvd_velocity_x *= -1

    if dvd_rect.top <= 0 or dvd_rect.bottom >= screen.get_height():
        dvd_velocity_y *= -1

    dvd_rect.x += dvd_velocity_x
    dvd_rect.y += dvd_velocity_y

    screen.blit(dvd_logo, dvd_rect)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()

# Catch the Apples Game
import pygame, random

pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

apple_img = pygame.image.load("Apple.jpg")
apple_rects = [pygame.Rect(random.randint(0, 750), random.randint(0, 150), 50, 50) for i in range(5)]

basket_img = pygame.image.load("Basket.png")
basket_rect = basket_img.get_rect()
basket_rect.x, basket_rect.y = 375, 550

speed = 1
score = 0

font = pygame.font.SysFont("consolas", 32)

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    screen.fill((255, 255, 255))

    if score > 0 and score % 5 == 0:
        speed = score // 2

    basket_rect.x = pygame.mouse.get_pos()[0]

    for i in range(len(apple_rects)):
        if apple_rects[i].bottom >= screen.get_height():
            runGame = False
        
        if basket_rect.colliderect(apple_rects[i]):
            score += 1
            apple_rects[i].x, apple_rects[i].y = random.randint(0, 750), random.randint(0, 150)

        apple_rects[i].y += speed
        
        screen.blit(apple_img, apple_rects[i])

    screen.blit(basket_img, basket_rect)

    score_text = font.render(f"Score: {score}", False, (0, 0, 0))

    screen.blit(score_text, (0, 0))

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()

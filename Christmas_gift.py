import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


GLOBE_CENTER = (WIDTH // 2, HEIGHT // 2 + 100)
GLOBE_RADIUS = 220

t = 0


class Snowflake:
    def __init__(self):
        self.reset()

    def reset(self):
        angle = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, GLOBE_RADIUS)
        self.x = GLOBE_CENTER[0] + r * math.cos(angle)
        self.y = GLOBE_CENTER[1] + r * math.sin(angle)
        self.speed = random.uniform(0.5, 2)
        self.size = random.randint(2, 4)

    def update(self):
        self.y += self.speed
        self.x += random.uniform(-0.5, 0.5)

        dx = self.x - GLOBE_CENTER[0]
        dy = self.y - GLOBE_CENTER[1]
        if dx*dx + dy*dy > GLOBE_RADIUS*GLOBE_RADIUS:
            self.reset()

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.size)


snowflakes = [Snowflake() for _ in range(200)]

def draw_sky(surface):
    for i in range(HEIGHT):
        c = 100 + int(80 * (i / HEIGHT))
        pygame.draw.line(surface, (c, c + 40, 255), (0, i), (WIDTH, i))

def draw_sun_with_rays(surface):
    sun_x, sun_y = WIDTH // 2, 100
    sun_radius = 35

    pygame.draw.circle(surface, (255, 230, 120), (sun_x, sun_y), sun_radius)

    ray_color = (255, 240, 150)
    ray_length = 60
    ray_count = 12

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        start_x = sun_x + sun_radius * math.cos(angle)
        start_y = sun_y + sun_radius * math.sin(angle)
        end_x = sun_x + (sun_radius + ray_length) * math.cos(angle)
        end_y = sun_y + (sun_radius + ray_length) * math.sin(angle)
        pygame.draw.line(surface, ray_color, (start_x, start_y), (end_x, end_y), 4)

def draw_clouds(surface):
    cloud_color = (255, 255, 255)
    clouds = [
        (150, 160), (180, 170), (210, 160),
        (400, 190), (430, 180), (460, 195)
    ]
    for x, y in clouds:
        pygame.draw.circle(surface, cloud_color, (x, y), 30)
        pygame.draw.circle(surface, cloud_color, (x + 25, y + 10), 25)
        pygame.draw.circle(surface, cloud_color, (x - 25, y + 10), 25)

def draw_tree(surface):
    global t
    TREE_OFFSET_Y = 575

    
    trunk_rect = pygame.Rect(WIDTH//2 - 15, TREE_OFFSET_Y, 30, 40)
    pygame.draw.rect(surface, (120, 70, 40), trunk_rect)

    
    green = (20, 120, 40)

    layer1 = [(WIDTH//2, TREE_OFFSET_Y - 100),
              (WIDTH//2 - 80, TREE_OFFSET_Y),
              (WIDTH//2 + 80, TREE_OFFSET_Y)]

    layer2 = [(WIDTH//2, TREE_OFFSET_Y - 160),
              (WIDTH//2 - 60, TREE_OFFSET_Y - 70),
              (WIDTH//2 + 60, TREE_OFFSET_Y - 70)]

    layer3 = [(WIDTH//2, TREE_OFFSET_Y - 210),
              (WIDTH//2 - 40, TREE_OFFSET_Y - 130),
              (WIDTH//2 + 40, TREE_OFFSET_Y - 130)]

    pygame.draw.polygon(surface, green, layer1)
    pygame.draw.polygon(surface, green, layer2)
    pygame.draw.polygon(surface, green, layer3)

    
    base_colors = [(255, 80, 80), (255, 255, 100), (120, 200, 255), (255, 150, 255)]
    light_positions = [
        (WIDTH//2 - 40, TREE_OFFSET_Y - 30),
        (WIDTH//2 + 30, TREE_OFFSET_Y - 40),
        (WIDTH//2 - 10, TREE_OFFSET_Y - 80),
        (WIDTH//2 + 20, TREE_OFFSET_Y - 110),
        (WIDTH//2 - 25, TREE_OFFSET_Y - 130),
    ]

    for i, pos in enumerate(light_positions):
        
        pulse = (math.sin(t * (2 + i * 0.5)) + 1) / 2  
        brightness = 0.5 + pulse * 0.5              

        r, g, b = base_colors[i % len(base_colors)]
        color = (int(r * brightness), int(g * brightness), int(b * brightness))

        pygame.draw.circle(surface, color, pos, 6)
        pygame.draw.circle(surface, color, pos, 12, 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += 0.05 

    draw_sky(screen)
    draw_sun_with_rays(screen)
    draw_clouds(screen)

    pygame.draw.circle(screen, (180, 200, 255), GLOBE_CENTER, GLOBE_RADIUS + 10, 5)
    pygame.draw.circle(screen, (230, 240, 255), GLOBE_CENTER, GLOBE_RADIUS, 2)

    draw_tree(screen)

    for flake in snowflakes:
        flake.update()
        flake.draw(screen)

    pygame.draw.rect(screen, (120, 80, 50),
                     (WIDTH//2 - 300, HEIGHT//2 + 250, 1000, 80),
                     border_radius=20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

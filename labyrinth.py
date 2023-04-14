import pygame
import sys
import random

# Oyun penceresi boyutları
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Labirent düzeyi boyutları
LEVEL_WIDTH = 10
LEVEL_HEIGHT = 10

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Oyun nesnesi
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Labirent Oyunu")
        self.clock = pygame.time.Clock()
        self.player = Player(0, 0) # Oyuncu nesnesi
        self.level = Level() # Labirent düzeyi nesnesi

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.update() # Oyuncu güncelleniyor

            self.screen.fill(WHITE)
            self.level.draw(self.screen) # Labirent düzeyi ekrana çiziliyor
            self.player.draw(self.screen) # Oyuncu ekrana çiziliyor
            pygame.display.flip()
            self.clock.tick(60)

# Labirent düzeyi nesnesi
class Level:
    def __init__(self):
        self.grid = [[random.choice([0, 1]) for _ in range(LEVEL_WIDTH)] for _ in range(LEVEL_HEIGHT)]

    def draw(self, screen):
        for y in range(LEVEL_HEIGHT):
            for x in range(LEVEL_WIDTH):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, BLACK, pygame.Rect(x * 40, y * 40, 40, 40))

# Oyuncu nesnesi
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 1
        elif keys[pygame.K_DOWN]:
            self.y += 1
        elif keys[pygame.K_LEFT]:
            self.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.x += 1

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.x*40, self.y * 40, 40, 40))

if __name__ == "__main__":
    game = Game()
    game.run()

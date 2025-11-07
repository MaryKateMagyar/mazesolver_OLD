import pygame
import constants as c
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event .get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(c.BLACK)
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

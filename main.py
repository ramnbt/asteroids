import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import * 
from shots import *
import sys 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    Shot.container = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    

    asteroid_field = AsteroidField()

    my_player = Player(x, y)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill("black")
        updatable.update(dt)
        for things in asteroids:
            if things.collision(my_player):
                sys.exit("Game Over!")
        for things in drawable:
            things.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60))/1000
    

    """print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")"""

    


if __name__ == "__main__":
    main()

import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

class Game:
    def __init__(self):
        # Initialize Pygame and set up the display
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Pygame Event Handling')
        self.clock = pygame.time.Clock()
        self._running = True

        # Example player object with a direction attribute
        self.player = Player()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

        keys = pygame.key.get_pressed()
        
        if keys[K_RIGHT]:
            self.player.d = 0
        elif keys[K_LEFT]:
            self.player.d = 1
        elif keys[K_UP]:
            self.player.d = 2
        elif keys[K_DOWN]:
            self.player.d = 3

    def run(self):
        while self._running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        # Update game state (e.g., move player based on direction)
        pass

    def render(self):
        # Render the game state to the screen
        self.screen.fill((0, 0, 0))  # Clear screen with black
        # Render player, etc.
        pygame.display.flip()

class Player:
    def __init__(self):
        self.d = -1  # Default direction

if __name__ == "__main__":
    game = Game()
    game.run()

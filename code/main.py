from settings import * 


from sprites import *

class Game:
    
    def __init__(self) -> None:
        
        # general setup 
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.running = True
        pygame.display.set_caption("PONG")
        self.clock = pygame.time.Clock()
        
        # sprites groups
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()
        
        
        self.player = Player(POS['player'],(self.all_sprites,self.paddle_sprites))
        self.ball = Ball(self.all_sprites,self.paddle_sprites)
        
        
    def run(self):
        
        
        # Game Loop
        while self.running:
            # Delta Time 
            dt = self.clock.tick() / 1000
            
            
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Draw The Game
            self.display_surface.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surface)
            
            #update sprite 
            self.all_sprites.update(dt)
            # Update The display
            pygame.display.update()
            
        pygame.quit()
        
        
if __name__ == '__main__':
    # Run the game 
    game = Game()
    game.run()
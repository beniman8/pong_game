from settings import * 





class Game:
    
    def __init__(self) -> None:
        
        # general setup 
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.running = True
        pygame.display.set_caption("PONG")
        self.clock = pygame.time.Clock()
        
        
        
    def run(self):
        
        
        # Game Loop
        while self.running:
            # Delta Time 
            dt = self.clock.tick()
            
            
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Draw The Game
            self.display_surface.fill('black')
            
            
            # Update The display
            pygame.display.update()
            
        pygame.quit()
        
        
if __name__ == '__main__':
    # Run the game 
    game = Game()
    game.run()
from settings import * 
import json
from groups import AllSprites
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
        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()
        
        
        self.player = Player(POS['player'],(self.all_sprites,self.paddle_sprites))
        self.ball = Ball(self.all_sprites,self.paddle_sprites,self.update_score)
        Opponent(POS['opponent'],self.ball,(self.all_sprites,self.paddle_sprites))
        
        # score 
        try:
            with open(join('data','score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            
            self.score = {'player':0,'opponent':0}
        self.font = pygame.font.Font(None,160)
        
    
    def display_score(self):
        
        #player
        player_surf = self.font.render(str(self.score['player']),True,COLORS['bg detail'])
        player_rect = player_surf.get_frect(center =(WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT /2))
        self.display_surface.blit(player_surf,player_rect)
        
        #opponent
        opponent_surf = self.font.render(str(self.score['opponent']),True,COLORS['bg detail'])
        opponent_rect = opponent_surf.get_frect(center =(WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT /2))
        self.display_surface.blit(opponent_surf,opponent_rect)       
        
        
        #line separator
        pygame.draw.line(self.display_surface,COLORS['bg detail'],(WINDOW_WIDTH/2,0),(WINDOW_WIDTH/2,WINDOW_HEIGHT),10)
        
    def update_score(self,side):
        self.score['player' if side == 'player' else 'opponent'] +=1
        
    def run(self):
        
        
        # Game Loop
        while self.running:
            # Delta Time 
            dt = self.clock.tick() / 1000
            
            
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('data','score.txt'),'w') as score_file:
                        json.dump(self.score,score_file)
                    
            # Draw The Game
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()
            
            #update sprite 
            self.all_sprites.update(dt)
            # Update The display
            pygame.display.update()
            
        pygame.quit()
        
        
if __name__ == '__main__':
    # Run the game 
    game = Game()
    game.run()
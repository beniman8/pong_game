from settings import *

from random import choice, uniform

class Player(pygame.sprite.Sprite):
    
    def __init__(self,pos, groups) -> None:
        super().__init__(groups)
        
        # image 
        self.image = pygame.Surface(SIZE['paddle'],pygame.SRCALPHA)
        pygame.draw.rect(self.image,COLORS['paddle'],pygame.FRect((0,0),SIZE['paddle']),0,4)
        #rect and movement
        self.rect = self.image.get_frect(center=pos)
        #self.image.fill(COLORS['paddle'])
        
        
        # Movement 
        self.direction = 0
        self.speed= SPEED['player']


    def move(self,dt):
        
        self.rect.centery += self.direction * self.speed* dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    
    def get_direction(self):
        
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        
        
        
    def update(self, dt) -> None:
        self.get_direction()
        self.move(dt)
        

        return super().update()
    
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, groups, paddle_sprites) -> None:
        super().__init__(groups)
        
        self.image = pygame.Surface(SIZE['ball'],pygame.SRCALPHA)
        pygame.draw.circle(self.image,COLORS['ball'],(SIZE['ball'][0]/2,SIZE['ball'][1]/2),SIZE['ball'][0]/2)
        #self.image.fill(COLORS['ball'])
        
        # Movement 
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2(choice((1,-1)),uniform(0.7,0.8) * choice((-1,1)))
        self.speed= SPEED['ball']

    def move(self,dt):
        self.rect.center += self.direction * SPEED['ball'] * dt
        
    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top=0
            self.direction.y *= -1
            
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom=WINDOW_HEIGHT
            self.direction.y *= -1   
            
        if self.rect.right <= 0:
            self.rect.right=0
            self.direction.x *= -1      
                    
        if self.rect.left >= WINDOW_WIDTH:
            self.rect.left=WINDOW_WIDTH
            self.direction.x *= -1                  
    def update(self, dt) -> None:
        self.wall_collision()
        self.move(dt)
        

        return super().update()
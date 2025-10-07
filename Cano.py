import pygame
import random

class Cano:
    
    def __init__(self, screen: pygame.Surface, up: bool):
        self.screen = screen
        self.vel_x = 500
        widht = 100
        
        height_at_screen = random.randrange(0, self.screen.get_height() + 1) # valor aleatorio do local da tela -> se for menor: maior o cano
        height = abs(self.screen.get_height() - height_at_screen) # altura do cano
        
        if (up):
            self.rect = pygame.Rect(100, self.screen.get_height(), widht, height)
        else:
            self.rect = pygame.React(100, 0, widht, self.height)
            
    def update_height(self):
        height_at_screen = random.randrange(0, self.screen.get_height() + 1) # valor aleatorio do local da tela -> se for menor: maior o cano
        self.rect.height = abs(self.screen.get_height() - height_at_screen) # altura do cano
    
    def animation(self):
        # ultrapasosu o limite
        if self.rect.x < 0:
            self.rect.x = self.screen.get_width()
            self.rect.y = random.randrange(1, self.screen.get_height())
            
        pygame.draw.rect(self.screen, "green", self.rect)
             
    def walk(self, dt: float):
        if self.vel_x < 1000:
            self.vel_x += 0.10
            
        self.rect.x -= self.vel_x * dt
    
    def get_height(self):
        return self.rect.y
import pygame
import random

class Cano:
    
    def __init__(self, screen: pygame.Surface, bottom: bool):
        self.screen = screen
        self.vel_x = 500
        self.widht = 100 # largura
        self.bottom = bottom
        self.start_height()
        
    def start_height(self):
        height_at_screen = random.randrange(30, self.screen.get_height() + 1) # valor aleatorio do local da tela -> se for menor: maior o cano
                
        if self.bottom:
            self.rect = pygame.Rect(self.screen.get_width(), self.screen.get_height() - height_at_screen, self.widht, height_at_screen)
        else: # down
            self.rect = pygame.Rect(self.screen.get_width(), 0, self.widht, height_at_screen)
            
    def animation(self):
        pygame.draw.rect(self.screen, "green", self.rect)
    
             
    def walk(self, dt: float) -> bool:
        if self.vel_x < 900:
            self.vel_x += 0.10
            
        self.rect.x -= self.vel_x * dt
        
        # ultrapassou do limite
        if self.rect.x < 0:
            self.rect.x = self.screen.get_width() # volta para o inicio
            return True
        
        return False
    
    def get_height(self):
        return self.rect.y
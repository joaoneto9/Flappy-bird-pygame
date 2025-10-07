import pygame
import random

class Cano:
    
    def __init__(self, screen: pygame.Surface, botton: bool):
        self.screen = screen
        self.vel_x = 500
        self.widht = 100 # largura
        self.botton = botton
        self.start_height()
        
    def start_height(self):
        height_at_screen = random.randrange(0, self.screen.get_height() + 1) # valor aleatorio do local da tela -> se for menor: maior o cano
                
        if self.botton:
            self.rect = pygame.Rect(self.screen.get_width(), self.screen.get_height() - height_at_screen, self.widht, height_at_screen)
        else: # down
            self.rect = pygame.Rect(self.screen.get_width(), 0, self.widht, height_at_screen)
            
    def update_height(self):
        if self.botton:
            self.rect.height = random.randrange(0, self.screen.get_height() + 1)
            self.rect.y = self.screen.get_height() - self.rect.height
        else: # down 
            self.rect.height = random.randrange(0, self.screen.get_height() + 1)
            
    def animation(self):
        # ultrapasosu o limite
        if self.rect.x < 0:
            self.update_height()
            self.rect.x = self.screen.get_width() # volta para o inicio
            
        pygame.draw.rect(self.screen, "green", self.rect)
             
    def walk(self, dt: float):
        if self.vel_x < 1000:
            self.vel_x += 0.10
            
        self.rect.x -= self.vel_x * dt
    
    def get_height(self):
        return self.rect.y
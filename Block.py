import pygame
import random
from Cano import Cano 

class Block:
    
    def __init__(self, screen: pygame.Surface, gap: int = 200):
        self.screen = screen
        self.gap = gap
        
        self.top_cano = Cano(screen, bottom=False)
        self.bottom_cano = Cano(screen, bottom=True)
        
        self.adjust_gap()
        
    def adjust_gap(self):
        """
        Ajusta a altura dos dois canos para garantir o gap correto
        """
        # Sorteia uma altura para o cano de baixo
        max_height = self.screen.get_height() - self.gap
        bottom_height = random.randrange(50, max_height)
        top_height = self.screen.get_height() - bottom_height - self.gap

        # Cano de baixo
        self.bottom_cano.rect.height = bottom_height
        self.bottom_cano.rect.y = self.screen.get_height() - bottom_height
        self.bottom_cano.rect.x = self.screen.get_width()  # posição inicial fora da tela

        # Cano de cima
        self.top_cano.rect.height = top_height
        self.top_cano.rect.y = 0
        self.top_cano.rect.x = self.screen.get_width()  # mesma posição horizontal do cano de baixo
        
    def walk(self, df):
        self.top_cano.walk(df)
        
        if self.bottom_cano.walk(df):
            self.adjust_gap()
            
    def animation(self):
        self.top_cano.animation()
        self.bottom_cano.animation()
        
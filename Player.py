import pygame

class Player:
    
    def __init__(self, name: str, screen: pygame.Surface):
        self.name = name
        self.screen = screen
        self.player_pos = pygame.Vector2(100, screen.get_height() / 2)
        self.vel_y = 0
        
    def gravity_decrease_height(self):
        self.vel_y += 0.10
        self.player_pos.y += self.vel_y
    
    def animation(self):
        pygame.draw.circle(self.screen, "red", self.player_pos, 40)
        
    def jump(self, dt: float):
        self.player_pos.y -= 500 * dt 
        self.vel_y = 0
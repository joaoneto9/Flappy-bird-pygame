import pygame

class Player:
    
    def __init__(self, name: str, screen: pygame.Surface):
        self.name = name
        self.screen = screen
        self.radius = 40
        self.player_pos = pygame.Vector2(100, screen.get_height() / 2)
        self.vel_y = 0
        
    def gravity_decrease_height(self):
        self.vel_y += 0.10
        self.player_pos.y += self.vel_y
    
    def animation(self):
        pygame.draw.circle(self.screen, "red", self.player_pos, self.radius)
        
    def jump(self, dt: float):
        self.player_pos.y -= 500 * dt 
        self.vel_y = 0
    
    def check_limits(self):
        if self.player_pos.y < 0 or self.player_pos.y > self.screen.get_height():
            return True
        
        return False
    
    def get_cordenates(self) -> dict:
        """
        Retorna as coordenadas ocupadas pelo player como listas de X e Y.
        Considera o player como um círculo de raio 40.
        """
        x_center = int(self.player_pos.x)
        y_center = int(self.player_pos.y)
        
        # Cria listas de X e Y dentro do círculo (aproximação em quadrado)
        x_coords = list(range(x_center - self.radius, x_center + self.radius + 1))
        y_coords = list(range(y_center - self.radius, y_center + self.radius + 1))
        
        return {"x": x_coords, "y": y_coords}
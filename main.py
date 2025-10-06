import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True

vel_y = 0
vel_x = 5
dt = 0
gravity = 0.05

# a posicao esta no centro, pois divide a altura e a largurna metade, meio que (x / 2, y /2)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

print("inicio do jogo")
# funcionamento do jogo
while running:
    for event in pygame.event.get(): # para cada ação
        if event.type == pygame.QUIT: # se apertar X paar fecahar o jogo
            running = False
    
    screen.fill("black") # não netendi
    
    pygame.draw.circle(screen, "red", player_pos, 40)
    
    keys = pygame.key.get_pressed() # teclas pressionadas
    
    # apertou 'w'
    if keys[pygame.K_SPACE]:
        player_pos.y -= 500 * dt
        vel_y = 0
    
    # acao da gravidade
    vel_y += gravity
    player_pos.y += vel_y
            
    # Renderizar o Jogo aqui
    
    # flip() coloca todo o trabalho na tela
    pygame.display.flip()
    
    # limita o FPS para 60
    # dt é o delta time em segundos desde o último frame
    dt = clock.tick(60) / 500
    
print("fim do jogo")
pygame.quit() 



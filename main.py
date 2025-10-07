import pygame
from Player import Player
from Block import Block

# name = input("escolha o seu nome: ")

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


running = True

# iniciando um objeto player
player = Player("name", screen)
block = Block(screen)

print("inicio do jogo")
# funcionamento do jogo
while running:
    for event in pygame.event.get(): # para cada ação
        if event.type == pygame.QUIT: # se apertar X paar fecahar o jogo
            running = False
            
    # limita o FPS para 60
    # dt é o delta time em segundos desde o último frame
    dt = clock.tick(60) / 500
    
    screen.fill("black") # não netendi
    
    player.animation()
    block.animation()
    
    # pygame.draw.rect(screen, "green", rect)
    
    keys = pygame.key.get_pressed() # teclas pressionadas
    
    # apertou 'w'
    if keys[pygame.K_SPACE]:
        player.jump(dt)
    
    # acao da gravidade e atualizacao do eixo x dos canos
    player.gravity_decrease_height()
    block.walk(dt)
    
    # flip() coloca todo o trabalho na tela
    pygame.display.flip()
    
print("fim do jogo")
pygame.quit() 



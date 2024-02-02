import pygame
import sys
from button import Button

pygame.init()

WIDTH, HEIGHT = 500, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_gr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Buttons')

def main_menu():
    green_button = Button(WIDTH/2-(252/2),
                      100,
                      252,
                      74,
                      "GREEN",
                      "green_button.png",
                      "green_button_hover.png",
                      "green_button_clicked.png",
                      "click.mp3"
                      )
    blue_button = Button(WIDTH/2-(252/2),
                        200,
                        252,
                        74,
                        "BLUE",
                        "blue_button.png",
                        "blue_button_hover.png",
                        "blue_button_clicked.png",
                        "click.mp3"
                        )
    red_button = Button(WIDTH/2-(252/2),
                        300,
                        252,
                        74,
                        "RED",
                        "red_button.png",
                        "red_button_hover.png",
                        "red_button_clicked.png",
                        "click.mp3"
                        )

    buttons = [green_button, blue_button, red_button]
    running = True
    while running:
        screen.fill(pygame.Color('#afeeee'))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("BUTTONS",
                                   True,
                                   ('#002654'))
        text_rect = text_surface.get_rect(center=(250,50))
        screen.blit(text_surface, text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.USEREVENT and\
                        event.button == green_button:
                print("Green button clicked!")
                green()
            
            if event.type == pygame.USEREVENT and\
                        event.button == blue_button:
                print("Blue button clicked!")
                blue()
            
            if event.type == pygame.USEREVENT and\
                        event.button == red_button:
                print("Red button clicked!")
                red()
            
            for button in buttons:
                button.handle_event(event)
       
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            button.check_hover(mouse_pos)
            button.draw(screen)
        pygame.display.flip()
        
        
def green():
    green_button = Button(WIDTH/2-(252/2),
                      200,
                      252,
                      74,
                      "GREEN",
                      "green_button.png",
                      "green_button_hover.png",
                      "green_button_clicked.png",
                      "click.mp3"
                      )    
    running = True
    while running:
        screen.fill(pygame.Color('#1f5c61'))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("GREEN",
                                   True,
                                   ('#002654'))
        text_rect = text_surface.get_rect(center=(250,50))
        screen.blit(text_surface, text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.USEREVENT and\
                        event.button == green_button:
                main_menu()
                                
            green_button.handle_event(event)
            
        green_button.check_hover(pygame.mouse.get_pos())
        green_button.draw(screen)
           
        pygame.display.flip()

def blue():
    blue_button = Button(WIDTH/2-(252/2),
                        200,
                        252,
                        74,
                        "BLUE",
                        "blue_button.png",
                        "blue_button_hover.png",
                        "blue_button_clicked.png",
                        "click.mp3"
                        )    
    running = True
    while running:
        screen.fill(pygame.Color('#005b91'))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("BLUE",
                                   True,
                                   ('#002654'))
        text_rect = text_surface.get_rect(center=(250,50))
        screen.blit(text_surface, text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.USEREVENT and\
                        event.button == blue_button:
                main_menu()
                                
            blue_button.handle_event(event)
            
        blue_button.check_hover(pygame.mouse.get_pos())
        blue_button.draw(screen)
           
        pygame.display.flip()

def red():
    red_button = Button(WIDTH/2-(252/2),
                        200,
                        252,
                        74,
                        "RED",
                        "red_button.png",
                        "red_button_hover.png",
                        "red_button_clicked.png",
                        "click.mp3"
                        )    
    running = True
    while running:
        screen.fill(pygame.Color('#d52b1e'))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("RED",
                                   True,
                                   ('#002654'))
        text_rect = text_surface.get_rect(center=(250,50))
        screen.blit(text_surface, text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.USEREVENT and\
                        event.button == red_button:
                main_menu()
                                
            red_button.handle_event(event)
            
        red_button.check_hover(pygame.mouse.get_pos())
        red_button.draw(screen)
           
        pygame.display.flip()

if __name__ == '__main__':
    
    main_menu()
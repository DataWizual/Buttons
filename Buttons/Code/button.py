import pygame

class Button:
    def __init__(self, x, y, width, height, text,
                 image_path, hover_image_path=None,
                 pressed_image_path=None, sound_path=None ):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image,
                                                      (width, height))
        self.pressed_image = self.image
        if pressed_image_path:
            self.pressed_image = pygame.image.load(pressed_image_path)
            self.pressed_image = pygame.transform.scale(self.pressed_image,
                                                        (width, height))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False
        self.is_pressed = False
        
        
    def draw(self, screen):
        current_image = self.pressed_image if self.is_pressed else\
               (self.hover_image if self.is_hovered else self.image)
        screen.blit(current_image, self.rect.topleft)
        
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, ('#002654'))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and\
                                                          self.is_hovered:
            if self.sound:
                self.sound.play()
            self.is_pressed = True
            pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                         button=self))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_pressed = False


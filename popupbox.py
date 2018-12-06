import pygame
from time import sleep
def display_box(screen, message,font_position_x,font_position_y):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.SysFont("Time New Roman",30)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (0,0,0)),
                (font_position_x,font_position_y))
  

def ask(event, current_string):
  "ask(screen, question) -> answer"
  pygame.font.init()
  
  unuse_case=[pygame.K_BACKSPACE,pygame.K_RETURN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFTBRACKET,pygame.K_RIGHTBRACKET]
  
  if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE and len(current_string)>0:
            del current_string[-1]
        elif event.key not in unuse_case:
            current_string.append(chr(event.key))
            sleep(0.1)
  
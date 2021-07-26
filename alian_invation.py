import sys
import pygame

class AlienInvasaion:

  def __init__(self):
    pygame.init()

    self.screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("エイリアン侵略")

  def run_game(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      pygame.display.flip()

if __name__ == '__main__':
  ai = AlienInvasaion()
  ai.run_game()
import sys
import pygame

from setting import Settings

class AlienInvasaion:

  def __init__(self):
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("エイリアン侵略")

    self.bg_color = (self.settings.bg_color)

  def run_game(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      self.screen.fill(self.bg_color)

      pygame.display.flip()

if __name__ == '__main__':
  ai = AlienInvasaion()
  ai.run_game()
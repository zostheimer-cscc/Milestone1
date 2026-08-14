"""
Program Name: Alien Invasion - Main

Author: Zachary Ostheimer

Purpose: This program runs the main game loop for Alien Invasion

Starter Code: Based on the in class Alien Invasion tutorial

Date: 08/14/2026
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal


class AlienInvasion:
    #manages the game setup, the main loop, and all events

    def __init__(self) -> None:
        #start pygame and build the screen, ship, and sound
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_w, self.settings.screen_h)
        )
        #scale the background to fill the screen

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))

    def run_game(self) -> None:
        #run the main game loop until the player quits
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self) -> None:
        #watch for quit, key press, and key release events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        #start moving or fire when a key is pressed
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        #stop moving when a movement key is released
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False

    def _update_screen(self) -> None:
        #draw the background and ship, then flip the display
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

"""
Program Name: Alien Invasion Settings

Author: Zachary Ostheimer

Purpose: This module stores all the settings for the game

Starter Code: Based on the in class Alien Invasion tutorial

Date: 08/12/2026
"""

from pathlib import Path

#gets the folder this file is in so assets load from anywhere
BASE_PATH = Path(__file__).parent


class Settings:
    #holds every setting the game needs in one place

    def __init__(self) -> None:
        #set up screen, ship, bullet, and alien settings
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = BASE_PATH / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = BASE_PATH / 'Assets' / 'images' / 'ship2_no_bg_.png'
        self.ship_w = 60
        self.ship_h = 40
        self.ship_speed = 5
        #ship is wider than tall now since it points right

        self.bullet_file = BASE_PATH / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = BASE_PATH / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 80
        self.bullet_h = 25
        #bullet is wider than tall since it flies sideways
        self.bullet_amount = 5

        self.alien_file = BASE_PATH / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 5
        self.fleet_direction = 1
        self.fleet_drop_speed = 40

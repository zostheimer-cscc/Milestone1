"""
Program Name: Alien Invasion - Settings

Author: Zachary Ostheimer

Purpose: This module stores all the static settings for the game

Starter Code: Based on the in class Alien Invasion tutorial

Date: 08/14/2026
"""

from pathlib import Path

#gets the folder this file is in so assets load from anywhere
BASE_PATH = Path(__file__).parent


class Settings:
    #holds every setting the game needs in one place

    def __init__(self) -> None:
        #set up screen, ship, and bullet settings
        self.name: str = 'Alien Invasion'
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60
        self.bg_file = BASE_PATH / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = BASE_PATH / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w: int = 60
        self.ship_h: int = 40
        self.ship_speed: int = 5
        #ship is wider than tall now since it points right

        self.bullet_file = BASE_PATH / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = BASE_PATH / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed: int = 7
        self.bullet_w: int = 80
        self.bullet_h: int = 25
        #bullet is wider than tall since it flies sideways
        self.bullet_amount: int = 5

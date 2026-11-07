import pygame
import os
import sys

# This thing is used for loading assets (.mp3, .png, etc.) so that the final build won't scream errors 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

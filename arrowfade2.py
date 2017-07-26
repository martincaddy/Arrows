import unicornhat, signal
from time import sleep

bright = unicornhat.brightness

def show():
    unicornhat.show()
    sleep(0.1)

def arrowfade():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0)], [(255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    bright(0.1)
    show()
    bright(0.2)
    show()
    bright(0.3)
    show()
    bright(0.4)
    show()
    bright(0.5)
    show()
    bright(0.6)
    show()
    bright(0.7)
    show()
    bright(0.8)
    show()
    bright(0.9)
    show()
    bright(1)
    show()
    bright(0.9)
    show()
    bright(0.8)
    show()
    bright(0.7)
    show()
    bright(0.7)
    show()
    bright(0.6)
    show()
    bright(0.5)
    show()
    bright(0.4)
    show()
    bright(0.3)
    show()
    bright(0.2)
    show()
    bright(0.1)
    show()
    unicornhat.clear()
    unicornhat.show()
   
arrowfade()
    

        
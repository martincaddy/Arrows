import unicornhat, signal
from time import sleep

bright = unicornhat.brightness

shine = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
i = iter


def show():
    unicornhat.show()
    sleep(0.1)
    
def arrowshine():    
        pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0)], [(255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
        unicornhat.set_pixels(pixels)
        for i in shine:
            bright(i)
            show()
            
arrowshine()
    

        
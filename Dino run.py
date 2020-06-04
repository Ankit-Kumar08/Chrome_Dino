import pyautogui
from PIL import Image, ImageGrab
from time import sleep
#from numpy import asarray


def take_ss():
    image = ImageGrab.grab().convert('L')
    return image

def hit(key):
    pyautogui.press(key)

def isCollide(data):
    for i in range(280, 316):
        for j in range(590, 676):
           if data[i, j] > 100:
               return True
    return False


sleep(1)
while True:
    image = take_ss()
    data = image.load()
    if isCollide(data):
        hit('up')





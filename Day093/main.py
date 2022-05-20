import pyautogui
from PIL import ImageGrab
import time


def click(key):
    pyautogui.keyDown(key)
    return


def check_obstacles(data):
    for xcor in range(760, 790):
        for ycor in range(270, 295):
            if data[xcor, ycor] < 100:
                click("down")
                return

    for xcor in range(710, 790):
        for ycor in range(300, 325):
            if data[xcor, ycor] < 100:
                click("up")
                return
    return


if __name__ == "__main__":
    time.sleep(3)
    click('up')

    while True:
        grayscale_image = ImageGrab.grab().convert('L')
        screen = grayscale_image.load()
        check_obstacles(screen)

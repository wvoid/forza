from mss import mss
import cv2 as cv2
import numpy as np
import uuid
import os

game_area = {"left": 0, "top": 0, "width": 1280, "height": 720}
capture = mss()


def collect_frames():
    filename = os.path.join('data', str(uuid.uuid1()))
    gamecap = np.array(capture.grab(game_area))
    cv2.imwrite(f'{filename}.jpg', gamecap)



def button_presses():


if __name__ == "__main__":
    # run some function here
    collect_frames()

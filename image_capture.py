import time

from mss import mss
import cv2 as cv2
import numpy as np
import uuid
import os
from getkeys import key_check

w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]
game_area = {"left": 0, "top": 0, "width": 1280, "height": 720}
capture = mss()


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output


def collect_frames():
    # filename = os.path.join('data', str(uuid.uuid1()))
    gamecap = np.array(capture.grab(game_area))
    gamecap_gray = cv2.cvtColor(gamecap, cv2.COLOR_RGBA2GRAY)
    # cv2.imwrite(f'{filename}.jpg', gamecap)
    return gamecap_gray


def collect_keys():
    keys = key_check()
    output = keys_to_output(keys)
    return output
    # print(output)


if __name__ == "__main__":
    # run some function here
    # collect_frames()
    np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
    data_train = []
    i = 0
    paused = False
    while True:
        if not paused:
            time.sleep(0.06)
            filename = os.path.join('data', 'data_train_{}'.format(i))
            # time.sleep(1)
            data_x = collect_frames()
            data_y = collect_keys()
            data_train.append([data_x, data_y])
            if len(data_train) % 100 == 0:
                print('collecting {}...'.format(i))
            if len(data_train) % 1000 == 0:
                np.save(filename, data_train)
                print('{} save successfully!'.format(filename))
                data_train = []
                i += 1

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('continue...')
                time.sleep(1)
            else:
                print('pauseing!')
                paused = True
                time.sleep(1)

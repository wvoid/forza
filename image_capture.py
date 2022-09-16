import time

from mss import mss
import cv2 as cv2
import numpy as np
import os
from getkeys import key_check
from torchvision import transforms
from PIL import Image

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


pipe = transforms.Compose([transforms.CenterCrop([600, 1000]), transforms.Resize([224])])


def collect_frames():
    # filename = os.path.join('data', str(uuid.uuid1()))
    gamecap = np.array(capture.grab(game_area))
    gamecap_gray = cv2.cvtColor(gamecap, cv2.COLOR_RGBA2GRAY)
    gamecap_gray = pipe(Image.fromarray(gamecap_gray))
    gamecap_gray = np.reshape(gamecap_gray, (1,) + np.array(gamecap_gray).shape)
    # cv2.imwrite(f'{filename}.jpg', gamecap)
    return gamecap_gray


def collect_keys():
    keys = key_check()
    output = keys_to_output(keys)
    return np.array(output)
    # print(output)


if __name__ == "__main__":
    # run some function here
    # collect_frames()
    time.sleep(2)
    np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
    # data_train = []
    x = []
    y = []
    i = 0
    paused = False
    while True:
        if not paused:
            time.sleep(0.1)
            filename = os.path.join('data', 'data_train_{}'.format(i))
            # time.sleep(1)
            data_x = collect_frames()
            data_y = collect_keys()
            x.append(data_x)
            y.append(data_y)
            if len(x) % 100 == 0:
                print('collecting {}...'.format(i))
            if len(x) % 500 == 0:
                np.savez(filename, image=x, label=y)
                print('{} save successfully!'.format(filename))
                x = []
                y = []
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

import pyautogui
import time

# gives us time to get situated in the game
for i in list(range(4))[::-1]:
    print(i + 1)
    time.sleep(1)


def p0():
    pyautogui.keyDown('w')
    time.sleep(0.1)
    pyautogui.keyUp('w')


def p1():
    pyautogui.keyDown('s')
    time.sleep(0.1)
    pyautogui.keyUp('s')


def p2():
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')


def p3():
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')


def p4():
    pyautogui.keyDown('w')
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')


def p5():
    pyautogui.keyDown('w')
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('w')
    pyautogui.keyUp('d')


def p6():
    pyautogui.keyDown('s')
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    pyautogui.keyUp('a')


def p7():
    pyautogui.keyDown('s')
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    pyautogui.keyUp('d')


def p8():
    time.sleep(0.1)


# print('down')
# pyautogui.keyDown('w')
# pyautogui.keyDown('d')
# time.sleep(4)
# print('up')
# pyautogui.keyUp('w')
# pyautogui.keyUp('d')
switch = {
    0: p0,
    1: p1,
    2: p2,
    3: p3,
    4: p4,
    5: p5,
    6: p6,
    7: p7,
    8: p8
}

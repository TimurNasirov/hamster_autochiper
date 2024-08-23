print(f'Starting utility "hamsterkombat cipher V1.5"...')

from config import *
from keyboard import add_hotkey
import pyautogui as pag
from time import sleep
from sys import argv
from random import uniform

def _long():
    pag.mouseDown()
    sleep(DELAY_IN_LONG_TAP)
    pag.mouseUp()

def short():
    pag.click()

def a():
    print('write A')
    short()
    sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_LETTER)

def b():
    print('write B')
    _long()
    for i in range(3):
        sleep(DELAY_PER_CLICK)
        short()
    sleep(DELAY_PER_LETTER)

def c():
    print('write C')
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        _long()
        sleep(DELAY_PER_CLICK)
        short()
    sleep(DELAY_PER_LETTER)

def d():
    print('write D')
    _long()
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        short()
    sleep(DELAY_PER_LETTER)

def e():
    print('write E')
    short()
    sleep(DELAY_PER_LETTER)

def f():
    print('write F')
    for i in range(2):
        short()
        sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_LETTER)

def g():
    print('write G')
    for i in range(2):
        _long()
        sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_LETTER)

def h():
    print('write H')
    for i in range(4):
        short()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def i():
    print('write I')
    for i in range(2):
        short()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def j():
    print('write J')
    short()
    for i in range(3):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_LETTER)

def k():
    print('write K')
    _long()
    sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_LETTER)

def l():
    print('write L')
    short()
    sleep(DELAY_PER_CLICK)
    _long()
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        short()
    sleep(DELAY_PER_LETTER)

def m():
    print('write M')
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_LETTER)

def n():
    print('write N')
    _long()
    sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_LETTER)

def o():
    print('write O')
    for i in range(3):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_LETTER)

def p():
    print('write P')
    short()
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_LETTER)

def q():
    print('write Q')
    for i in range(2):
        _long()
        sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_LETTER)

def r():
    print('write R')
    short()
    sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_LETTER)

def s():
    print('write S')
    for i in range(3):
        short()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def t():
    print('write T')
    _long()
    sleep(DELAY_PER_LETTER)

def u():
    print('write U')
    for i in range(2):
        short()
        sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_LETTER)

def v():
    print('write V')
    for i in range(3):
        short()
        sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_LETTER)

def w():
    print('write W')
    short()
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_LETTER)

def x():
    print('write X')
    _long()
    sleep(DELAY_PER_CLICK)
    for i in range(2):
        short()
        sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_LETTER)

def y():
    print('write Y')
    _long()
    sleep(DELAY_PER_CLICK)
    short()
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_LETTER)

def z():
    print('write Z')
    for i in range(2):
        _long()
        sleep(DELAY_PER_CLICK)
    for i in range(2):
        short()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def _0():
    print('write 0')
    for i in range(5):
        _long()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def _1():
    print('write 1')
    short()
    for i in range(4):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_LETTER)

def _2():
    print('write 2')
    for i in range(2):
        short()
        sleep(DELAY_PER_CLICK)
    for i in range(3):
        _long()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def _3():
    print('write 3')
    for i in range(3):
        short()
        sleep(DELAY_PER_CLICK)
    for i in range(2):
        _long()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def _4():
    print('write 4')
    for i in range(4):
        short()
        sleep(DELAY_PER_CLICK)
    _long()
    sleep(DELAY_PER_LETTER)

def _5():
    print('write 5')
    for i in range(5):
        short()
        sleep(DELAY_PER_CLICK)
    sleep(DELAY_PER_LETTER)

def _6():
    print('write 6')
    _long()
    for i in range(4):
        sleep(DELAY_PER_CLICK)
        short()
    sleep(DELAY_PER_LETTER)

def _7():
    print('write 7')
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        _long()
    for i in range(3):
        sleep(DELAY_PER_CLICK)
        short()
    sleep(DELAY_PER_LETTER)

def _8():
    print('write 8')
    for i in range(3):
        sleep(DELAY_PER_CLICK)
        _long()
    for i in range(2):
        sleep(DELAY_PER_CLICK)
        short()
    sleep(DELAY_PER_LETTER)

def _9():
    print('write 9')
    for i in range(4):
        sleep(DELAY_PER_CLICK)
        _long()
    sleep(DELAY_PER_CLICK)
    short()
    sleep(DELAY_PER_LETTER)

if UNNECESSARY_DELAYS:
    sleep(uniform(0.07, 0.25))
print('Started successfully.')
try:
    if "-c" not in argv:
        print('Real-time mode enabled.')
        add_hotkey('a', a)
        add_hotkey('b', b)
        add_hotkey('c', c)
        add_hotkey('d', d)
        add_hotkey('e', e)
        add_hotkey('f', f)
        add_hotkey('g', g)
        add_hotkey('h', h)
        add_hotkey('i', i)
        add_hotkey('j', j)
        add_hotkey('k', k)
        add_hotkey('l', l)
        add_hotkey('m', m)
        add_hotkey('n', n)
        add_hotkey('o', o)
        add_hotkey('p', p)
        add_hotkey('q', q)
        add_hotkey('r', r)
        add_hotkey('s', s)
        add_hotkey('t', t)
        add_hotkey('u', u)
        add_hotkey('v', v)
        add_hotkey('w', w)
        add_hotkey('x', x)
        add_hotkey('y', y)
        add_hotkey('z', z)
        add_hotkey('1', _1)
        add_hotkey('2', _2)
        add_hotkey('3', _3)
        add_hotkey('4', _4)
        add_hotkey('5', _5)
        add_hotkey('6', _6)
        add_hotkey('7', _7)
        add_hotkey('8', _8)
        add_hotkey('9', _9)
        
        
        while True:
            pass
    else:
        print('Auto mode enabled.')
        word = argv[2]
        sleep(3)
        print('Start writing text. Do not move your mouse')
        for _i in word:
            if _i == 'a': a()
            elif _i == 'b': b()
            elif _i == 'c': c()
            elif _i == 'd': d()
            elif _i == 'e': e()
            elif _i == 'f': f()
            elif _i == 'g': g()
            elif _i == 'h': h()
            elif _i == 'i': i()
            elif _i == 'j': j()
            elif _i == 'k': k()
            elif _i == 'l': l()
            elif _i == 'm': m()
            elif _i == 'n': n()
            elif _i == 'o': o()
            elif _i == 'p': p()
            elif _i == 'q': q()
            elif _i == 'r': r()
            elif _i == 's': s()
            elif _i == 't': t()
            elif _i == 'u': u()
            elif _i == 'v': v()
            elif _i == 'w': w()
            elif _i == 'x': x()
            elif _i == 'y': y()
            elif _i == 'z': z()
            elif _i == '0': _0()
            elif _i == '1': _1()
            elif _i == '2': _2()
            elif _i == '3': _3()
            elif _i == '4': _4()
            elif _i == '5': _5()
            elif _i == '6': _6()
            elif _i == '7': _7()
            elif _i == '8': _8()
            elif _i == '9': _9()
            else:
                print('Error in letter "' + _i + '". Please check text that you write.')
                if not CONTINUE_IF_ERROR:
                    print('Disabling mode because "continuation if error" is False...')
                    if UNNECESSARY_DELAYS:
                        sleep(0.08)
                    print('Auto mode disiabled.')
                    quit()
            sleep(DELAY_PER_LETTER)
        print('Task completed: disabling mode...')
        if UNNECESSARY_DELAYS:
            sleep(0.08)
        print('Auto mode disabled.')
        quit()
        
except KeyboardInterrupt:
    if "-c" in argv:
        print('Auto mode disabled.')
    else:
        print('Real-time mode disabled.')
    if UNNECESSARY_DELAYS:
        sleep(0.04)
    print('Utility stopped by user.')
    quit()
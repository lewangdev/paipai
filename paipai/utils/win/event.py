#coding=utf8

import win32api
import win32con
import win32gui
from ctypes import Structure, windll, c_long, byref
import time

class Point(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
    def __str__(self):
        return str((self.x, self.y))

def get_mouse_point():
    pt = Point()
    windll.user32.GetCursorPos(byref(pt))
    return int(pt.x), int(pt.y)

def make_lparam(llow, lhigh):
    return lhigh << 16 | llow

def mouse_click(hwnd, x, y):
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, make_lparam(x, y))
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, make_lparam(x, y))

def key_input(hwnd, text=''):
    for c in text:
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0, 1)
        win32api.PostMessage(hwnd, win32con.WM_CHAR, ord(c), 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0, 1)



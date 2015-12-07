#coding=utf8
'''python 调用 win32 dll 抓图
   http://blog.csdn.net/dyx1024/article/details/7340903
'''
import os
import sys
import ctypes
import win32gui
import ctypes.wintypes

from PIL import ImageGrab

class RECT(ctypes.Structure):
    '''定义截图区域
    '''
    _fields_ = [('left', ctypes.c_long),
            ('top', ctypes.c_long),
            ('right', ctypes.c_long),
            ('bottom', ctypes.c_long)]
    def __str__(self):
        return str((self.left, self.top, self.right, self.bottom))

def get_window_rect(hwnd):
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect

def capture_window(hwnd):
    '''指定窗口截图
    '''
    rect = get_window_rect(hwnd)
    rectangle = (rect.left,rect.top,rect.right,rect.bottom)
    img = ImageGrab.grab(rectangle)
    return img

def capture_rect(rectangle):
    '''指定区域截图
    '''
    img = ImageGrab.grab(rectangle)
    return img


if __name__ == '__main__':
    HWND = win32gui.GetForegroundWindow()
    capture_window(HWND)


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

def capture_window(HWND):
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(HWND,ctypes.byref(rect))
    rangle = (rect.left,rect.top,rect.right,rect.bottom)
    img = ImageGrab.grab(rangle)
    return img

if __name__ == '__main__':
    HWND = win32gui.GetForegroundWindow()
    capture_window(HWND)


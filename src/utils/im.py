# coding=utf-8
""" 图片处理部分

包括截图，图片转换，文字识别等部分
"""

import win32gui
import win32ui
import win32con
from ctypes import windll

from PIL import Image

def capture_window(hwnd, client_area_only=True):
    """指定窗口截图

    http://stackoverflow.com/questions/19695214/python-screenshot-of-inactive-window-printwindow-win32gui
    """
    # 和 client_area_only=True 效果相同
    #left, upper, right, lower = win32gui.GetClientRect(hwnd)
    left, upper, right, lower = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = lower - upper

    srcdc = win32gui.GetWindowDC(hwnd)
    memdc  = win32ui.CreateDCFromHandle(srcdc)
    destdc = memdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(memdc, w, h)
    destdc.SelectObject(bmp)

    # 和 client_area_only=False 效果相同, 所以直接使用 PrintWindow
    #destdc.BitBlt((0, 0), (w, h), memdc, (0, 0), win32con.SRCCOPY)
    windll.user32.PrintWindow(hwnd,
            destdc.GetSafeHdc(),
            1 if client_area_only else 0)

    bmp_info = bmp.GetInfo()
    bmp_bits = bmp.GetBitmapBits(True)
    im = Image.frombuffer(
            'RGB',
            (bmp_info['bmWidth'], bmp_info['bmHeight']),
            bmp_bits, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(bmp.GetHandle())
    destdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, srcdc)

    return im

def capture_window_rect(hwnd, rect):
    """区域截图

    窗口 client area 部分相对位置区域截图
    """
    im_window =  capture_window(hwnd)
    return im_window.crop()


def binarization(im, threshold=None, inverse=False):
    '''对图片进行二值化操作
    '''
    # 灰度处理
    im = im.convert('L')

    w, h = im.size

    if threshold is None:
        threshold = 0
        for x in xrange(w):
            for y in xrange(h):
                threshold += im.getpixel(x, y)

        threshold /= w * h

    for x in xrange(w):
        for y in xrange(h):
            if (im.getpixel((x, y)) > threshold):
                im.putpixel((x, y), 0xFF if not inverse else 0x00)
            else:
                im.putpixel((x, y), 0x00 if not inverse else 0xFF)
    return im

if __name__ == '__main__':
    hwnd = win32gui.GetForegroundWindow()
    im = capture_window(hwnd)
    im.save('test.bmp', 'BMP')

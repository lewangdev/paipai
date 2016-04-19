# coding=utf-8
""" windows 平台下窗口截图

"""

import win32gui
import win32ui
import win32con
from ctypes import windll

from PIL import Image

def capture_window(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    w = right - left
    h = bottom - top

    srcdc = win32gui.GetWindowDC(hwnd)
    memdc  = win32ui.CreateDCFromHandle(srcdc)
    destdc = memdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(memdc, w, h)
    destdc.SelectObject(bmp)

    destdc.BitBlt((0, 0), (w, h), memdc, (0, 0), win32con.SRCCOPY)

    bmp_info = bmp.GetInfo()
    bmp_bits = bmp.GetBitmapBits(True)

    # Only works in 32bit mode,
    # 虚拟机下有可能图形不是在 32 位模式的
    im = Image.frombuffer(
            'RGB',
            (bmp_info['bmWidth'], bmp_info['bmHeight']),
            bmp_bits, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(bmp.GetHandle())
    destdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, srcdc)

    return im

def capture_inactive_window(hwnd, client_area_only=True):
    """指定窗口截图

    http://stackoverflow.com/questions/19695214/python-screenshot-of-inactive\
            -window-printwindow-win32gui
    """
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    w = right - left
    h = bottom - top

    srcdc = win32gui.GetWindowDC(hwnd)
    memdc  = win32ui.CreateDCFromHandle(srcdc)
    destdc = memdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(memdc, w, h)
    destdc.SelectObject(bmp)

    windll.user32.PrintWindow(hwnd, destdc.GetSafeHdc(), 1 if client_area_only\
            else 0)

    bmp_info = bmp.GetInfo()
    bmp_bits = bmp.GetBitmapBits(True)

    # Only works in 32bit mode,
    # 虚拟机下有可能图形不是在 32 位模式的
    im = Image.frombuffer(
            'RGB',
            (bmp_info['bmWidth'], bmp_info['bmHeight']),
            bmp_bits, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(bmp.GetHandle())
    destdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, srcdc)

    return im


def capture_rect(hwnd, rect):
    """区域截图

    窗口 client area 部分相对位置区域截图
    """
    im_window = capture_window(hwnd)
    return im_window.crop(rect)

if __name__ == '__main__':
    hwnd = win32gui.GetForegroundWindow()
    im = capture_window(hwnd)
    im.save('window.bmp', 'BMP')

    im = capture_window(hwnd)
    im.save('client.bmp', 'BMP')

import win32gui
import win32ui
import win32con

from PIL import Image

def capture_window(hwnd):
    l, t, r, b = win32gui.GetWindowRect(hwnd)
    w = r - l
    h = b - t

    srcdc = win32gui.GetWindowDC(hwnd)
    memdc  = win32ui.CreateDCFromHandle(srcdc)
    destdc = memdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(memdc, w, h)
    destdc.SelectObject(bmp)

    destdc.BitBlt((0, 0), (w, h), memdc, (0, 0), win32con.SRCCOPY)
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
    return capture_window(hwnd)

if __name__ == '__main__':
    hwnd = win32gui.GetForegroundWindow()
    im = capture_window(hwnd)
    im.save('test.bmp', 'BMP')

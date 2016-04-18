#coding=utf8

import im
import browser
import window
import time

if __name__ == '__main__':
    ie = browser.open_ie(url="http://moni.51hupai.org")
    #hwnd = window.find_sub_hwnd(ie.HWND, [("Frame Tab", 0),
    #    ("TabWindowClass", 0),
    #    ("Shell DocObject View", 0),
    #    ("Internet Explorer_Server", 0)])
    hwnd = window.find_sub_hwnd(ie.HWND, [("Frame Tab", 0)])
    print "%x" % (hwnd)

    time.sleep(3)

    for i in xrange(100):
        image = im.capture_window(hwnd, False)
        if image.getpixel((0,0)) > 0:
            image = image.save('images/test_%s.bmp' % i, 'BMP')
            time.sleep(0.05)


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

    for i in xrange(100):
        im.capture_window(hwnd, False)
        im.save('test_%s.bmp' % i, 'BMP')
        time.sleep(1)


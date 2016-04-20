#coding=utf8

import imtool
import ocr

from win.capture import capture_inactive_window as capture_window
from win.browser import open_ie
from win.window import find_sub_hwnd

import time
import logging

if __name__ == '__main__':
    logging.basicConfig(
            filename='test.log',
            format='%(asctime)s %(levelname)s %(message)s',
            level=logging.DEBUG)
    # 51hupai.org
    # (left, top), w, h
    pos_info = [
            ((125, 291), 62, 13),
            ((139, 307), 62, 13),
            ((123, 402), 83, 13),
            ((152, 420), 83, 13),
            ((183, 434), 83, 13),
            ]

    ie = open_ie(url="http://moni.51hupai.org")
    time.sleep(5)
    print "%x" % ie.HWND
    hwnd = find_sub_hwnd(ie.hwnd, [("Frame Tab", 0),
        ("TabWindowClass", 0),
        ("Shell DocObject View", 0),
        ("Internet Explorer_Server", 0)])
    #hwnd = find_sub_hwnd(ie.HWND, [("Frame Tab", 0)])
    print "%x" % hwnd


    while True:
        img = capture_window(hwnd)
        images = imtool.find_images(img, pos_info)
        data = []
        for j in xrange(len(images)):
            data.append(ocr.recog(images[j]))
        (attcount, limit, bidtime, price, pricetime) = tuple(data)
        logging.info(','.join(data))
        if bidtime == '11:29:59':
            break
        #time.sleep(0.25)


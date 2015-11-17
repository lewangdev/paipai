#coding=utf8

import capture
import browser

import time

if __name__ == '__main__':
    url = 'http://moni.51hupai.com:8081/'
    ie = browser.open(url)

    # wait until stateready
    time.sleep(5)
    img = capture.capture_window(ie.HWND)
    img.save('t.bmp', 'BMP')
    time.sleep(5)
    ie.Quit()

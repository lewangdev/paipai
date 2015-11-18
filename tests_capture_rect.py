#coding=utf8

import capture
import browser
import time

import gen_config
import config
import ocr


if __name__ == '__main__':
    url = 'http://moni.51hupai.com:8081/'
    ie = browser.open(url)

    # wait until stateready
    time.sleep(5)
    img = capture.capture_window(ie.HWND)
    img.save('ie.bmp', 'BMP')

    rect=capture.get_window_rect(ie.HWND)
    for k,v in config.capture_pos.items():
        ow, oh = v
        rectangle = (rect.left + ow, rect.top + oh, rect.left + ow + gen_config.capture_width, rect.top + oh + 10)
        img = capture.capture_rect(rectangle)
        img.save('%s.bmp' % k, 'BMP')
        print ocr.recofull(img)

    time.sleep(5)
    ie.Quit()

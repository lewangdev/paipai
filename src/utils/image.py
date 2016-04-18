# coding=utf-8
""" 图片处理

"""
from PIL import Image


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
    pass

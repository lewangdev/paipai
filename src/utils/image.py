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

def cut_image(im):
    """对图进行分片处理

    找到所有最小矩形色块
    """
    pass

def find_images(im, pos_info):
    """
    获取所有指定位置和大小的图片
    """
    images = []
    for p, w, h in pos_info:
        left, top = p
        images.append(im.crop((left, top, left + w, top + h)))
    return images


if __name__ == '__main__':
    pos_info = [
            ((110, 291), 62, 13),
            ((139, 307), 62, 13),
            ((123, 405), 83, 13),
            ((152, 420), 83, 13),
            ((267, 435), 83, 13),
            ]
    img = Image.open("2-1.png")
    images = find_images(img, pos_info)
    for i in xrange(len(images)):
        images[i].save('%s.png' % i)

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
                threshold += im.getpixel((x, y))

        threshold /= w * h

    for x in xrange(w):
        for y in xrange(h):
            if (im.getpixel((x, y)) > threshold):
                im.putpixel((x, y), 0xFF if not inverse else 0x00)
            else:
                im.putpixel((x, y), 0x00 if not inverse else 0xFF)
    return im


def find_images(im, pos_info):
    """
    获取所有指定位置和大小的图片
    """
    images = []
    for p, w, h in pos_info:
        left, top = p
        images.append(im.crop((left, top, left + w, top + h)))
    return images


def crop_min_image(img):
    '''裁剪到包括所有非FF色的最小矩形的图
    '''
    w, h = img.size
    pixdata = img.load()

    left = 0
    for x in xrange(w):
        left = x
        stop = False
        for y in xrange(h):
            r = pixdata[x, y]
            if r != 0xFF:
                stop = True
                break
        if stop:
            break

    top = 0
    for y in xrange(h):
        top = y
        stop = False
        for x in xrange(w):
            r = pixdata[x, y]
            if r != 0xFF:
                stop = True
                break
        if stop:
            break

    right = w - 1
    for x in xrange(w - 1, -1, -1):
        right = x
        stop = False
        for y in xrange(h):
            r = pixdata[x, y]
            if r != 0xFF:
                stop = True
                break
        if stop or right <= left:
            break

    bottom = h - 1
    for y in xrange(h - 1, -1, -1):
        bottom = y
        stop = False
        for x in xrange(w):
            r = pixdata[x, y]
            if r != 0xFF:
                stop = True
                break
        if stop or bottom <= top:
            break

    return img.crop((left, top, right + 1, bottom + 1))

def split_image(img):
    """对图进行分片处理

    找到所有最小矩形色块
    """
    w, h = img.size
    pixdata = img.load()

    # 降为1维，如果这一列上全部都是FF，则记为 False, 表示空白列
    mask = []
    for x in xrange(w):
        colorful = False
        for y in xrange(h):
            r = pixdata[x, y]
            if r != 0xFF:
                colorful = True
        mask.append(colorful)

    # 寻找连续的色块
    pieces = []
    top = 0
    bottom = h
    left = 0
    right = 0

    while True:
        while left < w:
            if mask[left]:
                break;
            left += 1

        right = left
        while right < w:
            if not mask[right]:
                break
            right += 1
        if right > left:
            p = img.crop((left, top, right, bottom))
            p = crop_min_image(p)
            pieces.append(p)

        left = right

        if left == w or right == w:
            break

    return pieces

def get_martix(img):
    w, h = img.size
    pixdata = img.load()
    matrix = []
    for x in xrange(h):
        row = []
        for y in xrange(w):
            r = pixdata[y, x]
            if r != 0xFF:
                row.append('1')
            else:
                row.append('0')
        matrix.append(''.join(row))
    return matrix

def fingerprint(img):
    matrix = get_martix(img)
    return "".join(matrix)

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
        #images[i].save('%s.png' % i)
        image_pieces = split_image(binarization(images[i]))
        for image_piece in image_pieces:
            print fingerprint(image_piece)

#coding=utf-8

from PIL import Image

def crop(img):
    '''裁剪到包括所有非FF色的最小矩形
    '''
    w, h = img.size
    pixdata = img.load()

    left = 0
    for x in xrange(w):
        left = x
        stop = False
        for y in xrange(h):
            r,g,b = pixdata[x, y]
            if r != 0xFF or g != 0xFF or b != 0xFF:
                stop = True
                break
        if stop:
            break

    top = 0
    for y in xrange(h):
        top = y
        stop = False
        for x in xrange(w):
            r,g,b = pixdata[x, y]
            if r != 0xFF or g != 0xFF or b != 0xFF:
                stop = True
                break
        if stop:
            break

    right = w - 1
    for x in xrange(w - 1, -1, -1):
        right = x
        stop = False
        for y in xrange(h):
            r,g,b = pixdata[x, y]
            if r != 0xFF or g != 0xFF or b != 0xFF:
                stop = True
                break
        if stop or right <= left:
            break

    bottom = h - 1
    for y in xrange(h - 1, -1, -1):
        bottom = y
        stop = False
        for x in xrange(w):
            r,g,b = pixdata[x, y]
            if r != 0xFF or g != 0xFF or b != 0xFF:
                stop = True
                break
        if stop or bottom <= top:
            break

    return img.crop((left, top, right + 1, bottom + 1))


def split(img):
    w, h = img.size
    pixdata = img.load()


    # 降为1维，如果这一列上全部都是FF，则记为 False, 表示空白列
    mask = []
    for x in xrange(w):
        right = x
        colorful = False
        for y in xrange(h):
            r,g,b = pixdata[x, y]
            if r != 0xFF or g != 0xFF or b != 0xFF:
                colorful = True
                break
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
        p = img.crop((left, top, right, bottom))
        p = crop(p)
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
            r,g,b = pixdata[y, x]
            if r != 0xFF or g != 0xFF or b != 0xFF:
                row.append('1')
            else:
                row.append('0')
        matrix.append(''.join(row))
    return matrix

def get_fingerprint(img):
    matrix = get_martix(img)
    return "".join(matrix)

if __name__ == '__main__':
    chars = list("1234567890-:")
    oimg = Image.open('trainning/normal.bmp')
    oimg = crop(oimg)
    pieces = split(oimg)
    i = 0
    model = {}
    for p in pieces:
        fp = get_fingerprint(p)
        model[fp] = chars[i]
        i += 1
    oimg = Image.open('trainning/bold.bmp')
    oimg = crop(oimg)
    pieces = split(oimg)
    i = 0
    for p in pieces:
        fp = get_fingerprint(p)
        model[fp] = chars[i]
        i += 1

    print model

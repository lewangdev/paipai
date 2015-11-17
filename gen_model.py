#coding=utf-8

from PIL import Image


def get_pixel_string(font, weight='normal'):
    options = dict(normal=7, bold=8)
    img = Image.open(font)
    width, height = img.size
    pixdata = img.load()

    model = []
    for idx in xrange(width/options[weight]):
        char = []
        for y in xrange(height):
            row = []
            for x in xrange(idx * options[weight], (idx + 1) * options[weight]):
                r, g, b = pixdata[x, y]
                if r and g == 0:
                    row.append('1')
                else:
                    row.append('0')
            bin_str = ''.join(row)
            irow = int(bin_str, 2)
            char.append(irow)
        model.append(char)

    return model

def get_fingerprint(font, weight='normal'):
    options = dict(normal=7, bold=8)
    img = Image.open(font)
    width, height = img.size
    pixdata = img.load()

    chars = []
    for idx in xrange(width/options[weight]):
        char = []
        for y in xrange(height):
            for x in xrange(idx * options[weight], (idx + 1) * options[weight]):
                r, g, b = pixdata[x, y]
                if r and g == 0:
                    char.append('1')
                else:
                    char.append('0')
        chars.append(''.join(char))

    return chars

if __name__ == '__main__':
    #arr_normal = get_pixel_string('normal.bmp')
    #arr_bold = get_pixel_string('bold.bmp', weight='bold')
    #print arr_normal
    #print arr_bold
    chars = list('1234567890-:')
    normal = get_fingerprint('normal.bmp')
    normal_dict = {}
    for i in xrange(12):
        normal_dict[normal[i]] = chars[i]

    bold = get_fingerprint('bold.bmp', weight='bold')
    bold_dict = {}
    for i in xrange(12):
        bold_dict[bold[i]] = chars[i]
    print normal_dict
    print bold_dict

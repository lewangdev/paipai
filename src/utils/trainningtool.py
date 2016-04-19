#coding=utf-8

from imtool import split_image, fingerprint, binarization
from PIL import Image

import json

if __name__ == '__main__':
    expected_text='1234567890-:'
    imagefiles = ["../../trainning/normal.bmp", '../../trainning/bold.bmp']

    models = {}
    for f in imagefiles:
        image = Image.open(f)
        image_pieces = split_image(binarization(image))
        for i in xrange(len(image_pieces)):
            models[fingerprint(image_pieces[i])] = expected_text[i]

    print json.dumps(models)

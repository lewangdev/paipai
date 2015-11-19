#coding=utf8
import model
import gen_model

import sys

def reco(fp):
    return model.models.get(fp, '')

def recofull(img):
    text = []
    img = gen_model.crop(img)
    pieces = gen_model.split(img)
    for p in pieces:
        fp = gen_model.get_fingerprint(p)
        text.append(reco(fp))
    return ''.join(text)


if __name__ == '__main__':
    ## usage
    # python ocr.py img.bmp
    ##
    img = sys.argv[1]

    print recofull(img)

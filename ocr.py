#coding=utf8
import model
import gen_model

import sys

def reco(fp, weight='normal'):
    return model.models.get(weight).get(fp, ' ')

if __name__ == '__main__':
    ## usage
    # python ocr.py img.bmp [bold|normal]
    ##
    img = sys.argv[1]

    if len(sys.argv) == 2:
        weight = 'normal'
    else:
        weight = sys.argv[2]

    fps = gen_model.get_fingerprint(img, weight)

    text = []
    for fp in fps:
        text.append(reco(fp, weight))
    print ''.join(text)


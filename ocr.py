#coding=utf8
import model
import gen_model

import sys

def reco(fp, weight='normal'):
    return model.models.get(weight).get(fp, ' ')

if __name__ == '__main__':
    #fps = gen_model.get_fingerprint('normal.bmp')
    #for fp in fps:
    #    print reco(fp)

    #fps = gen_model.get_fingerprint('bold.bmp', 'bold')
    #for fp in fps:
    #    print reco(fp, 'bold')
    img = sys.argv[1]
    weight = sys.argv[2]
    fps = gen_model.get_fingerprint(img, weight)

    text = []
    for fp in fps:
        text.append(reco(fp, weight))
    print ''.join(text)


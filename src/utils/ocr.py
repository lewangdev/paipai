#coding=utf8
import model
import imtool

def recog(img):
    image_pieces = imtool.split_image(imtool.binarization(img))
    text = []
    for image_piece in image_pieces:
        fp = imtool.get_fingerprint(image_piece)
        text.append(model.models.get(fp, ''))
    return ''.join(text)

if __name__ == '__main__':
    pass

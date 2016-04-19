import ocr
import imtool

from PIL import Image

if __name__ == '__main__':
    pos_info = [
            ((110, 291), 62, 13),
            ((139, 307), 62, 13),
            ((123, 405), 83, 13),
            ((152, 420), 83, 13),
            ((267, 435), 83, 13),
            ]
    img = Image.open("../../trainning/2-2.png")
    images = imtool.find_images(img, pos_info)
    i = 1
    for image in images:
        image.save('images/%s.png' % i)
        i += 1
        print ocr.recog(image)

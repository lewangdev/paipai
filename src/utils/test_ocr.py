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
    img = Image.open("2-1.png")
    images = imtool.find_images(img, pos_info)
    for image in images:
        print ocr.recog(image)

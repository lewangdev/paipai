#coding=utf8
import ocr
from PIL import Image

import unittest

class TestOcr(unittest.TestCase):
    def test_ocr(self):
        files = [
                ('t1.bmp', '2015-09-19 11:24:15', 'bold'),
                ('t2.bmp', '11:28:17', 'bold'),
                ('t3.bmp', '80500', 'bold'),
                ('nt1.bmp', '165765', 'normal'),
                ('nt2.bmp', '8727', 'normal'),
                ]

        prefix = 'testfiles/%s'

        for t in files:
            f, expected, w = t
            actual = ocr.recofull(Image.open(prefix % f), w)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

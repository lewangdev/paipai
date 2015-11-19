#coding=utf8
import ocr
from PIL import Image

import unittest

class TestOcr(unittest.TestCase):
    def test_ocr(self):
        files = [
                ('t1.bmp', '2015-09-1911:24:15'),
                ('t2.bmp', '11:28:17'),
                ('t3.bmp', '80500'),
                ('nt1.bmp', '165765'),
                ('nt2.bmp', '8727'),
                ('r1.bmp', '8727'),
                ('r2.bmp', '165765'),
                ('r3.bmp', '11:28:17'),
                ('r4.bmp', '80500'),
                ('r5.bmp', '2015-09-1911:24:15'),
                ]

        prefix = 'testfiles/%s'

        for t in files:
            f, expected = t
            actual = ocr.recofull(Image.open(prefix % f))
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

import numpy as np
import os
import cv2
import json
from fuzzywuzzy import fuzz
from ctypes import *

libpath = os.environ.get('VIRTUAL_ENV')

lib3 = cdll.LoadLibrary(os.path.join(libpath, 'lib/libprahvi3.so'))
lib4 = cdll.LoadLibrary(os.path.join(libpath, 'lib/libprahvi4.so'))

def compareText(string1, string2):
    """Function to get accuracy between a ground truth str
    and a ocr'd str"""
    string1 = string1.replace('\n', '')
    string2 = string2.replace('\n', '')

    return float(fuzz.partial_ratio(string1, string2)) / 100.0


class Prahvi3:
    """Wrapper Class for C++ Prahvi API"""
    def __init__(self):
        cur_dir = os.path.abspath(os.path.dirname(__file__))
        os.environ["TESSDATA_PREFIX"] = os.path.join(cur_dir, '../../tessdata/3.0.5/')

        lib3.Prahvi_getText.restype = c_char_p
        self.obj = lib3.Prahvi_new()

    def getNewText(self, np_image):
        return lib3.Prahvi_getNewText(self.obj, py_object(np_image))

    def getText(self):
        return lib3.Prahvi_getText(self.obj)


class Prahvi4:
    """Wrapper Class for C++ Prahvi API"""
    def __init__(self):
        cur_dir = os.path.dirname(__file__)
        os.environ["TESSDATA_PREFIX"] = os.path.join(cur_dir, '../../tessdata/4.0.0/')

        lib4.Prahvi_getText.restype = c_char_p
        self.obj = lib4.Prahvi_new()

    def getNewText(self, np_image):
        return lib4.Prahvi_getNewText(self.obj, py_object(np_image))

    def getText(self):
        return lib4.Prahvi_getText(self.obj)



class TFIDF:
    """Class to compute the TFIDF of a document"""
    def __init__(self, text):
        text = text.split(' ')
        idf, num_doc = json.loads(tfidf_file)
        result = {}


        tf = {}
        for word in text:
            if word == '':
                continue
            if tf.get(word):
                tf[word] += 1
            else:
                tf[word] = 1

        max_tf = max(tf.values())

        for word in tf.keys():
            tf[word] = 0.5 + 0.5 * (tf[word] / max_tf)
            idf_val = log(num_doc / idf[word])
            result[word] = tf[word] * idf_val

        return result

if __name__ == '__main__':
    # Tests
    pv = Prahvi3()

    img_path = '/home/abemillan/Developer/PRAHVI/ExtractTextLine/test_images/IMG_9121.png'
    img = cv2.imread(img_path) 


    print 'Doing OCR3...'

    print pv.getNewText(img)

    print 'Results:'
    print pv.getText()

    pv = Prahvi4()
    print 'Doing OCR4'
    print pv.getNewText(img)

    print 'Results: '
    print pv.getText()

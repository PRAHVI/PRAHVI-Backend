import numpy as np
import cv2
from prahvi.api.v1 import blueprint 
from prahvi.lib import compareText, Prahvi3, Prahvi4, TFIDF
from flask import jsonify, request

import time


class PRAHVIRESPONSE:
    SUCCESS = 0
    BLUR = 1

def _get_image(stream):
    data = stream.read()
    image = np.asarray(bytearray(data), dtype='uint8')
    return cv2.imdecode(image, cv2.IMREAD_COLOR)


@blueprint.route('/image/ocr3/', methods=['POST'])
def getTextFromImageUsingTesseract3():
    pv = Prahvi3()
    image = _get_image(request.files['image'])

    response = pv.getNewText(image)
    if response == PRAHVIRESPONSE.SUCCESS:
        return jsonify({ 'result': pv.getText() })

    return jsonify({ 'result': '' })


@blueprint.route('/image/ocr4/', methods=['POST'])
def getTextFromImageUsingTesseract4():
    pv = Prahvi4()
    image = _get_image(request.files['image'])
    
    if pv.getNewText(image) == PRAHVIRESPONSE.SUCCESS:
        return jsonify({ 'result': pv.getText() })

    return jsonify({ 'result': ''})


@blueprint.route('/text/tfidf/', methods=['POST'])
def getTFIDIF():
    text = request.get_json() 
    text = text.get('text')

    tfidf = TFIDF(text)

    return jsonify({ 'result': tfidf.result })


@blueprint.route('/text/compare/', methods=['POST'])
def getSimilarity():
    data = request.get_json()
    orig_text = data.get('text1')
    comp_text = data.get('text2') 

    if not orig_text or not comp_text:
        return jsonify({ 'result': -1 })

    return jsonify({ 'result': compareText(orig_text, comp_text) })

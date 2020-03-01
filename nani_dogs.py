import dlib, cv2, os
from imutils import face_utils
import numpy as np
import argparse

import matplotlib.pyplot as plt
from math import atan2, degrees, cos
from PIL import Image
import os




def angle_between(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    return atan2(x, y)


ap = argparse.ArgumentParser()
# Original
ap.add_argument("-i1", "--dog", required=True,
                help="path to input image")
ap.add_argument("-s", "--scale", required=True,
                help="eyes scale")
args = vars(ap.parse_args())

detector = dlib.cnn_face_detection_model_v1(os.getcwd() + '/dogHeadDetector.dat')
predictor = dlib.shape_predictor( os.getcwd() + '/landmarkDetector.dat')

img = cv2.imread(args["dog"])


dets = detector(img, upsample_num_times=0)



img_result = img.copy()

shapes = []

for i, d in enumerate(dets):
    shape = predictor(img, d.rect)
    shape = face_utils.shape_to_np(shape)

    for i, p in enumerate(shape):
        shapes.append(shape)



try:
    eyes = Image.open('nani.png')
    original = Image.open(args['dog'])
    new_size = ((int(eyes.size[0] * float(args['scale']))), int(eyes.size[1] * float(args['scale'])))
    eyes = eyes.resize(new_size)
    dim = (eyes.size[0]//2, eyes.size[1]//2)
    mask = eyes.split()[3]

    original.paste(eyes, (shape[5][0] - dim[0], shape[5][1] - dim[1]), mask=mask)

    original.paste(eyes, (shape[2][0] - dim[0], shape[2][1] - dim[1]), mask=mask)

    original.save('nanidog.png')
except:
    print('couldnt find dog')

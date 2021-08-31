#! /usr/bin/env python3
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2021-08-25 15:05:19
####################################################

import cv2
import os
import time
import numpy as np

class FaceModelTrainer(object):
    def __init__(self):
        self.__labels = []
        self.__images = []
        self.__names = []
        self.__model = cv2.face.EigenFaceRecognizer_create()
    def load(self, samples="samples"):
        labels = []
        images = []
        names = []
        label = 1
        print("load images from {}".format(samples))
        for name in os.listdir(samples):
            names.append(name)
            self.__model.setLabelInfo(label, name)
            subpath = samples+"/"+name
            if not os.listdir(subpath):
                print("error: {}: no such directory".format(subpath))
                break
            print("load images label:{}, name:{}".format(label, name))
            cv2.namedWindow(subpath)
            for filename in os.listdir(subpath):
                imgpath = os.path.join(subpath, filename)
                img = cv2.imread(imgpath)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.putText(img, filename, (0, img.shape[1]//2), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.8, color=(255,0,0))
                cv2.imshow(subpath, img)
                cv2.waitKey(30)
                images.append(gray)
                labels.append(label)
            label += 1
            cv2.destroyWindow(subpath)
        images = np.asarray(images)
        labels = np.asarray(labels)
        self.__labels = labels
        self.__images = images
        self.__names = names
    def train(self, saveto="face_model.xml"):
        print("train ...")
        self.__model.train(self.__images, self.__labels)
        print("save model {} ...".format(saveto))
        self.__model.save(saveto)

def model_train(samples="samples"):
    model = FaceModelTrainer()
    model.load(samples)
    model.train()

if __name__ == '__main__':
    model_train("samples")


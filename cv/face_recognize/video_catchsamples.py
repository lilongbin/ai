#! /usr/bin/env python3
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2021-08-24 16:30:11
####################################################

import cv2
import os
import shutil
import time
import string

# source can be camera device id, default 0 or -1, if usb camera maybe 1, etc.
# source can also be a local video file name.
class Capture(object):
    def __init__(self, source=0):
        print ('open capture {}'.format(source))
        # 1. create a capture from a device or local file
        self.__capture = cv2.VideoCapture(source)
        self.__size = (int(self.__capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(self.__capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.__fps = int(self.__capture.get(cv2.CAP_PROP_FPS))
    def __del__(self):
        print ('close capture')
        # 3. release() when dont use again
        self.__capture.release()
    def size(self):
        return self.__size
    def fps(self):
        return self.__fps
    def dump(self, name, frame, rect, dstsize=(0,0)):
        x,y,w,h = rect
        if sum(dstsize) == 0:
            dstsize = (w, h)
        newframe = cv2.resize(frame[y:y+h, x:x+w], dstsize)
        cv2.imwrite(name, newframe)
        print("dump image: {}".format(name))
    def capture(self):
        while self.__capture.isOpened():
            # 2. get frame by read()
            ok, frame = self.__capture.read()
            yield ok, frame
            if not ok: break
            #continue
            #key = cv2.waitKey(30)
            #if (key == ord('q') or (0x1B == key)):
            #    break # q or Esc

class CVWindow(object):
    def __init__(self, title="myvideo"):
        print("create cv2 window: {}".format(title))
        self.__title = title
        cv2.namedWindow(self.__title)
    def __del__(self):
        print("destroy cv2 window")
        cv2.destroyWindow(self.__title)
    def putText(self, frame, text, origin=(0,0), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.8, color=(255,0,0), thickness=1, lineType=8, bottomLeftOrigin=False):
        w,h = cv2.getTextSize(text, fontFace, fontScale, thickness)
        if (origin[1] <= h):
            origin = (origin[0], h)
        cv2.putText(frame, text, origin, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
    def show(self, frame):
        cv2.imshow(self.__title, frame)

class FaceDetector(object):
    def __init__(self, classifier=r"haarcascade_frontalface_alt2.xml", color=(0,255,0),min_size=(64,64)):
        self.__color = color
        self.__min_size = min_size
        path = "/".join([cv2.data.haarcascades,classifier])
        self.__classifier = cv2.CascadeClassifier(path)
    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_rects = self.__classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=self.__min_size)
        return face_rects
    def bordered(self, frame, rects):
        for (x,y,w,h) in rects: # may contain multi faces
            cv2.rectangle(frame, (x,y), (x+w, y+h), self.__color, 1)

def video_sample(source=0):
    if str(source).isdigit():
        title = "myvideo-" + str(source)
    else:
        title = str(source)
    name = input("please type your name:")
    path = "samples/"+name

    window = CVWindow(title)
    capture = Capture(source)
    size = capture.size()
    print("size: {}, fps: {}".format(size, capture.fps()))

    detector = FaceDetector()
    count = 0
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("remove dir: {}".format(path))
    if not os.path.isdir(path):
        os.makedirs(path)
        print("make dir: {}".format(path))
    for ok, frame in capture.capture():
        if not ok: break
        faces = detector.detect(frame)
        key = cv2.waitKey(30)
        if (key == ord('q') or (0x1B == key)):
            break # q or Esc
        if (ord('s') == key): #save
            for (x,y,w,h) in faces:
                count += 1
                filename = path + "/" + str(count)+".png"
                capture.dump(filename, frame, (x,y,w,h), (200, 200))
        if len(faces):
            window.putText(frame, "face detected and {} saved".format(count), (size[0]//4, size[1]//2))
        detector.bordered(frame, faces)
        window.show(frame)

if __name__ == '__main__':
    #video_sample("myvideo.mkv")
    video_sample(0)


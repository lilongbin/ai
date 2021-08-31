#! /usr/bin/env python3
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2021-08-20 14:43:06
####################################################

import cv2
import time

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

class Recorder(object):
    def __init__(self, name="myvideo.mkv", codec="X264", fps=30.0, size=(640,480), color=True):
        # four character codec see www.fourcc.org/cofecs.php
        # eg: XVID HEVC(H265) X264(H264)
        print("open %s codec:%s fps:%d size:%s" % (name, codec, fps, str(size)))
        fourcc = cv2.VideoWriter_fourcc(*codec)
        self.__writer = cv2.VideoWriter(name, fourcc, fps, size, color)
    def __del__(self):
        self.__writer.release()
    def write(self, frame):
        self.__writer.write(frame)

def video_record(source=0):
    title = "myvideo-" + str(source) + "." + time.strftime("%F_%H%M%S")

    window = CVWindow(title)
    capture = Capture(source)
    size = capture.size()
    print("size: {}, fps: {}".format(size, capture.fps()))

    video = Recorder(title+".mkv", codec="XVID", size=size)
    print("capture {} start".format(time.strftime("%F %T")))
    for ok, frame in capture.capture():
        if not ok: break
        key = cv2.waitKey(30)
        if (key == ord('q') or (0x1B == key)):
            break # q or Esc
        window.putText(frame, title, (0, size[1]*95//100))
        window.show(frame)
        print("\rcapture {} ...".format(time.strftime("%F %T")), end="")
        video.write(frame)
    print("\rcapture {} end".format(time.strftime("%F %T")))

if __name__ == '__main__':
    video_record(0)


#! /usr/bin/env python
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2018-04-18 00:24:38
####################################################

import random
from PIL import Image,ImageDraw,ImageFont

def gen_randcode(randlen=6, fontsize=30):
    width = fontsize * randlen
    highth = fontsize * 2
    
    def rndTxt():
        ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        strs = ascii_letters + digits
        return random.choice(strs)
    def rndFgColor():
        black = (0, 0, 0)
        # return black
        color = tuple(random.randint(0,128) for i in range(3))
        return color
    def rndBgColor():
        white = (255, 255, 255)
        # return white
        color = tuple(random.randint(129,255) for i in range(3))
        return color
    def rndPoint():
        return (random.randint(0, width), random.randint(0, highth))
    def fillBg(width, highth):
        for x in range(width):
            for y in range(highth):
                draw.point((x,y), fill=rndBgColor())
    
    # 创建img实例并使用随机颜色填充背景
    img = Image.new(mode="RGB",size=(width,highth),color=rndBgColor())
    # 实例化一支画笔
    draw = ImageDraw.Draw(img,mode="RGB")
    # 绘制随机背景
    fillBg(width, highth)
    # 绘制干扰线
    draw.line((rndPoint(), rndPoint()), fill=rndFgColor(), width=3)
    # 定义要使用的字体
    font = ImageFont.truetype("/home/longbin/.fonts/UbuntuMono-R.ttf", fontsize)
    
    randcode = "".join([rndTxt() for i in range(randlen)])
    for x,char in enumerate(randcode):
        randcolor = rndFgColor()
        #把生成的字母或数字添加到图片上
        #每添加一个字符,其位置就要向后移动
        w = fontsize*x + fontsize/4
        h = random.randint(0, fontsize) #上下边界随机
        draw.text([w, h], char, randcolor, font=font)
    
    #把生成的图片保存为png格式
    img.save(randcode + ".png")
    return randcode

def func_test():
    randcode = gen_randcode(5)
    print("%s" % randcode)

if __name__ == "__main__":
    func_test()


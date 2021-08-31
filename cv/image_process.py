#! /usr/bin/python
import Image
import ImageDraw
import ImageEnhance

## resize image
def resize_img(raw_img, new_img='new_img.jpg', length=800, width=600):
	img = Image.open(raw_img)
	tmp_img = img.resize((length, width), Image.BILINEAR)
	tmp_img.save(new_img)
	# print img.info

# resize_img(raw_img='img12-green.jpg', new_img='new_img.jpg', length=256, width=256)
# resize_img(raw_img='img12-green.jpg', new_img='new_img.jpg')

def rotate_img(img_name, new_img, rotate=45):
	img = Image.open(img_name)
	tmp_img = img.rotate(rotate)
	tmp_img.save(new_img)

# rotate_img(img_name='img12-green.jpg', new_img='new_img.jpg', rotate=60)

def format_img(img_name, to_format='bmp'):
	img = Image.open(img_name)
	img.save(img_name[:-4] + '.' + to_format)

# format_img(img_name='img12-green.jpg', to_format='png')

def histogram_img(img_name):
	img = Image.open(img_name)
	print img.histogram()

# histogram_img(img_name='img12-green.jpg')

def draw_img(img_name, new_img):
	img = Image.open(img_name).resize((800, 600), Image.BILINEAR)
	draw_img = ImageDraw.Draw(img)
	width, height = img.size

	## draw croos line
	## draw_img.line((point1, point2), color)
	draw_img.line(((0, 0), (width-1, height-1)), (0, 0, 0))
	draw_img.line(((0, height-1), (width-1, 0)), (0, 0, 0))
	## draw circle line
	draw_img.arc((0, 0, width - 1, height - 1), 0, 360, 255)
	img.show()
	img.save(new_img)

# draw_img(img_name='img12-green.jpg', new_img='new_img.jpg')

def brightness_img(img_name, new_img='new_img.jpg'):
	bright_img = Image.open(img_name)
	## brightness
	brightness = ImageEnhance.Brightness(bright_img)
	tmp_img = brightness.enhance(1.2)
	tmp_img.save(new_img)

# brightness_img(img_name='img12-green.jpg', new_img='new_img.jpg')

def sharpness_img(img_name, new_img='new_img.jpg'):
	img = Image.open(img_name)
	sharpness = ImageEnhance.Sharpness(img)
	sharp_img = sharpness.enhance(7.0)
	sharp_img.save(new_img)

# sharpness_img(img_name='img12-green.jpg', new_img='new_img.jpg')

def contrast_img(img_name, new_img='new_img.jpg'):
	img = Image.open(img_name)
	contrast = ImageEnhance.Contrast(img)
	contrast_img = contrast.enhance(2.0)
	contrast_img.save(new_img)

# contrast_img(img_name='img12-green.jpg', new_img='new_img.jpg')









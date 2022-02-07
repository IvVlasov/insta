from PIL import Image,  ImageDraw
import urllib
import requests
from io import BytesIO
from ast import literal_eval


def centerPic(picture):
	(pic_w, pic_y) = picture.size
	return (pic_w//2, pic_y//2)
 

def pasteImage(picture, icon): 
	x_done = centerPic(picture)[0] - centerPic(icon)[0] 
	y_done = centerPic(picture)[1] - centerPic(icon)[1] 
	return(x_done, y_done)

def colorImage(color):
	img = Image.new("RGB", (300, 300), color)
	return img
	# with BytesIO() as output:
	#     img.save(output, format="PNG")
	#     contents = output.getvalue()
	# return contents

def createColorful(color, ico):
	colorful = Image.new("RGB", (1080, 1920), color)
	colorful.paste(ico, pasteImage(colorful, ico),  ico)
	colorful.save('done.png')


def createBackground(backpath, iconpath):
	back = Image.open(BytesIO(backpath.content))
	ico = Image.open(iconpath)
	back = back.resize((1080,1920))
	
	back.paste(ico, pasteImage(back, ico),  ico)
	with BytesIO() as output:
	    back.save(output, format="PNG")
	    contents = output.getvalue()
	return contents

def color_back(rgb):
	img = Image.new("RGB", (1080,1920), literal_eval(rgb))
	with BytesIO() as output:
	    img.save(output, format="PNG")
	    contents = output.getvalue()
	return contents

def create_color_Background(color, iconpath):
	back = Image.new("RGB", (1080,1920), literal_eval(color))

	ico = Image.open(iconpath)
	ico = ico.resize((800,800))
	
	back.paste(ico, pasteImage(back, ico),  ico)

	with BytesIO() as output:
	    back.save(output, format="PNG")
	    contents = output.getvalue()
	return contents


# string = '(222, 123, 44)'
# print(literal_eval(string))

# new_im = Image.new('RGB', (900, 300))
# x_offset = 0
# for i, el in enumerate(rgb_list):
# 	# colorImage(el).save('colors/'+ str(i) + '.png')

# 	new_im.paste(colorImage(el), (x_offset,0))

# 	x_offset += 300

# new_im.save('colors/test.jpg')





# colorImage(rgb1)
# colorImage(rgb2)
# colorImage(rgb3)

























# background = Image.open('backgrounds/pink.jpg')
# for i in range(6):
# 	if i == 0:
# 		continue
# 	icon = Image.open('icons/'+str(i)+'.png')
# 	icon = icon.resize((100,100))
# 	icon.save('icons/Mini/'+str(i)+'.png')

# createColorful((100,13,22), icon)
# createBackground(background, icon)





# colorful.paste(icon, pasteImage(colorful, icon),  icon)
# colorful.save('done.png')

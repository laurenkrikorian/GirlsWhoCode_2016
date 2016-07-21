from PIL import Image

im = Image.open("giraffe.jpg")

dark_green = (0, 90, 0)
blue = (0, 148, 189)
coral = (255, 160, 120)

pixel = list(im.getdata())

new_image = []

for pix in pixel: # pix is one pixel (0, 13, 255)
	r = pix[0]
	g = pix[1]
	b = pix[2]
	
	pixel_value = r + g + b

	if pixel_value < 215:
		new_image.append(dark_green)
		
	if pixel_value >= 215 and pixel_value < 520:
		new_image.append(blue)
		
	if pixel_value >= 520:
		new_image.append(coral)

im.putdata(new_image)

im.show()
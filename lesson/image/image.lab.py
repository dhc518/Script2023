from PIL import ImageColor
from PIL import Image
import viewer

# color_names = ImageColor.colormap.keys()
#
# cat_img = Image.open('zophie.png')
# print(cat_img.size,cat_img.filename,cat_img.format,cat_img.format_description,cat_img.info)
#cat_img.show()


from PIL import Image
from PIL import ImageEnhance

cat_img = Image.open('zophie.png')
bright = ImageEnhance.Brightness(cat_img)
bright_cat = bright.enhance(0.7)

color = ImageEnhance.Color(cat_img)
color_cat = color.enhance(0.0)

contrasted_cat_img = ImageEnhance.Contrast(cat_img).enhance(1.5)

sharpened_cat_img = ImageEnhance.Sharpness(cat_img).enhance(3.0) # sharpened

#viewer.show_images(cat_img, contrasted_cat_img)

from PIL import ImageFilter

blurred_cat_img = cat_img.filter(ImageFilter.GaussianBlur(radius=3))
filtered_cat_img = cat_img.filter(ImageFilter.FIND_EDGES)

filtered_cat_img = cat_img.filter(ImageFilter.CONTOUR)

filtered_cat_img = cat_img.filter(ImageFilter.DETAIL)

filtered_cat_img = cat_img.filter(ImageFilter.SMOOTH)

filtered_cat_img = cat_img.filter(ImageFilter.SMOOTH_MORE)

filtered_cat_img = cat_img.filter(ImageFilter.EMBOSS)

filtered_cat_img = cat_img.filter(ImageFilter.SHARPEN)
# viewer.show_images(cat_img, filtered_cat_img)


new_img = Image.new('RGBA', (400,400),'yellow')
# new_img.save('yellow_card.png')

face = cat_img.crop((334,345,565,560))
# viewer.show_image(face)

#new_img.paste(face,(0,0))
#viewer.show_image(new_img)

cat_img_copy = cat_img.copy()
cat_logo_img = Image.open('catlogo.png').resize((100, 100))
new_img.paste(cat_logo_img, (200, 100), cat_logo_img)
#viewer.show_image(new_img)

# width, height = cat_img.size
# cat_img_small = cat_img.resize((width//2, height//2))
# viewer.show_image(cat_img_small)
# new_img = cat_img.rotate(90, expand=True)
# viewer.show_image(new_img)
# new_img = cat_img.rotate(45, expand=True)
# viewer.show_image(new_img)
# new_img = cat_img.transpose(Image.FLIP_LEFT_RIGHT)
# viewer.show_image(new_img)
# new_img = cat_img.transpose(Image.FLIP_TOP_BOTTOM)
# viewer.show_image(new_img)

from PIL import ImageDraw
im = Image.new('RGBA', (200, 200),'white')
draw = ImageDraw.Draw(im)
draw.point([(10, 10), (180, 10), (180, 180), (10, 180)], fill='orange')
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black', width=5)

draw.rectangle((20, 30, 60, 60), fill='blue')
draw.rectangle((20, 30, 60, 60), fill='blue', outline='red')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')
#viewer.show_image(im)

from PIL import ImageFont
import os
im = Image.new('RGBA', (400, 400), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'c:/Windows/Fonts'
gulimFont = ImageFont.truetype('C:\windows\Fonts\gulim.ttc', 32)
draw.text((100, 150), '안녕하세요', fill='red', font=gulimFont)
viewer.show_image(im)


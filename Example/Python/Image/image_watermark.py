from PIL import Image
from PIL import ImageDraw
import os
__DIR__ = os.path.dirname(os.path.abspath(__file__))

img = Image.open(__DIR__ + '/scaled_photo1.jpg')
img_draw = ImageDraw.Draw(img)
img_draw.text((25,20), "AmirRasoulzadeh", fill = (255,0,0))
img.save(__DIR__ + '/watermarked_photo1.jpg')
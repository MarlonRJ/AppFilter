import cv2
import numpy as np
from PIL import Image
import pilgram

#Image Path
path_image ="/home/croissant/Pictures/EnGaren.jpg"
im = Image.open(path_image)
pilgram.aden(im).save('sample-aden.jpg')

pilgram.css.saturate(im,2).save("filtered1.jpg")

#pilgram.css.blending.color(img, img2).save("blended.jpg")
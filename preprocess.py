import os
from PIL import Image
from multiprocessing import Pool
from resizeimage import resizeimage


size = 256, 256

def resize_image(path_and_file):
	with Image.open(path_and_file[0]) as im:
		cover = resizeimage.resize_cover(im, [256, 256])
		cover.save(path_and_file[0].replace("downloads", "train"), "JPEG")

img_dir = "./images/downloads/"
images = []

for directory in os.listdir(img_dir):
    for filename in os.listdir(os.path.join(img_dir, directory)):
        filePath = os.path.join(os.path.join(img_dir, directory), filename).replace("\\", "/") #.replace("downloads", "train")
        images.append([filePath, filename])

for picture in images:
    resize_image(picture)

print("All the images were Resized!") 
import cv2
import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ImagePath")
args = parser.parse_args()

# print(args.ImagePath)


img = cv2.imread(args.ImagePath)
scale = 255
percent = 0.4
#percent = 0.25
#percent = 0


b,g,r = cv2.split(img)
b = b.astype(np.float32)
g = g.astype(np.float32)
r = r.astype(np.float32)

c = 1 - r / scale
m = 1 - g / scale
y = 1 - b / scale
k = cv2.min(cv2.min(c, m),y)
c = scale * (c - k) / (1 - k)
m = scale * (m - k) / (1 - k)
y = scale * (y - k) / (1 - k)

# desaturate neighbors of G which are C,Y
c = cv2.multiply(c, percent)
y = cv2.multiply(y, percent)

# convert back to bgr
r = scale * (1.0 - c / scale) * (1.0 - k)
g = scale * (1.0 - m / scale) * (1.0 - k)
b = scale * (1.0 - y / scale) * (1.0 - k)
r = r.clip(0,255).astype(np.uint8)
g = g.clip(0,255).astype(np.uint8)
b = b.clip(0,255).astype(np.uint8)
img_desat = cv2.merge([b,g,r])

# save result
cv2.imwrite('result.jpg', img_desat)

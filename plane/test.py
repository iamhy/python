from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

planes = Image.open("a330-300.png")
im1 = planes.convert('L')
wc = Image.open("WC.png")
im2 = wc.convert('L')
width, height = im1.size
width1, height1 = im2.size

img = []

n = 0

plt.figure("图片列表")

for x in range(0, width, width1):
    for y in range(0, height, height1):
        box = (width, height, width + width1, height + height1)
        roi = planes.crop(box)
        n += 1

        plt.subplot(204,10,n),plt.title(str(n))
        plt.imshow(roi)
plt.show()
print(n)


# p = np.array(im1)
# # q = np.array(im2)
# print(im1.size,im2.size)

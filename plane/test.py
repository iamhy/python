from PIL import Image
import numpy as np

im = Image.open("a330-300.png").convert('L')
im2 = Image.open("WC.png").convert('L')

width, height = im.size
width1, height = im2.size

n = 0

for x in range(0, width):
    for y in range(0, height):
        for i in range(0, width1):
            for j in range(0, height):
                if im.getpixel((x, y)) == im2.getpixel((i, j)):
                    continue
                    n+=1
                else:
                    break
    
            break
    
# p = np.array(im)
# q = np.array(im2)
print(n)

# im.show()

# print(q)

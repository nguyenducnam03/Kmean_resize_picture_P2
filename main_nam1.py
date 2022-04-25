import time
start_time = time.time()
print("Process finished --- %s seconds ---" % (time.time() - start_time))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
import numpy as np
from PIL import Image

# img=mpimg.imread('test_kmean.jfif')
img=mpimg.imread('nam1.jpg')

HEIGHT = img.shape[0]
WIDTH = img.shape[1]
dim = img.shape[2]
n_colors = 9
img = img.reshape(-1,dim)

COLORS = []
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(img)
labels = kmeans.labels_
# print(labels.index(1))
for i in range(n_colors):
    sum_r = 0
    sum_g = 0
    sum_b = 0
    sum_rgb = 0
    for j in range(len(labels)):
        if labels[j] == i:
            sum_rgb += 1
            sum_r += img[j][0]
            sum_g += img[j][1]
            sum_b += img[j][2]
    COLORS.append([round(sum_r/sum_rgb,2),round(sum_g/sum_rgb,2),round(sum_b/sum_rgb,2)])

print(COLORS)
for i in range(len(img)):
    img[i] = COLORS[labels[i]]

img = img.reshape(HEIGHT,WIDTH,dim)
print(img)
print("Process finished --- %s seconds ---" % (time.time() - start_time))

#command for print the picture with rgb value
imgplot = plt.imshow(img)
plt.show()

im = Image.fromarray(img)
im.save("picture_kmean_1.jpeg")


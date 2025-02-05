import math
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def eculidean_distance(point,center,k):
    distances=[]
    for j in range(k):
        sum = np.sum(np.square(point - center[j]))
        distances.append(np.sqrt(sum))
    return distances

def update_centers(k,clusters,points):
    new_center=[]
    cluster_points=[]
    for i in range(k):
        for j in range(len(points)):
            if i==clusters[j]:
             #collecting the pixels for each cluster
             cluster_points.append(points[j])
        new_center.append(np.mean(cluster_points))
    return new_center

img=Image.open('./mm.jpeg')
img1=plt.imread('./mm.jpeg')
row=img1.shape[0]
col=img1.shape[1]
channel=img1.shape[2]
matrix1=np.array(img.getdata())
array_pixels=[x for sets in matrix1 for x in sets]
#choose cluster val
K=2
#create array of centers
center=np.empty([K])
#choose centers randomly
for i in range (K):
    index = np.random.randint(len(array_pixels))
    center[i]=array_pixels[index]


iterations=2
for max in range(iterations):
    cluster_indx = []
    #clustring
    for i in range(len(array_pixels)):
       distance=eculidean_distance(array_pixels[i],center,K)
       cluster_indx.append(np.argmin(distance,axis=0))
    new_center=update_centers(K,cluster_indx,array_pixels)


new_img=np.empty([len(array_pixels)])
for i in range(len(array_pixels)):
    new_img[i]=math.ceil(new_center[cluster_indx[i]])


new_img=new_img.reshape(row,col,channel)
print(new_img)
plt.imshow(new_img.astype('uint8'))
plt.show()

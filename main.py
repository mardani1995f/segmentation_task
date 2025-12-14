import os
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # یا 'Qt5Agg'
import matplotlib.pyplot as plt

image_dir = "G:/Projects/segmentation_task/data/images/"
mask_dir = "G:/Projects/segmentation_task/data/annotations/trimaps/"
image_files = os.listdir(image_dir)
#print(image_files)
image_files_edited= []
for name in image_files:
    if name.endswith(".jpg") == False:
        print(name)
    else:
        image_files_edited.append(name)
fname = image_files_edited[334]
fname_mask = fname.replace(".jpg", ".png")

print(mask_dir+'._'+fname_mask)
img = Image.open(mask_dir+fname_mask)
img2 = Image.open(image_dir+fname)
#img.show()
img = np.asarray(Image.open(mask_dir+fname_mask))
img2 = np.asarray(Image.open(image_dir+fname))
plt.imshow(img)
plt.figure()
plt.imshow(img2)
plt.show()

from PIL import Image as image
import numpy as np
from matplotlib import pyplot as plt
# %%
c = 1
gamma =
pic_a = image.open("Pictures/normal.PNG")
pic_b = image.open("Pictures/bright.PNG")
pic_c = image.open("Pictures/dark.PNG")
pic_d = image.open("Pictures/gray.PNG")
# %%
pic_a_matrix = np.array(pic_a)
row,col,dim = pic_a_matrix.shape
temp = np.zeros([row,col,dim])

# %%
"""
for k in range(dim):
    for i in range(row):
        for j in range(col):
            temp[i,j,k] = c*((pic_a_matrix[i,j,k]/255)**gamma)
"""

temp = c*(pic_a_matrix/255)**gamma

# %%
new = image.fromarray((temp * 255).astype(np.uint8)).convert('RGBA')
new.save("test.PNG")
#%%
plt.figure(figsize=(7,5))
plt.subplot(1,2,1), plt.title('pic_a')
plt.imshow(pic_a), plt.axis("off")

plt.subplot(1,2,2),plt.title('new')
plt.imshow(new),plt.axis("off")

plt.show()

import matplotlib.image as image
import os
import pandas as pd
import cv2
from tqdm import tqdm
import numpy as np
from PIL import Image
path = 'Datasets/Resized_syam/'
filename = 'syam.csv'
files = os.listdir(path)
dim = (100, 100)
cls = 1
df = pd.DataFrame(columns = [f'pix-{i}' for i in range(1, 1+(dim[0]*dim[1]))]+['class'])
for i in tqdm(range(1, 1+len(files))):
    img =Image.open(path+files[i-1])
    df.loc[i] = list(img.getdata()) + [cls]

df.to_csv(filename,index = False)
print('Task Completed')
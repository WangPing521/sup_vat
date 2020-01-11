import os
import torch
path = 'dataset/ACDC-all/val/img'
imgs = os.listdir(path)
n = len(imgs)
for i in range(n):
    char = int(os.path.basename(imgs[i])[16:-4])
    comm_char = os.path.basename(imgs[i])[:16]
    if char < 10:
        char = char.__str__()
        new_char = '0'+char+'.png'
        os.rename(r'dataset/ACDC-all/val/img/'+imgs[i],
        r'dataset/ACDC-all/val/img/'+comm_char+new_char)

import cv2
import numpy as np
import os

def equalize_hist(src):
    # 画像の高さ・幅を取得
    h, w = src.shape[0], src.shape[1]
    
    # 全画素数
    s = w * h
    
    # 画素値の最大値
    imax = src.max()
    imin = src.min()
    imean = src.mean()
    ivar = src.var()
    imedian = np.median(src)
    unique, freq = np.unique(src, return_counts=True)
    imode = unique[np.argmax(freq)]

    print(f'max:{imax}',f'min:{imin}',f'mean:{imean}',f'var:{ivar}',f'median:{imedian}',f'mode:{imode}', sep='\n')


# 入力画像を読み込み
img = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/"+"Cameraman.bmp", cv2.IMREAD_GRAYSCALE)

# 方法1(NumPyで実装)
dst = equalize_hist(img)
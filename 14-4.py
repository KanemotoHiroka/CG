import cv2
import numpy as np
import random
import math
import pandas as pd

N_ROW  = 128 # 画像の行 (縦方向) の数
N_COL  = 128 # 画像の列 (横方向) の数
pic_num =  3 # 作成する画像の枚数

radius = 48  # 球の半径
kyu_x  = 64  # 中心のx座標
kyu_y  = 64  # 中心のy座標
K_d    = 1 # 球の拡散反射率

OUTPUT_DIR = "input"; 

sn = np.zeros([N_ROW, N_COL, 3])
S  = np.zeros([pic_num, 3])

for i in range(0,N_ROW):
    for j in range(0,N_COL):
        if (i - kyu_x) ** 2 + (j - kyu_y) ** 2 <= radius ** 2:
            k = math.sqrt(radius ** 2 - (i - kyu_x) ** 2 - (j - kyu_y) ** 2)
            sn_tmp =  [i - kyu_x, j - kyu_y , k]
            sn_tmp = sn_tmp / np.linalg.norm(sn_tmp)
            sn[i,j,:] = sn_tmp




for k in range(0,pic_num):
    light = [random.random() - 0.5, random.random() - 0.5, random.random() / 2]
    light = light / np.linalg.norm(light)
    img_output = np.zeros([N_ROW, N_COL])

    for i in range(0,N_ROW):
        for j in range(0,N_COL):
            sn_tmp =  sn[i,j,:]
            if np.linalg.norm(sn_tmp) > 0:
                cos_theta = np.dot(light,sn_tmp)
                if cos_theta > 0:
                    img_output[i,j] = K_d * cos_theta * 255

    S[k,:] = light
    cv2.imwrite(OUTPUT_DIR + "/" + str(k + 1) + ".pgm", img_output)


np.savetxt(OUTPUT_DIR + "./light_source.txt", S) # 光源方向保存
np.save(OUTPUT_DIR + "./sn_true.npy", sn) # 正しい法線保存 (確認用)

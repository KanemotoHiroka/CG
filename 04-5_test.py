from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

import numpy as np
##from matplotlib import pyplot as plt
##from matplotlib.colors import Normalize              # カラーマップを自在に操作するために必要
from numba import jit                                # これが無いとおそろしく計算時間がかかる
import time                                          # 計算時間を見るために必要
 
t0 = time.time()
color_map = [[0]*3]*256
 
@jit                                                 # NumbaによるJust In Time Compileを実行
def julia(z_real, z_imag, n_max, a, b):
    Re, Im = np.meshgrid(z_real, z_imag)             # ReとImの組み合わせを計算
    n_grid = len(Re.ravel())                         # 組み合わせの総数
    z = np.zeros(n_grid)                             # ジュリア集合のデータ格納用空配列
 
    # zにジュリア集合に属するか否かのデータを格納していくループ
    for i in range(n_grid):
        c = complex(a, b)                            # 複素数cを定義
 
        # イタレーション回数nと複素数z0を初期化
        n = 0
        z0 = complex(Re.ravel()[i], Im.ravel()[i])
 
        # z0が無限大になるか、最大イタレーション数になるまでループする
        while np.abs(z0) < 1e20 and not n == n_max:
            z0 = z0 ** 2 + c                         # 漸化式を計算
            n += 1                                   # イタレーション数を増分
 
        # z0が無限大に発散する場合はn, 収束する場合は0を格納
        if n == n_max:
            z[i] = 0
        else:
            z[i] = n
 
        # 計算の進捗度をモニター(毎ループだと計算が遅くなるため)
        if i % 100000 == 0:
            print(i, '/',n_grid, (i/n_grid)*100)
    z = np.reshape(z, Re.shape)                      # 2次元配列(画像表示用)にリシェイプ
    z = z[::-1]                                      # imshow()で上下逆になるので予め上下反転
    return z
 
# 水平方向h(実部Re)と垂直方向v(虚部Im)の範囲を決める
h1 = -1.5
h2 = 1.5
v1 = -1.5
v2 = 1.5
 
# 分解能を設定
resolution = 1000
 
# 実部と虚部の軸データ配列、最大イタレーション数を設定
z_real = np.linspace(h1, h2, resolution)
z_imag = np.linspace(v1, v2, resolution)
n_max = 100
 
a = -0.8
b = 0.15
 
# 関数を実行し画像を得る
z = julia(z_real, z_imag, n_max, a, b)
 
t1 = time.time()
print('Calculation time=', float(t1 - t0), '[s]')

def calcColorMap():
    global color_map
    for i in range(256):
        r = 1.0
        g = 0.0
        b = 0.0
        s1 = 119
        s2 = 128
        s3 = 137
        if s3 <= i <= 256:
            r = 0.0
            g = 0.0
            b = 0.5/(256-s3)*(i - s3) + 0.5
        if s2 <= i <= s3:
            r = -1.0/(s3-s2)*(i - s2) + 1.0
            g = -0.5/(s3-s2)*(i - s2) + 0.5
            b = -0.5/(s3-s2)*(i - s2) + 1.0
        if s1 <= i <= s2:
            r = 0.5/(s2-s1)*(i - s1) + 0.5
            g = 0.5/(s2-s1)*(i - s1)
            b = 1.0/(s2-s1)*(i - s1)
        if i <= s1:
            r = -0.5/(s1)*i + 1.0
            g = 0.0
            b = 0.0
        if i == 127:
            r = 0
            g = 0
            b = 0
        color_map[i] = [r, g, b]

def draw_2D_ScalarField(sf, min, max):
    dx = 1.0/NX
    dy = 1.0/NY
    glBegin(GL_QUADS)
    for i in range(0, NX):
        x = i/NX
        for j in range(0, NY):
            y = j/NY

            index00 = int(255 * (sf[i][j] - min)/(max - min)) if sf[i][j] < max else 255 ## calculate index for color_map based on value of sf[i][j] ##
            glColor3f(color_map[index00][0], color_map[index00][1], color_map[index00][2]) ## specify the color to glColor3f using color_map ##
            glVertex2f(x, y)

            index10 = int(255 * (sf[i+1][j] - min)/(max - min)) if sf[i+1][j] < max else 255
            glColor3f(color_map[index10][0], color_map[index10][1], color_map[index10][2]) ## specify the color to glColor3f using color_map ##
            glVertex2f(x+1, y) ## specify 2D coordinate to glVertex2f ##

            index11 = int(255 * (sf[i+1][j+1] - min)/(max - min)) if sf[i+1][j+1] < max else 255 ## calculate index (index11) for color_map based on value of sf[i+1][j+1] ##
            glColor3f(color_map[index11][0], color_map[index11][1], color_map[index11][2])
            glVertex2f(x+1, y+1) ## specify 2D coordinate to glVertex2f ##

            index01 = int(255 * (sf[i][j+1] - min)/(max - min)) if sf[i][j+1] < max else 255 ## calculate index for color_map based on value of sf[i][j+1] ##
            glColor3f(color_map[index01][0], color_map[index01][1], color_map[index01][2]) ## specify the color to glColor3f using color_map ##
            glVertex2f(x, y+1) ## specify 2D coordinate to glVertex2f ##
    glEnd()

def reshape(width, height):
    global win_x, win_y
    glutReshapeWindow(width, height)
    win_x = width
    win_y = height
    glViewport(0, 0, win_x, win_y)

def idle():
    global step, metabo
    step += 1
    for i in range(len(metabo)):
       metabo[i].update(step/10)
    glutPostRedisplay()

def main():
    global metabo
    # Instantiate the Metaballs class and add to the global list named "metabo"
    m1 = julia(100, 50, 0)
    
      

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(win_x, win_y)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"julia")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init()
    glutIdleFunc(idle)
    glutMainLoop()

def init():
    glViewport(0, 0, win_x, win_y)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    """ gluOrtho2D(left, right, bottom, top) """
    gluOrtho2D(0.0, 1.0, 0.0, 1.0)    # The coordinate system to draw


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Calculate a scalar field from some metaball
    calcScalarFieldBy(metabo, 0.25)

    # Draw a scalar field
    draw_2D_ScalarField(scalar_field, -100, 100)

    glFlush()
    glutSwapBuffers()


if __name__ == "__main__":
    calcColorMap()
    main()
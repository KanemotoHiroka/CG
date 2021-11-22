from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(300, 300)     # window size
    glutInitWindowPosition(100, 100) # window position
    glutCreateWindow(b"Checkerboard")      # show window
    glutDisplayFunc(display)         # draw callback function
    glutReshapeFunc(reshape)         # resize callback function
    init(300, 300)
    glutMainLoop()

def init(width, height):
    """ initialize """
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST) # enable shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    ##set perspective
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

def drawTriangle():
    glBegin(GL_LINE_LOOP)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    glVertex3f(1,1,0)
    glEnd()


def line(sx,sy,sz):
    arr=[[1,sx,0,0],[sy,1,0,0],[sz,0,1,0],[0,0,0,1]]
    arr1=[0,0,0,1]
    arr2=[1,0,0,1]
    arr3=[1,1,0,1]
    l_1=np.matmul(arr, arr1)
    l_2=np.matmul(arr, arr2)
    l_3=np.matmul(arr, arr3)
    glBegin(GL_TRIANGLES)
    glVertex3f(l_1[0],l_1[1],l_1[2])
    glVertex3f(l_2[0],l_2[1],l_2[2])
    glVertex3f(l_3[0],l_3[1],l_3[2])
    glEnd()
    

def display():
    """ display """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    ##set camera
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    drawTriangle()
    glColor3f(0.0, 1.0, 0.0)
    line(0,-2,0)
    #glColor3f(0.0, 1.0, 1.0)
    #line(0,0,0,-2)
    glColor3f(0.0, 0.0, 1.0)
    line(0,0,-2)

    

    glFlush()  # enforce OpenGL command

def reshape(width, height):
    """callback function resize window"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

if __name__ == "__main__":
    main()
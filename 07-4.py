from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

win_x = 400
win_y = 400

dt = 0.002
t = 0
ball_x, ball_y = 0.5, 0.5
ball_vx, ball_vy = 0.0, 0.0

natural_length = 0.5
frame_no = 0

def draw_ball(x, y, r):
    glBegin(GL_POLYGON)
    dtheta = 0
    while dtheta < 2*math.pi:
        dx = r*math.cos(dtheta) + x
        dy = r*math.sin(dtheta) + y

        glVertex2f(dx, dy)

        dtheta += math.pi/30
    glEnd()


def reshape(width, height):
    global win_x, win_y
    glutReshapeWindow(width, height)
    win_x = width
    win_y = height
    glViewport(0, 0, win_x, win_y)


def idle():
    global t
    t += dt
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(win_x, win_y)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"7-4")
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
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)    # The coordinate system to draw


def display():
    global frame_no

    glClear(GL_COLOR_BUFFER_BIT)

    x = math.cos(t)/(1+math.sin(t)**2)
    y = math.sin(t)*math.cos(t)/(1+math.sin(t)**2)
    r = x
    b = 0
    if x < 0:
        b = -x
    glColor3f(r, 0.0, b)
    draw_ball(x, y, 0.2)

    glFlush()
    glutSwapBuffers()


if __name__ == "__main__":
    main()
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle_ea = 0
angle_mo = 0
angle_me = 0
angle_ve = 0
angle_ma = 0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D_anime_template")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    glutMainLoop()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
     #太陽
    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(0.4, 20, 20)
    #地球
    glRotatef(angle_ea, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 2.0)
    glColor3f(0.0, 0.945, 1.0)
    glutSolidSphere(0.2, 20, 20)
    glTranslatef(0.0, 0.0, -2.0)
    glRotatef(-angle_ea, 0.0, 1.0, 0.0)
    #月
    glRotatef(angle_mo, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 2.0)
    glColor3f(1.0, 1.0, 1.0)
    glutSolidSphere(0.1, 20, 20)
    glTranslatef(0.0, 0.0, -2.0)
    glRotatef(-angle_mo, 0.0, 1.0, 0.0)
    #水星
    glRotatef(angle_me, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 2.0)
    glColor3f(0.0, 0.0, 1.0)
    glutSolidSphere(0.15, 20, 20)
    glTranslatef(0.0, 0.0, -2.0)
    glRotatef(-angle_me, 0.0, 1.0, 0.0)
     #金星
    glRotatef(angle_ve, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 2.0)
    glColor3f(1.0, 0.945, 0.0)
    glutSolidSphere(0.2, 20, 20)
    glTranslatef(0.0, 0.0, -2.0)
    glRotatef(-angle_ve, 0.0, 1.0, 0.0)
     #火星
    glRotatef(angle_ma, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 2.0)
    glColor3f(1,0,0)
    glutSolidSphere(0.15, 20, 20)
    glTranslatef(0.0, 0.0, -2.0)
    glRotatef(-angle_ma, 0.0, 1.0, 0.0)
    glutSwapBuffers()
    
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def idle():
    global angle_mo,angle_me,angle_ea,angle_ve,angle_ma

    angle_mo += ((360/27)/100)
    
    angle_me += ((360/88)/100)
    
    angle_ea += ((360/365)/100)
    
    angle_ve += ((360/225)/100)
    
    angle_ma += ((360/687)/100)

    glutPostRedisplay()

if __name__ == "__main__":
    main()
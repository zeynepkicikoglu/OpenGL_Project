from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    #glOrtho(left, right, up, bottom, near, far)
    glOrtho(-5.0, 5.0, -5.0, 5.0, -1.0, 20.0)

    #gluLookAt(eyex, eyey, eyez, targetx, targety, targetz, upx, upy, upz)
    gluLookAt(0, 0, -1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor(1,0.5,1)
    glutWireTeapot(1)

    glColor(0, 0.5, 1)
    for i in range(1, 5):
        glPushMatrix()
        glTranslate(i * -1, 0, i)
        glutWireTeapot(1)
        glPopMatrix()

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(320,320)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b" glOrtho Sample ")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()



main()
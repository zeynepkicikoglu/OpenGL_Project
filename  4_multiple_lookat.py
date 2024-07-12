from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glViewport(0, 300, 300, 300)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -3.0, 3.0, 1.0, 50.0)
    gluLookAt(0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor(1.0, 0.5, 0.5)
    glutWireTeapot(1)

    glViewport(300, 300, 300, 300)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -3.0, 3.0, 1.0, 50.0)
    gluLookAt(5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor(1.0, 0.5, 0.5)
    glutWireTeapot(1)

    glViewport(0, 0, 300, 300)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -3.0, 3.0, 1.0, 50.0) #acı daha ıyı olsun dıye orthondontık projeksıyon var
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)#bu yapı ile caydanlıgı farklı acılardan goruruz
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor(1.0, 0.5, 0.5)
    glutWireTeapot(1)

    glViewport(300, 0, 300, 300)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70.0, 1.0, 1, 50)
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(30.0, 1.0, 0.0, 0.0)
    glRotatef(30, 0.0, 1.0, 0.0)
    glColor(0.0, 0.5, 0.5)
    glutWireTeapot(1)

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Multiple LookAt 3D teapot Sample")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()


if __name__ == '__main__':
    main()
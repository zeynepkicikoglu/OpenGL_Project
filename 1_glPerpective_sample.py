from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective( fovy, aspect, zNear, zFar )
    #boy/en
    gluPerspective(150, 1, 1, 100)

    gluLookAt(0, 0, -1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor(1, 0.5, 1)
    glutWireTeapot(1)

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(320,320)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"glPerspective teapot Sample")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()

main()
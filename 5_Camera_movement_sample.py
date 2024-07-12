from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math as m

# angle of rotation for the camera direction
angle=0.0
# actual vector representing the camera's direction
target_x=0.0
target_z=0.0
#XZ position of the camera
eyex=0.0
eyez=-50.0


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Derinlik tamponunu temizle
    glClearColor(1.0, 1.0, 1.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(150, 1.5, -1, 20)
    glOrtho(-5.0, 5.0, -5.0, 5.0, -1.0, 20.0)
    gluLookAt(eyex, 0.0, eyez, target_x, 0.0, target_z, 0.0, 1.0, 0.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor(1, 0.5, 1)
    glutWireTeapot(20)

    #glutSwapBuffers()

    glFlush()


def keyPressed(*args):
    global angle, eyex, target_x, eyez, target_z
    if args[0] == b"a":
        target_x += 1
    elif args[0] == b"d":
        target_x -= 1
    elif args[0] == b"w":
        eyez += 0.5
    elif args[0] == b"s":
        eyez -= 0.5
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(320, 320)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"3D teapot Sample")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyPressed)
    glEnable(GL_DEPTH_TEST)  # Derinlik testini etkinleştir
    glutMainLoop()


if __name__ == '__main__':
    main()

# PyFunc.py
# Plotting functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, random

points = [[0.0, 0.0]]


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)


def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)

    # X koordinat DÃ¼zlemi
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0)
    glVertex2f(5.0, 0)
    glEnd()

    # Y koordinat DÃ¼zlemi
    glBegin(GL_LINES)
    glVertex2f(.0, -5.0)
    glVertex2f(.0, 5.0)
    glEnd()

    glPointSize(5.0)
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        R = random.random()
        G = random.random()
        B = random.random()

        glBegin(GL_POINTS)
        glColor3f(R, G, B)
        glVertex2f(x, y)
        glEnd()

    glFlush()


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    print("Mouse bastım")
    print(args)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Function Plotter")
    glutDisplayFunc(plotfunc)
    glutMouseFunc(keyPressed)
    init()
    glutMainLoop()


main()
# End of program
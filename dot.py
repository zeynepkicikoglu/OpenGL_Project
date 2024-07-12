from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(0.5, 0.5)  # İlk nokta
    glVertex2f(0.5, -0.5)  # İkinci nokta
    glEnd()
    glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Plot Points")
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()
if __name__ == "__main__":
    main()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) #arka plan rengi mat ve beyaz olarak ayarlandı.
    gluOrtho2D(-5.0, 5.0, -5.0, 25.0)  # x ekseni -5 ile 5 arasında, y ekseni -5 ile 25 arasında olacak şekilde ayarlandı.

def plot_function():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2.0)
    
    glBegin(GL_LINE_STRIP)
    for x in range(-50, 51):  # x değerleri -5 ile 5 arasında
        glVertex2f(x / 10.0, (x / 10.0) ** 2)  # f(x) = x^2 fonksiyonu
    glEnd()
    
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Plot Function")
    glutDisplayFunc(plot_function)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Pencere boyutları
window_width = 800
window_height = 600

# Fonksiyon tanımı
def f(x):
    return 2 * x**3 + 3 * x**2 - 5

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-3.0, 3.0, -50.0, 50.0)  # x aralığı: [-3, 3], y aralığı: [-50, 50]

def plot_function():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2.0)
    
    glBegin(GL_LINE_STRIP)
    # [-3, 3] aralığında x değerlerini hesapla ve çiz
    for x in range(-300, 301):
        x /= 100.0
        glVertex2f(x, f(x))
    glEnd()
    
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Plot Function")
    glutDisplayFunc(plot_function)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()

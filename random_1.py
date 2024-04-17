from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random as rd

import sys
# Ardından, random() fonksiyonuna rd.random() şeklinde erişebilirsiniz.


# Pencere boyutları
window_width = 500
window_height = 500

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0, window_width, 0, window_height)

def draw_random_point():
    # Rastgele bir renk oluştur
    glColor3f(rd.random(), rd.random(), rd.random())
    # Rastgele bir konum seç
    x = rd.randint(0, window_width)
    y = rd.randint(0, window_height)
    # Noktayı çiz
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def keyboard(key, x, y):
    # Herhangi bir tuşa basıldığında draw_random_point fonksiyonunu çağır
    draw_random_point()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Random Point on Keypress")
    glutDisplayFunc(draw_random_point)
    init()
    # Klavye işlemi yakalama
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()

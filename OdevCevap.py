from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

#Kırmızı olarak koyu kırmızı kullandım ve başlangıçta araba kırmızı
R=0.6
G=0.0
B=0.0

#Dikdörtgen çizmek için fonksiyon
def plotQuad():
    glBegin(GL_QUAD_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, 0.5)
    glVertex2f(1.0, 0.5)
    glEnd()

#Çizilen dikdörtgenlerin çerçevesini çizmek için fonksiyon
def plotLines():
    glLineWidth(3)
    glBegin(GL_LINES)

    glVertex2f(0.0, 0.0)
    glVertex2f(1.0, 0.0)

    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.5)

    glVertex2f(0.0, 0.5)
    glVertex2f(1.0, 0.5)

    glVertex2f(1.0, 0.5)
    glVertex2f(1.0, 0.0)

    glEnd()

#Tekerlekleri çizmek için daire çizen fonksiyon
def plotCircle():
    glPointSize(5.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        x = 0.2 * math.sin((i) * 3.14 / 180)
        y = 0.2 * math.cos((i) * 3.14 / 180)
        glVertex2f(x, y)

    glEnd()

#Arabanın kendisini çizmek için fonksiyon
def plotpoints():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    # Arka kaput için
    glViewport(0, 0, 250, 250)
    glColor3f(R, G, B)
    plotQuad()
    glColor3f(0, 0, 0)
    plotLines()

    # Ön kaput için
    glViewport(125, 0, 250, 250)
    glColor3f(R, G, B)
    plotQuad()
    glColor3f(0, 0, 0)
    plotLines()

    # Camlar için
    glViewport(63, 63, 250, 250)
    glColor4f(0.5, 1.0, 1.0, 1.0)
    plotQuad()
    glColor3f(0, 0, 0)
    plotLines()

    # Arka tekerlek için
    glViewport(25, -25, 250, 250)
    glColor3f(0, 0, 0)
    plotCircle()

    # Ön tekerlek için
    glViewport(220, -25, 250, 250)
    glColor3f(0, 0, 0)
    plotCircle()

    glutSwapBuffers()


def keyPressed(*args):
    global R
    global G
    global B
    print(args[0])
    # Escape code=\x1b
    if args[0] == b"\x1b":
        sys.exit()
    elif args[0] == bytes('r', 'utf-8'):
        #Kırmızı renk için koyu kırmızı
        R = 0.6
        G = 0.0
        B = 0.0
    elif args[0] == bytes('g', 'utf-8'):
        #Yeşil renk için açık bir yeşil
        R = 0.5
        G = 1.0
        B = 0.5
    elif args[0] == bytes('b', 'utf-8'):
        #Mavi renk için koyu bir mavi
        R = 0.0
        G = 0.0
        B = 0.5

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Aleyna's Car")
    glutDisplayFunc(plotpoints)
    glutKeyboardUpFunc(keyPressed)
    glutMainLoop()


main()
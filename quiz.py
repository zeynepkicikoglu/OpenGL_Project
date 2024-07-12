from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

car_position_x = 0.0

R = 0.6
G = 0.0
B = 0.0

def plotQuad():
    glBegin(GL_QUAD_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, 0.5)
    glVertex2f(1.0, 0.5)
    glEnd()

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

def plotCircle():
    glPointSize(5.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        x = 0.2 * math.sin((i) * 3.14 / 180)
        y = 0.2 * math.cos((i) * 3.14 / 180)
        glVertex2f(x, y)
    glEnd()

def plotCar():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(int(car_position_x), 0, 250, 250)
    glColor3f(R, G, B)
    plotQuad()
    glColor3f(0, 0, 0)
    plotLines()

    glViewport(int(car_position_x) + 125, 0, 250, 250)
    glColor3f(R, G, B)
    plotQuad()
    glColor3f(0, 0, 0)
    plotLines()

    glViewport(int(car_position_x) + 63, 63, 250, 250)
    glColor4f(0.5, 1.0, 1.0, 1.0)
    plotQuad()
    glColor3f(0, 0, 0)
    plotLines()

    glViewport(int(car_position_x) + 25, -25, 250, 250)
    glColor3f(0, 0, 0)
    plotCircle()

    glViewport(int(car_position_x) + 220, -25, 250, 250)
    glColor3f(0, 0, 0)
    plotCircle()

    glViewport(200, -300, 600, 800)
    glPushMatrix()
    glColor3f(0.5, 0.25, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(0.4, 0.0)
    glVertex2f(0.4, 0.4)
    glVertex2f(0.6, 0.4)
    glVertex2f(0.6, 0.0)
    glEnd()
    glColor3f(0.0, 0.5, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.3, 0.4)
    glVertex2f(0.5, 0.8)
    glVertex2f(0.7, 0.4)
    glEnd()
    glPopMatrix()

    glutSwapBuffers()

def is_collision(x):
    tree_x = 200
    tree_width = 60
    if x < tree_x or x > tree_x + tree_width:
        return False
    return True

def mouseButton(button, state, x, y):
    global car_position_x
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        new_position_x = car_position_x - 20.0
        if is_collision(new_position_x):
            return
        car_position_x = new_position_x
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        new_position_x = car_position_x + 20.0
        if is_collision(new_position_x):
            return
        car_position_x = new_position_x
    glutPostRedisplay()

def keyPressed(*args):
    pass

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"QUIZ")
    glutDisplayFunc(plotCar)
    glutMouseFunc(mouseButton)
    glutKeyboardUpFunc(keyPressed)
    glutMainLoop()

main()
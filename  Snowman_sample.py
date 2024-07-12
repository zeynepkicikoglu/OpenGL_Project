from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math as m

# https://www.lighthouse3d.com/tutorials/glut-tutorial/keyboard-example-moving-around-the-world/

# angle of rotation for the camera direction
angle = 0.0
# // actual vector representing the camera's direction
deltax = 0.0
deltaz = -1.0
# XZ position of the camera
eye_x = 0.0
eye_z = 5.0


def drawSnowMan():
    glColor3f(1.0, 1.0, 1.0)
    # Draw Body
    glTranslatef(0.0, 0.75, 0.0)
    glutSolidSphere(0.75, 20, 20)
    # Draw Head
    glTranslatef(0.0, 1.0, 0.0)
    glutSolidSphere(0.25, 20, 20)
    # Draw Eyes
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glTranslatef(0.05, 0.10, 0.18)
    glutSolidSphere(0.05, 10, 10)
    glTranslatef(-0.1, 0.0, 0.0)
    glutSolidSphere(0.05, 10, 10)
    glPopMatrix()
    # Draw Nose
    glColor3f(1.0, 0.5, 0.5)
    glutSolidCone(0.08, 0.5, 10, 2)


def renderScene():
    # glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 4.0 / 3.0, 1, 40)
    # glOrtho(-50,50,-50,50,-50,50)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Set the camera
    gluLookAt(eye_x, 1.0, eye_z, (eye_x + deltax), 1.0, (eye_z + deltaz), 0.0, 1.0, 0.0)

    # // Draw ground
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_QUADS)
    glVertex3f(-100.0, 0.0, -100.0)
    glVertex3f(-100.0, 0.0, 100.0)
    glVertex3f(100.0, 0.0, 100.0)
    glVertex3f(100.0, 0.0, -100.0)
    glEnd()

    # // Draw 36 SnowMen
    for i in range(-3, 3):
        for j in range(-3, 3):
            glPushMatrix()
            glTranslatef(i * 10.0, 0, j * 10.0)
            drawSnowMan()
            glPopMatrix()
    glutSwapBuffers()


def keyPressed(*args):
    fraction = 0.1
    global angle, eye_x, deltax, eye_z, deltaz
    if args[0] == b"a":
        angle -= 0.01
        deltax = m.sin(angle)
        deltaz = -m.cos(angle)
    elif args[0] == b"d":
        angle += 0.01
        deltax = m.sin(angle)
        deltaz = -m.cos(angle)
    elif args[0] == b"w":
        eye_x += deltax * fraction
        eye_z += deltaz * fraction
    elif args[0] == b"s":
        eye_x -= deltax * fraction
        eye_z -= deltaz * fraction
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(320, 320)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Snowman Sample")
    glutDisplayFunc(renderScene)
    glutIdleFunc(renderScene)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()
    glEnable(GL_DEPTH_TEST)


main()
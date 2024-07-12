from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glFrustum(xwMin, xwMax, ywMin, ywMax, dnear, dfar)
    glFrustum(-15.0, 15.0, -5.0, 5.0, 1.0, 20.0)

    gluLookAt(0, 0, -1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPushMatrix()
    glColor(1, 0.5, 1)
    glTranslate(3, 0, 0)
    glutWireTeapot(1)
    glPopMatrix()
    #Artan z değerine göre ekrana 5 adet çaydanlık yerleştirin.


        #i=[0,1,2,3,4]
    for i in range(5):
        glPushMatrix()
        glColor(0, 1, 0)
        glTranslate(i*-2,i,i*3)
        glutWireTeapot(1)
        glPopMatrix()

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(320,320)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"glFrustum teapot Sample")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)  # OpenGL bağlamını oluşturduktan sonra glutIdleFunc() fonksiyonunu çağırın
    glutMainLoop()


if __name__ == '__main__':
    main()
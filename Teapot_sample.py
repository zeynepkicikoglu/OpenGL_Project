from OpenGL.GLUT import *
from OpenGL.GL import *

import sys
def draw():
    #glutWireTeapot(0.5)
    #glutWireSphere (0.75, 25, 25)

    #glutWireCube (1.0)
    #glutWireTetrahedron ()

    #glutWireCone(1, 1, 10, 10)
    #glutWireSphere(0.5,10,10)
    glutWireTorus(0.5,1.5,10,10)
    glFlush()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutInitWindowPosition(20,22)
glutCreateWindow(bytes("MyWindow","ascii"))
glutDisplayFunc(draw)
glutMainLoop()




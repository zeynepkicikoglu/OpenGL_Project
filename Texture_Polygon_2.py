from PIL import Image
from OpenGL.GLUT import *
from OpenGL.GL import *

id1=0
id2=0

def LoadTexture(file):
    image = Image.open(file)
    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBX")

    id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

    return id


def display():
    """Glut display function."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glScalef(0.5,0.5,0.5)
    glTranslatef(-1,0,0)
    glBindTexture(GL_TEXTURE_2D, id1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(-0.5, 0.5, 0)
    glTexCoord2f(0, 0)
    glVertex3f(-0.5, -0.5, 0)
    glTexCoord2f(1, 0)
    glVertex3f(0.5, -0.5, 0)
    glTexCoord2f(1, 1)
    glVertex3f(0.5, 0.5, 0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glScalef(0.5, 0.5, 0.5)
    glTranslatef(1, 0, 0)
    glBindTexture(GL_TEXTURE_2D, id2)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(-0.5, 0.5, 0)
    glTexCoord2f(0, 0)
    glVertex3f(-0.5, -0.5, 0)
    glTexCoord2f(1, 0)
    glVertex3f(0.5, -0.5, 0)
    glTexCoord2f(1, 1)
    glVertex3f(0.5, 0.5, 0)
    glEnd()
    glPopMatrix()

    glutSwapBuffers()


def init():
    global id1,id2
    glActiveTexture(GL_TEXTURE0)
    id1=LoadTexture("Wall.bmp")
    id2 = LoadTexture("brick.jpg")
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Texture Sample 2   ")
init()
glutDisplayFunc(display)
glutMainLoop()
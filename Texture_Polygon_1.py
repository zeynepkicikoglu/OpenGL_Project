from PIL import Image
from OpenGL.GLUT import *
from OpenGL.GL import *

def display():
    """Glut display function."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 1, 1)

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

    glutSwapBuffers()


def init():
    """Glut init function."""
    im = Image.open("brick.jpg")
    xSize = im.size[0]
    ySize = im.size[1]
    rawReference = im.tobytes("raw", "RGB")

    glClearColor(0, 0, 0, 0)

    # Create Texture
    id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id)  # bind Texture, 2d texture (x and y size)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, xSize, ySize, 0, GL_RGB, GL_UNSIGNED_BYTE, rawReference)
    glEnable(GL_TEXTURE_2D)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Texture Sample 1")
init()
glutDisplayFunc(display)
glutMainLoop()
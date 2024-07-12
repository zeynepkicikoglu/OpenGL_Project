from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def load_obj(filename):
    vertices = []
    faces = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('v '):
                vertex = list(map(float, line.strip().split()[1:]))
                vertices.append(vertex)
            elif line.startswith('f '):
                face = [int(vertex.split('/')[0]) for vertex in line.strip().split()[1:]]
                faces.append(face)
    return vertices, faces


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)  # Kamera konumunu ayarlar
    glColor3f(1, 1, 1)  # Objeyi beyaz renkte çizer
    draw_obj(vertices, faces)
    glutSwapBuffers()

def draw_obj(vertices, faces):
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_index in face:
            vertex = vertices[vertex_index - 1]
            glVertex3fv(vertex)
    glEnd()

if __name__ == "__main__":
    # Obj dosyasının adını ve yolunu belirtin
    obj_file = "Tree1.obj"
    vertices, faces = load_obj(obj_file)

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'3D Obj Viewer')
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutMainLoop()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def load_obj(filename):
    vertices = []
    faces = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 0:
                if parts[0] == 'v':
                    vertices.append(list(map(float, parts[1:])))
                elif parts[0] == 'f':
                    face = [int(vertex.split('/')[0]) for vertex in parts[1:]]
                    faces.append(face)

    return vertices, faces

def render_obj(filename):
    vertices, faces = load_obj(filename)

    scaled_vertices = [[vertex[0] * 4, vertex[1] * 4, vertex[2] * 4] for vertex in vertices]

    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_index in face:
            vertex = scaled_vertices[vertex_index - 1]
            glVertex3f(*vertex)
    glEnd()

car_position_x = 0.0
car_direction = 1  # 1 sağa, -1 sola hareket etmek için yön belirleyici

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
    global car_position_x

    # Arka plan rengini beyaz yap
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # Kuş modelini hareket ettir
    car_position_x += 0.1  # Kuşun ileri hareket hızı

    # Eğer kuş ekranın sağ sınırına ulaşırsa, tekrar sola dön
    if car_position_x > 200:
        car_position_x = -200

    # Kuş modelini sol üst köşede ve sabit bir yükseklikte görüntüle
    glViewport(400, 400, 250, 250)
    glPushMatrix()
    glTranslatef(car_position_x, 0, 0)  # Kuşu hareket ettir
    glColor3f(1.0, 1.0, 0.0)  # Sarı renk
    render_obj("Cardinalis.obj")  # Kuş modelini render et
    glPopMatrix()

    # Diğer çizimler için
    glViewport(0, 0, 1000, 1000)  # Ekranı tamamen dolduracak şekilde ayarla

    # Araba ve diğer çizimleri gerçekleştir
    glColor3f(R, G, B)
    glViewport(int(car_position_x), 0, 250, 250)
    plotQuad()
    glColor3f(0, 0, 0)
    plotLines()

    glViewport(int(car_position_x) + 125, 0, 250, 250)
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

    glutSwapBuffers()  # Pencereyi yenile

    # Yeniden çiz
    glutPostRedisplay()



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


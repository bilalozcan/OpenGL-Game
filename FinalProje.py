''' Final Proje Ödevi
    Beni Yakala Oyunu
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# angle of rotation for the camera direction
angle = 0.0
# // actual vector representing the camera's direction
deltax = 0.0
deltaz = -1.0
# XZ position of the camera
eye_x = 0.0
eye_z = 5.0


def InitGL():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 4.0 / 3.0, 1, 40)
    # glOrtho(-50,50,-50,50,-50,50)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Set the camera
    gluLookAt(eye_x, 1.0, eye_z, (eye_x + deltax), 1.0, (eye_z + deltaz), 0.0, 3.0, -5.0)


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.55, 0.92, 0.49)
    glBegin(GL_QUADS)
    glVertex3f(-100.0, 0.0, -100.0)
    glVertex3f(-100.0, 0.0, 100.0)
    glVertex3f(100.0, 0.0, 100.0)
    glVertex3f(100.0, 0.0, -100.0)
    glEnd()

    ''' glBegin(GL_LINE_LOOP)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(0, 0)
    glVertex2f(0.1, 0)
    glVertex2f(0.1, -0.1)
    glVertex2f(0, -0.1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glEnd()'''
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(800, 400)
    glutInitWindowPosition(800, 400)
    glutCreateWindow(b"Final Proje")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    InitGL()
    glutMainLoop()


main()

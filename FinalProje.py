''' '''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def InitGL():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-11.0, 11.0, -11.0, 11.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, 400, 400)
    glutSwapBuffers()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(800, 400)
    glutInitWindowPosition(400, 400)
    glutCreateWindow(b"Final Proje")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    InitGL()
    glutMainLoop()


main()

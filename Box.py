from OpenGL.GLUT import *
from RectangularPrism import *


def getBox(w,h,d,x,y,z):
    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(x, y, z)
    RectangularPrism(w, h, d)
    glPopMatrix()
    return x-w,x+w,z-d,z+d



from OpenGL.GLUT import *
from RectangularPrism import *


def getBox(w,h,d,x,y,z,r,g,b):
    glPushMatrix()
    glColor3f(r, g, b)
    glTranslatef(x, y, z)
    RectangularPrism(w, h, d)
    glPopMatrix()
    return x-w,x+w,z-d,z+d



from OpenGL.GLUT import *
from Cube import *
from MapTexture import *

def getBox(w,h,d,x,y,z,string):
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(x, y, z)
    glActiveTexture(GL_TEXTURE0)
    LoadTextures(string)
    Cube(w, h, d)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    return x-w,x+w,z-d,z+d



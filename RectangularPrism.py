from OpenGL.GL import *

def RectangularPrism(width, height, depth):
    # Üst Yüzey
    glBegin(GL_QUADS)
    glVertex3f(width, height, -depth)
    glVertex3f(-width, height, -depth)
    glVertex3f(-width, height, depth)
    glVertex3f(width, height, depth)

    # Alt Yüzey
    glVertex3f(width, -height, depth)
    glVertex3f(-width, -height, depth)
    glVertex3f(-width, -height, -depth)
    glVertex3f(width, -height, -depth)

    # Ön Yüzey
    glVertex3f(width, height, depth)
    glVertex3f(-width, height, depth)
    glVertex3f(-width, -height, depth)
    glVertex3f(width, -height, depth)

    # Arka Yüzey
    glVertex3f(width, -height, -depth)
    glVertex3f(-width, -height, -depth)
    glVertex3f(-width, height, -depth)
    glVertex3f(width, height, -depth)

    # Sol Yüzey
    glVertex3f(-width, height, depth)
    glVertex3f(-width, height, -depth)
    glVertex3f(-width, -height, -depth)
    glVertex3f(-width, -height, depth)

    # Sağ Yüzey
    glVertex3f(width, height, -depth)
    glVertex3f(width, height, depth)
    glVertex3f(width, -height, depth)
    glVertex3f(width, -height, -depth)
    glEnd()
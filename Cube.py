from OpenGL.GL import *

def Cube(width, height, depth):
    # Üst Yüzey
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0), glVertex3f(width, height, -depth)
    glTexCoord2f(1.0, 0.0), glVertex3f(-width, height, -depth)
    glTexCoord2f(1.0, 1.0), glVertex3f(-width, height, depth)
    glTexCoord2f(0.0, 1.0), glVertex3f(width, height, depth)

    # Alt Yüzey
    glTexCoord2f(1.0, 0.0), glVertex3f(width, -height, depth)
    glTexCoord2f(1.0, 1.0), glVertex3f(-width, -height, depth)
    glTexCoord2f(0.0, 1.0), glVertex3f(-width, -height, -depth)
    glTexCoord2f(0.0, 0.0), glVertex3f(width, -height, -depth)

    # Ön Yüzey
    glTexCoord2f(0.0, 1.0), glVertex3f(width, height, depth)
    glTexCoord2f(0.0, 0.0), glVertex3f(-width, height, depth)
    glTexCoord2f(1.0, 0.0), glVertex3f(-width, -height, depth)
    glTexCoord2f(1.0, 1.0), glVertex3f(width, -height, depth)

    # Arka Yüzey
    glTexCoord2f(1.0, 1.0), glVertex3f(width, -height, -depth)
    glTexCoord2f(0.0, 1.0), glVertex3f(-width, -height, -depth)
    glTexCoord2f(0.0, 0.0), glVertex3f(-width, height, -depth)
    glTexCoord2f(1.0, 0.0), glVertex3f(width, height, -depth)

    # Sol Yüzey
    glTexCoord2f(1.0, 0.0), glVertex3f(-width, height, depth)
    glTexCoord2f(1.0, 1.0), glVertex3f(-width, height, -depth)
    glTexCoord2f(0.0, 1.0), glVertex3f(-width, -height, -depth)
    glTexCoord2f(0.0, 0.0), glVertex3f(-width, -height, depth)

    # Sağ Yüzey
    glTexCoord2f(0.0, 0.0), glVertex3f(width, height, -depth)
    glTexCoord2f(1.0, 0.0), glVertex3f(width, height, depth)
    glTexCoord2f(1.0, 1.0), glVertex3f(width, -height, depth)
    glTexCoord2f(0.0, 1.0), glVertex3f(width, -height, -depth)
    glEnd()
from OpenGL.GL import *

''' Verilen width, height ve depth değerleri boyutunda
    dikdörtgenler prizması oluşturan fonksiyon
'''
def RectangularPrism(width, height, depth):

    #Üst Yüzey
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

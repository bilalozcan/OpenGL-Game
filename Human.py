from OpenGL.GLUT import *
from RectangularPrism import *
def drawHuman():
    # KAFA
    glPushMatrix()
    glColor3f(0, 1, 0)
    RectangularPrism(0.3, 0.3, 0.3)
    glPopMatrix()

    # BOYUN
    glPushMatrix()
    glTranslatef(0, -0.4, 0)
    glColor3f(0, 0, 1)
    RectangularPrism(0.1, 0.1, 0.1)
    glPopMatrix()

    # GÖVDE
    glPushMatrix()
    glTranslatef(0, -1.5, 0)
    glColor3f(1, 0, 1)
    RectangularPrism(0.5, 1, 0.25)
    glPopMatrix()

    # SAĞ KOL
    glPushMatrix()
    glTranslatef(0.5, -0.65, 0)
    glColor3f(0, 1, 1)
    glutSolidSphere(0.22,20,20)
    glColor3f(0.23, 0.78, 1)
    glTranslatef(0.18, -0.65, 0)
    RectangularPrism(0.15, 0.8, 0.25)
    glPopMatrix()

    # SOL KOL
    glPushMatrix()
    glTranslatef(-0.5, -0.65, 0)
    glColor3f(0.23, 0.45, 0.36)
    glutSolidSphere(0.22, 20, 20)
    glColor3f(0.88, 0.88, 0.12)
    glTranslatef(-0.18, -0.65, 0)
    RectangularPrism(0.15, 0.8, 0.25)
    glPopMatrix()

    # SAĞ BACAK
    glPushMatrix()
    glTranslatef(0.3, -2.6, 0)
    glColor3f(0.44, 0.77, 0.66)
    glutSolidSphere(0.22, 20, 20)
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(0, -0.95, 0)
    RectangularPrism(0.15, 1, 0.25)
    glPopMatrix()

    # SOL BACAK
    glPushMatrix()
    glTranslatef(-0.3, -2.6, 0)
    glColor3f(0.44, 0.77, 0.66)
    glutSolidSphere(0.22, 20, 20)
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(0, -0.95, 0)
    RectangularPrism(0.15, 1, 0.25)
    glPopMatrix()

    # SAĞ AYAK
    glPushMatrix()
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(0.3, -4.65, -0.165)
    RectangularPrism(0.15, 0.1, 0.4)
    glPopMatrix()

    # SOL AYAK
    glPushMatrix()
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(-0.3, -4.65, -0.165)
    RectangularPrism(0.15, 0.1, 0.4)
    glPopMatrix()
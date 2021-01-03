from OpenGL.GLUT import *
from RectangularPrism import *

def drawDog(human):
    # GÖVDE
    glPushMatrix()
    glColor3f(0.37, 0.18, 0)
    RectangularPrism(0.312, 0.312, 1)
    glPopMatrix()

    # KAFA
    glPushMatrix()
    glTranslatef(0, 0, -0.4)
    glColor3f(0.20, 0.188, 0)
    RectangularPrism(0.4, 0.4, 0.4)
    glPopMatrix()

    # SAĞ KULAK
    glPushMatrix()
    glTranslatef(0.2, 0.4, -0.9)
    glColor3f(0, 0.45, 0)
    RectangularPrism(0.1, 0.1, 0.03)
    glPopMatrix()

    # SOL KULAK
    glPushMatrix()
    glTranslatef(-0.2, 0.4, -0.9)
    glColor3f(0, 0.45, 0)
    RectangularPrism(0.1, 0.1, 0.03)
    glPopMatrix()

    # SAĞ GÖZ
    glPushMatrix()
    glTranslatef(0.15, 0.18, -1)
    glColor3f(0, 0, 0)
    RectangularPrism(0.05, 0.05, 0.03)
    glPopMatrix()

    # SOL GÖZ
    glPushMatrix()
    glTranslatef(-0.15, 0.18, -1)
    glColor3f(0, 0, 0)
    RectangularPrism(0.05, 0.05, 0.03)
    glPopMatrix()

    # BURUN
    glPushMatrix()
    glTranslatef(0, -0.15, -1.08)
    glColor3f(0.77, 0.77, 0.77)
    RectangularPrism(0.165, 0.165, 0.165)
    glPopMatrix()

    # AĞIZ
    glPushMatrix()
    glTranslatef(0, -0.2, -1.25)
    glColor3f(0.7, 0, 0)
    RectangularPrism(0.12, 0.05, 0.03)
    glPopMatrix()

    # SOL ÖN AYAK
    glPushMatrix()
    glRotatef(human.solBacakAngle, 1, 0, 0)
    glTranslatef(-0.18, -1, -0.4)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SAĞ ÖN AYAK
    glPushMatrix()
    glRotatef(human.sagBacakAngle, 1, 0, 0)
    glTranslatef(0.18, -1, -0.4)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SOL ARKA AYAK
    glPushMatrix()
    glRotatef(human.solBacakAngle, 1, 0, 0)
    glTranslatef(-0.18, -1, 0.8)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SAĞ ARKA AYAK
    glPushMatrix()
    glRotatef(human.sagBacakAngle, 1, 0, 0)
    glTranslatef(0.18, -1, 0.8)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # KUYRUK
    glPushMatrix()
    glTranslatef(0.045, -0.25, 1.3)
    glRotatef(45,1,0,0)
    glColor3f(0, 0, 0.3)
    RectangularPrism(0.12, 0.12, 0.6)
    glPopMatrix()

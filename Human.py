import pygame
from OpenGL.GLUT import *
from RectangularPrism import *

''' EKLENECEK '''
def is_Inside(x_value,z_value,human,camera,boxList,plusBox):
    if z_value > plusBox.z1 and z_value < plusBox.z2 and x_value > plusBox.x1 and x_value < plusBox.x2:
        plusBox.hide = False
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('assets/sounds/eat.mp3'))
        if(human.carpismaSayisi>10):
            human.carpismaSayisi -= 10
    for i in range(0,6):
        if z_value > boxList[i][2] and z_value < boxList[i][3] and x_value > boxList[i][0] and x_value < boxList[i][1]:
            human.engelVar =True
            human.carpismaSayisi +=1
    if(x_value>300):
        human.engelVar = True
        human.carpismaSayisi += 1
    if(z_value>300):
        human.engelVar = True
        human.carpismaSayisi += 1
    if (x_value < -300):
        human.engelVar = True
        human.carpismaSayisi += 1
    if (z_value < -300):
        human.engelVar = True
        human.carpismaSayisi += 1

''' EKLENECEK '''
def getHuman(camera,human,boxList,plusBox):
    HumanKosmaDurum(human)
    glPushMatrix()
    glTranslatef(0, 5, 0)
    #glTranslatef(camera.xPos + 15 * camera.directionX, human.humanSpace, (camera.zPos) + 15 * camera.directionZ)
    is_Inside(camera.xPos + 15 * camera.directionX, (camera.zPos) + 15 * camera.directionZ,human,camera,boxList,plusBox)
    if(human.engelVar==False):
        human.topxPos =camera.xPos + 15 * camera.directionX
        human.topzPos = (camera.zPos) + 15 * camera.directionZ
    glTranslatef(human.topxPos, human.humanSpace, human.topzPos)
    HumanSpace(human)
    glRotatef(-57.5 * (camera.angleY), 0, 1, 0)
    drawHuman(human)
    glPopMatrix()

''' EKLENECEK '''
def HumanKosmaDurum(human):
    if(human.hareket == True and human.humanSpaceControl!=True and human.engelVar == False):
        if (human.durum == 0):
            human.sagBacakAngle += 5
            human.solBacakAngle -= 5
            if (human.sagBacakAngle > 40):
                human.durum = 1
        elif (human.durum == 1):
            human.sagBacakAngle -= 5
            human.solBacakAngle += 5
            if (human.sagBacakAngle < -40):
                human.durum = 0
    else :
        human.sagBacakAngle = 0
        human.solBacakAngle = 0
def HumanSpace(human):
    if (human.humanSpaceControl):
        human.humanSpace += 0.5
        if (human.humanSpace >= 4):
            human.humanSpaceControl = False
    elif (human.humanSpace > 0):
        human.humanSpace -= 0.5
        if (human.humanSpace < 0):
            human.humanSpace = 0

''' Dikdörtgenler prizmaları kullanılarak bir İnsan oluşturan fonksiyon '''
def drawHuman(human):
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
    glRotatef(human.solBacakAngle, 1, 0, 0)
    glColor3f(0.23, 0.78, 1)
    glTranslatef(0.18, -0.65, 0)
    RectangularPrism(0.15, 0.8, 0.25)
    glPopMatrix()

    # SOL KOL
    glPushMatrix()
    glTranslatef(-0.5, -0.65, 0)
    glColor3f(0.23, 0.45, 0.36)
    glutSolidSphere(0.22, 20, 20)
    glRotatef(human.sagBacakAngle, 1, 0, 0)
    glColor3f(0.88, 0.88, 0.12)
    glTranslatef(-0.18, -0.65, 0)
    RectangularPrism(0.15, 0.8, 0.25)
    glPopMatrix()

    # SAĞ BACAK
    glPushMatrix()
    glTranslatef(0.3, -2.6, 0)
    glColor3f(0.44, 0.77, 0.66)
    glutSolidSphere(0.22, 20, 20)
    glRotatef(human.sagBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(0, -0.95,0)
    RectangularPrism(0.15, 1, 0.25)
    #SAG AYAK
    glPushMatrix()
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(0.0, -1.1, -0.165)
    RectangularPrism(0.15, 0.1, 0.4)
    glPopMatrix()
    glPopMatrix()

    # SOL BACAK

    glPushMatrix()
    glTranslatef(-0.3, -2.6, 0)
    glColor3f(0.44, 0.77, 0.66)
    glutSolidSphere(0.22, 20, 20)
    glRotatef(human.solBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(0, -0.95, 0)
    RectangularPrism(0.15, 1, 0.25)
    #SOL AYAK
    glPushMatrix()
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(0.0, -1.1, -0.165)
    RectangularPrism(0.15, 0.1, 0.4)
    glPopMatrix()
    glPopMatrix()



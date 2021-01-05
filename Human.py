import pygame
from OpenGL.GLUT import *
from RectangularPrism import *

''' İnsanın engellerin içine girmesini ve sahne sınırlarının dışına çıkmasını
    kontrol edip engelleyen fonksiyondur
    GiftBox toplama kontrolünü de yapar'''
def is_Inside(x_value,z_value,human,boxList,plusBox):
    if z_value > plusBox.z1 and z_value < plusBox.z2 and x_value > plusBox.x1 and x_value < plusBox.x2:
        plusBox.hide = False
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('assets/sounds/eat.mp3'))
        if(human.carpismaSayisi>-30):
            human.carpismaSayisi -= 20
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

''' İnsan oluşturma çağrısı burada yapılır
    Zıplama ve hareket durumlarını kontrol eder ve değişiklik uygulanır
'''
def getHuman(control, human, boxList, plusBox):
    HumanKosmaDurum(human)
    glPushMatrix()
    glTranslatef(0, 5, 0)
    is_Inside(control.xPos + 15 * control.directionX, (control.zPos) + 15 * control.directionZ, human, boxList, plusBox)
    if(human.engelVar==False):
        human.topxPos = control.xPos + 15 * control.directionX
        human.topzPos = (control.zPos) + 15 * control.directionZ
    glTranslatef(human.topxPos, human.humanSpace, human.topzPos)
    HumanSpace(human)
    glRotatef(-57.5 * (control.angleY), 0, 1, 0)
    drawHuman(human)
    glPopMatrix()

''' İnsanın koşma durumunu kontrol eder '''
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
    glColor3f(0.011, 0.027, 0.117)
    RectangularPrism(0.3, 0.3, 0.3)
    glPopMatrix()

    # BOYUN
    glPushMatrix()
    glTranslatef(0, -0.4, 0)
    glColor3f(0.79, 0.6, 0.494)
    RectangularPrism(0.1, 0.1, 0.1)
    glPopMatrix()

    # GÖVDE
    glPushMatrix()
    glTranslatef(0, -1.5, 0)
    glColor3f(0.521, 0.094, 0.164)
    RectangularPrism(0.5, 1, 0.25)
    glPopMatrix()

    # SAĞ KOL
    glPushMatrix()
    glTranslatef(0.5, -0.65, 0)
    glColor3f(0.698, 0.49, 0.384)
    glutSolidSphere(0.22,20,20)
    glRotatef(human.solBacakAngle, 1, 0, 0)
    glColor3f(0.46, 0.286, 0.211)
    glTranslatef(0.18, -0.65, 0)
    RectangularPrism(0.15, 0.8, 0.25)
    glPopMatrix()

    # SOL KOL
    glPushMatrix()
    glTranslatef(-0.5, -0.65, 0)
    glColor3f(0.698, 0.49, 0.384)
    glutSolidSphere(0.22, 20, 20)
    glRotatef(human.sagBacakAngle, 1, 0, 0)
    glColor3f(0.46, 0.286, 0.211)
    glTranslatef(-0.18, -0.65, 0)
    RectangularPrism(0.15, 0.8, 0.25)
    glPopMatrix()

    # SAĞ BACAK
    glPushMatrix()
    glTranslatef(0.3, -2.6, 0)
    glColor3f(0.698, 0.49, 0.384)
    glutSolidSphere(0.22, 20, 20)
    glRotatef(human.sagBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(0, -0.95,0)
    RectangularPrism(0.15, 1, 0.25)
    #SAG AYAK
    glPushMatrix()
    glColor3f(1,1,1)
    glTranslatef(0.0, -1.1, -0.165)
    RectangularPrism(0.15, 0.1, 0.4)
    glPopMatrix()
    glPopMatrix()

    # SOL BACAK

    glPushMatrix()
    glTranslatef(-0.3, -2.6, 0)
    glColor3f(0.698, 0.49, 0.384)
    glutSolidSphere(0.22, 20, 20)
    glRotatef(human.solBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(0, -0.95, 0)
    RectangularPrism(0.15, 1, 0.25)
    #SOL AYAK
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(0.0, -1.1, -0.165)
    RectangularPrism(0.15, 0.1, 0.4)
    glPopMatrix()
    glPopMatrix()

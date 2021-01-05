import random
import pygame
from RectangularPrism import *
''' Köpeği oluşturma işlevi burada çağırılır
    İnsanın oyundaki çarpma ve hareketine göre köğein hızını ayarlar
'''
def getDog(control, dog, human, game):
    dog.hareket =True
    rand = random.randint(0, 1)
    if((dog.hiz>7 and dog.hiz<7.5)or(dog.hiz>8.5 and dog.hiz<9)or(dog.hiz>10 and dog.hiz<10.5)or(dog.hiz>11.5 and dog.hiz<12) or dog.hiz>13):
        if pygame.mixer.Channel(4).get_busy():
            pass
        else:
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('assets/sounds/dog-sound.mp3'))
    if dog.hiz >= 13.5 and dog.hiz < 14.1 and game.end != True:
        game.end = True
        game.win = False
    elif (human.carpismaSayisi > 100):
        dog.hiz += 0.5
    elif (human.carpismaSayisi > 80):
        dog.hiz += 0.1
    elif (human.carpismaSayisi > 50):
        dog.hiz += 0.05
    elif (human.carpismaSayisi > 20):
        dog.hiz += 0.005

    glPushMatrix()
    glTranslatef(0, 1, 0)
    glTranslatef(control.xPos + dog.hiz * control.directionX, 0, (control.zPos) + dog.hiz * control.directionZ)
    glRotatef(-57.5 * (control.angleY), 0, 1, 0)
    DogKosmaDurum(dog)
    drawDog(dog)
    glPopMatrix()
''' Köpeğin hareketini kontrol eder'''
def DogKosmaDurum(dog):
    if(dog.hareket == True):
        if (dog.durum == 0):
            dog.sagBacakAngle += dog.hiz
            dog.solBacakAngle -= dog.hiz
            dog.kuyruk +=dog.hiz
            if (dog.sagBacakAngle > 40):
                dog.durum = 1
        elif (dog.durum == 1):
            dog.sagBacakAngle -= dog.hiz
            dog.solBacakAngle += dog.hiz
            dog.kuyruk -= dog.hiz
            if (dog.sagBacakAngle < -40):
                dog.durum = 0
    else :
        dog.kuyruk = 0
        dog.sagBacakAngle = 0
        dog.solBacakAngle = 0

''' Dikdörtgenler prizmaları kullanılarak bir köpek oluşturan fonksiyon '''
def drawDog(dog):
    # GÖVDE
    glPushMatrix()
    glColor3f(0.85, 0.85, 85)
    RectangularPrism(0.312, 0.312, 1)
    glPopMatrix()

    # KAFA
    glPushMatrix()
    glTranslatef(0, 0, -0.4)
    glColor3f(0.694, 0.654, 0.65)
    RectangularPrism(0.4, 0.4, 0.4)
    glPopMatrix()

    # SAĞ KULAK
    glPushMatrix()
    glTranslatef(0.2, 0.4, -0.9)
    glColor3f(0.823, 0.823, 0.82)
    RectangularPrism(0.1, 0.1, 0.03)
    glPopMatrix()

    # SOL KULAK
    glPushMatrix()
    glTranslatef(-0.2, 0.4, -0.9)
    glColor3f(0.823, 0.823, 0.82)
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
    glTranslatef(-0.18, -0.7, -0.4)
    glRotatef(dog.solBacakAngle, 1, 0, 0)
    glColor3f(0.929, 0.929, 0.874)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SAĞ ÖN AYAK
    glPushMatrix()
    glTranslatef(0.18, -0.7, -0.4)
    glRotatef(dog.sagBacakAngle, 1, 0, 0)
    glColor3f(0.929, 0.929, 0.874)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SOL ARKA AYAK
    glPushMatrix()
    glTranslatef(-0.18, -0.7, 0.8)
    glRotatef(dog.sagBacakAngle, 1, 0, 0)
    glColor3f(0.929, 0.929, 0.874)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SAĞ ARKA AYAK
    glPushMatrix()
    glTranslatef(0.18, -0.7, 0.8)
    glRotatef(dog.solBacakAngle, 1, 0, 0)
    glColor3f(0.929, 0.929, 0.874)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # KUYRUK
    glRotatef(dog.kuyruk, 0, 0, 1)
    glPushMatrix()
    glTranslatef(0.045, -0.25, 1.3)
    glRotatef(45,1,0,0)
    glColor3f(1,1,1)
    RectangularPrism(0.12, 0.12, 0.6)
    glPopMatrix()

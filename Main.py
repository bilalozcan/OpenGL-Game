from OpenGL.GLU import *
import OpenGL.GLUT as glut
from Box import *
from Human import *
from Dog import *
import math as m
from MapTexture import *
import pygame
''' 3D Bir sahneden oluşan oyundur. Bir insan ve köpek vardır.
    İnsanın köpekten kaçması gerekmektedir. Sahnede engeller ve hediye kutusu vardır.
    İnsan engellere ve alan sınırlarına çarptıkça köpek insana yaklaşır.
    İnsan Hediye Kutusu toplayınca köpeğin hızı azalır.
    Köpek insanı yakaladığında oyun biter.
    100 Puana ulaşınca oyun kazanılır.
    P tuşuna basınca duraklatma menüsü açılır.
'''
''' Ekran Boyutu için değişkenler'''
windowX = 1920
windowY = 1080

''' Ses efektleri için başlangıçta gerekli hazırlıkların yapılması
    Engeller için rastgele koordinat atamalarının yapılması'''
def init():
    global boxCordinate # Engeller için rastgele koordinatların tutulduğu liste
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/background-sounds.mp3')) #Arka Plan Ses Efekti
    pygame.mixer.Channel(0).set_volume(0.04)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/walk-human.mp3')) #Yürüme Ses Efekti
    pygame.mixer.Channel(1).set_volume(0.8)
    pygame.mixer.Channel(1).stop()
    pygame.mixer.Channel(4).play(pygame.mixer.Sound('assets/sounds/dog-sound.mp3')) #Köpek Ses Efekti
    pygame.mixer.Channel(4).set_volume(0.5)
    pygame.mixer.Channel(4).stop()
    for i in range(0,6):
        boxCordinate.append([random.randint(-300,300),random.randint(-300,300)])
''' Oyun ve ses durumunun tutulduğu class '''
class Game():
    score = 0
    end = False
    pause = False
    ses = False
    win = False
''' Hediye Kutusu durumunun tutulduğu class '''
class PlusBox():
    hide = False
    plusBoxCordinateX = random.randint(-300,300)
    plusBoxCordinateY = random.randint(-300, 300)
    x1 = 0
    x2 =0
    z1 =0
    z2 =0
    def NewCordinate(self):
        self.plusBoxCordinateX = random.randint(-100, 100)
        self.plusBoxCordinateY = random.randint(-100, 100)
''' Tuşa basılı tutma durumlarını tutan class '''
class Tus():
    keyW = False
    keyA = False
    keyD = False

''' İnsan modeli için gerekli parametrelerin (zıplama/hareket/engele çarpma gibi) tutulduğu class '''
class Human():
    sagBacakAngle = 0 #Sağ Bacak dönme açısı
    solBacakAngle = 0 #Sol Bacak dönme açısı
    durum = 0 # Bacak ileri geri hareket durumu
    humanSpace = 0 # Zıplama
    humanSpaceControl = False # Zıplama Durumu
    topxPos = 0.0 # İnsanın anlık X konumu
    topzPos = 1.0 # İnsanın anlık Y konumu
    hareket = False
    engelVar = False
    carpismaSayisi =0
    backStep =0 #Geri adım atma sayısı

''' Köpek modeli için gerekli parametrelerin (hareket/hız gibi) tutulduğu class '''
class Dog():
    sagBacakAngle = 0 # Sağ Bacak dönme açısı
    solBacakAngle = 0 # Sol Bacak dönme açısı
    kuyruk = 0 # Kuyruk dönme açısı
    durum = 0
    hiz = 6.0
    hareket = False

''' Genel Konum kontrol sınıfıdır. Kameranın, insanın, farenin konumu, görüş açısı, dönme açısı gibi değerler buraya bağlıdır '''
class Control():
    angleY = 0.05
    directionX = 0.0 # Genel Dönme Açısı (İnsan/Köpek/Kamera)
    directionY = 0  # Genel Dönme Açısı (İnsan/Köpek/Kamera)
    directionZ = -1.0 # Genel Dönme Açısı (İnsan/Köpek/Kamera)
    directionXmouse = 0.0 # Mouse ile Dönme Açısı
    directionYmouse = 0.0 # Mouse ile Dönme Açısı
    directionZmouse = 0.0 # Mouse ile Dönme Açısı
    xPos = 0.0 # Kameranın X Konumu
    zPos = -5.0 # Kameranın Z Konumu
    yPos = 8.0 # Kameranın Y Konumu
    zoom = 0.2 #
    mouse_x = 0 # Mouse Anlık X Konumu
    mouse_y = 0 # Mouse Anlık Y Konumu
    mouse_left = 1 # Mouse Tıklandı mı
    mouseTikX =0 # Mouse Tıklama X Konumu
    mouseTikY =0 # Mouse Tıklama Y Konumu

''' Oyun ile ilgili temel objelerin oluşturulması '''
game = Game()
plusBox = PlusBox()
tus = Tus()
control = Control()
human = Human()
dog = Dog()
stopTime = 2.0
boxCordinate = [] # Engeller için rastgele koordinatların tutulduğu liste
boxList = []

''' Oyuna yeniden başlama durumunda insan/köpek/kamera konumu gibi değerleri sıfırlayan fonksiyon '''
def restart():
    global game,plusBox,tus,control,human,dog,stopTime
    game.score = 0
    plusBox = PlusBox()
    tus = Tus()
    control = Control()
    human = Human()
    dog = Dog()
    stopTime = 2.0

''' Oyun ekranının durumunu kontrol etmek için gerekli değişkenler '''
MAIN_MENU_SCREEN = 0 # Ana Menü Ekranı
GAME_SCREEN = 1 # Oyun Ekranı
PAUSE_MENU_SCREEN = 2 # Duraklatma Ekranı
END_SCREEN = 3 # Bitiş Ekranı
CurrentScreen = MAIN_MENU_SCREEN # Geçerli ekran

''' Geçerli ekran değişimini kontrol edip değişimi yapan fonksiyon
    Duruma göre ses efektleri durdurulur '''
def changeScreen():
    global CurrentScreen
    if(game.end == True):
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(1).stop()
        pygame.mixer.Channel(2).stop()
        pygame.mixer.Channel(3).stop()
        pygame.mixer.Channel(4).stop()
        pygame.mixer.Channel(5).stop()
        CurrentScreen = END_SCREEN
    if CurrentScreen == END_SCREEN:
        return EndMenu()
    if CurrentScreen == MAIN_MENU_SCREEN:
        return MainMenu()
    elif CurrentScreen == GAME_SCREEN:
        return GameScreen()
    elif CurrentScreen == PAUSE_MENU_SCREEN:
        return PauseMenu()


''' Ana Menü Ekranını çalıştıran fonksiyon
    Texture ile Play butonu içerir '''

def MainMenu():
    pygame.mixer.Channel(0).pause()
    #glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(-5,-5,0)
    glActiveTexture(GL_TEXTURE0)
    LoadTextures("assets/main-menu-screen.png")
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex2f(0.0, 0.0)
    glTexCoord2f(0.0, 0.0), glVertex2f(0.0, 10.0)
    glTexCoord2f(1.0, 0.0), glVertex2f(10.0,10.0)
    glTexCoord2f(1.0, 1.0), glVertex2f(10.0, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glutSwapBuffers()

''' Duraklatma Menü Ekranını çalıştıran fonksiyon
    Texture ile Resume, Restart ve Mute/Unmute butonları içerir '''
def PauseMenu():
    pygame.mixer.Channel(0).pause()
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)
    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(-5, -5, 0)
    glActiveTexture(GL_TEXTURE0)
    if(game.ses==False):
        LoadTextures("assets/pause-menu-screen.png")
    else:
        LoadTextures("assets/pause-menu-mute-screen.png")
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex2f(0.0, 0.0)
    glTexCoord2f(0.0, 0.0), glVertex2f(0.0, 10.0)
    glTexCoord2f(1.0, 0.0), glVertex2f(10.0, 10.0)
    glTexCoord2f(1.0, 1.0), glVertex2f(10.0, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glutSwapBuffers()

''' Bitiş Ekranını çalıştıran fonksiyon
    Texture ile Restart butonu içerir '''
def EndMenu():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)
    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(-5, -5, 0)
    glActiveTexture(GL_TEXTURE0)
    if game.win == False:
        LoadTextures("assets/gameover-screen.png")
    else:
        LoadTextures("assets/win-screen.png")
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex2f(0.0, 0.0)
    glTexCoord2f(0.0, 0.0), glVertex2f(0.0, 10.0)
    glTexCoord2f(1.0, 0.0), glVertex2f(10.0, 10.0)
    glTexCoord2f(1.0, 1.0), glVertex2f(10.0, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glutSwapBuffers()

''' Verilen stringi ekrana text olarak yazdıran fonksiyon '''
def textWrite(string):
    glRasterPos3f(0, 0, 0)
    for i in string:
        glutBitmapCharacter(glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(i))

''' Oyun Ekranını çalıştıran fonksiyon
    3D bir sahne, köpek, insan, engeller içerir '''
def GameScreen():
    global control,dog,human,boxCordinate, boxList,plusBox
    pygame.mixer.Channel(0).unpause() # Arkaplan sesinin resume edilmesi
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 8.0 / 4.0, 1, 600) # Perspektif bakış açısının ayarlanması
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Kameranın pozisyonu ve bakış açısının ayarlanması
    gluLookAt(control.xPos, control.yPos, control.zPos, control.xPos + control.directionX + control.directionXmouse,
              control.yPos - control.zoom + control.directionY - 0.18 + control.directionYmouse,
              control.zPos + control.directionZ + control.directionZmouse, 0, 1, 0)
    mapTexture(300, 100, 300) # 3D sahnenin zemin, gökyüzü ve etraf texture'larının yapılması
    getDog(control, dog, human, game) #Verilen parametreleri kullanarak sahnede köpek oluşturur
    keyControl() # İki tuş basma kontrolünü sağlar
    plusBox.x1, plusBox.x2, plusBox.z1, plusBox.z2 = getBox(2, 2, 2, plusBox.plusBoxCordinateX, 1,
                                                            plusBox.plusBoxCordinateY,"assets/giftbox.png" )
    if plusBox.hide == False:
        plusBox.hide = True
        game.score += 10
        if game.score >= 100:
            game.end = True
            game.win = True
        plusBox.NewCordinate()
    # Sahnede 6 tane engel oluşturulması
    for i in range(0,6):
        boxList.append(getBox(5,5,5,boxCordinate[i][0],2.5,boxCordinate[i][1],"assets/box.png"))
    getHuman(control, human, boxList, plusBox)
    if(tus.keyW == False):
        dog.hiz += 0.01
    glPushMatrix()
    glColor3f(1, 0,0)
    stra = "KÖPEK KALAN MESAFE:{:.3}".format(13.5 - dog.hiz)
    glTranslatef(control.xPos + 10 * control.directionX, 9.1, (control.zPos) + 10 * control.directionZ)
    textWrite(stra)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0,0)
    strb = "GERI ADIM SAYISI:{:.2}".format(str(20-human.backStep))
    glTranslatef(control.xPos + 10 * control.directionX, 8.8, (control.zPos) + 10 * control.directionZ)
    textWrite(strb)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0, 0)
    strb = "SCORE:{:.3}".format(str(game.score - 10))
    glTranslatef(control.xPos + 10 * control.directionX, 9.4, (control.zPos) + 10 * control.directionZ)
    textWrite(strb)
    glPopMatrix()

    glutSwapBuffers()

''' İki Tuşa aynı anda basılma işlemini sağlayan fonksiyondur
    İki tuşa basarak iki hareket işlevinin beraber yapılmasını sağlar
'''
def keyControl():
    global control,human,tus
    ''' Engel varsa insan hareket edemez
        Engel yoksa 2 tuş ile hareket buradan sağlanır'''
    if(human.engelVar == False):
        if(tus.keyW==True and tus.keyA):
            pass
        if (tus.keyW == True and tus.keyD):
            pass
        elif tus.keyW == True:
            if pygame.mixer.Channel(1).get_busy():
                pass
            else:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/walk-human.mp3'))
            control.xPos += control.directionX * 1.5
            control.zPos += control.directionZ * 1.5
            control.yPos += control.directionY * 1.5
        elif(tus.keyA):
            pass
        elif(tus.keyD):
            pass

''' Tuşa basılı tutma işlevini kontrol edip
    Ona göre insana hareket kazandıran fonksiyon 
    Tuştan basılı tutma bırakıldıgı an durumu false olur
'''
def keyUp(*args):
    global  tus
    if args[0] == b"a":
        tus.keyA = False
    elif args[0] == b"d":
        tus.keyD = False
    elif args[0] == b"w":
        pygame.mixer.Channel(1).stop()
        if (human.engelVar == True):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/sounds/collision.mp3'))
        human.hareket = False
        tus.keyW = False
    elif args[0] == b" ":
        pass

    glutPostRedisplay()
''' İnsan ve kameranın klavye ile kontrolünü sağlayan fonksiyon '''
def keyPressed(*args):
    global control, human,tus,CurrentScreen
    if args[0] == b'\r':
        CurrentScreen = GAME_SCREEN
    elif args[0] == b"p":
        CurrentScreen = PAUSE_MENU_SCREEN
    if(CurrentScreen == GAME_SCREEN):
        if args[0] == b"\x1b":
            glutDestroyWindow(b"Beni Yakala 3D")
        if args[0] == b"a":
            tus.keyA =True
        elif args[0] == b"d":
            tus.keyD = True
        elif args[0] == b"w":
            human.hareket = True
            tus.keyW = True
        elif args[0] == b"s" :
            if(human.backStep<20):
                human.backStep +=1
                human.engelVar = False
                control.xPos -= control.directionX
                control.zPos -= control.directionZ
                control.yPos -= control.directionY

        elif args[0] == b" ":
            if (human.backStep > 0):
                human.backStep -= 1
            if (human.humanSpace == 0):
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('assets/sounds/jump.mp3'))
                human.humanSpaceControl = True

    glutPostRedisplay()

''' Menü Ekranlarında buton tıklama işlevlerini kontrol edip
    gerekli işevleri -Gerekli Ekran Geçişlerini- yapmasını sağlayan fonksiyon 
'''
def mouse(button, state, x, y):
    global control,CurrentScreen
    if GLUT_LEFT_BUTTON == 0:
        if GLUT_DOWN == 0:
            control.mouse_left = 1
            if(CurrentScreen == MAIN_MENU_SCREEN):
                if(x>885 and x<1060 and y<530 and y>400):
                    CurrentScreen = GAME_SCREEN
            if(CurrentScreen == PAUSE_MENU_SCREEN):
                if(x>485 and x<720 and y<530 and y>375):
                    restart()
                    game.end = False
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/background-sounds.mp3'))
                    pygame.mixer.Channel(0).set_volume(0.04)
                    CurrentScreen = GAME_SCREEN
                if (x > 860 and x < 1100 and y < 530 and y > 375):
                    CurrentScreen = GAME_SCREEN
                if (x > 1250 and x < 1380 and y < 530 and y > 375):
                    game.ses = True
                    for i in range(5):
                        pygame.mixer.Channel(i).set_volume(0)
                if (x > 1385 and x < 1490 and y < 530 and y > 375):
                    game.ses = False
                    pygame.mixer.Channel(0).set_volume(0.04)
                    for i in range(1,5):
                        pygame.mixer.Channel(i).set_volume(0.8)
            if (CurrentScreen == END_SCREEN):
                if (x > 820 and x < 1060 and y < 510 and y > 360):

                    restart()
                    game.end = False
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/background-sounds.mp3'))
                    pygame.mixer.Channel(0).set_volume(0.04)
                    CurrentScreen = GAME_SCREEN

        if GLUT_UP == 0:
            control.mouse_left = 0

''' Fare hareketine göre kamera açısını ayarlayan fonksiyondur '''
def mouseMotion(x, y):
    global control,human
    if(human.engelVar == False and CurrentScreen == GAME_SCREEN):
        '''İlk başlangıç inin mouse'un geçmiş bir konumu olmadığı için ekranın sağına gidilirse kamera açısı sağa
            sola gidilirse kamera açısı sola döner.
            Daha sonraki durumlarda mouse'un önceki konumuna göre sola gidilirse açı sola
            sağa gidilirse açı sağa döner'''
        if (control.mouse_x == 0): #Mouse'un başlangıç değeri olmadığı için ortayı baz alır
            control.mouse_x = x
            if (x > windowX / 2):
                control.angleY += 0.04
                control.directionX = m.sin(control.angleY)
                control.directionZ = -m.cos(control.angleY)
            else:
                control.angleY -= 0.04
                control.directionX = m.sin(control.angleY)
                control.directionZ = -m.cos(control.angleY)
        if (x > 1800):
            control.mouse_x = x
            control.angleY += 0.09
            control.directionX = m.sin(control.angleY)
            control.directionZ = -m.cos(control.angleY)
        if (x < 100):
            control.mouse_x = x
            control.angleY -= 0.09
            control.directionX = m.sin(control.angleY)
            control.directionZ = -m.cos(control.angleY)
        else:
            if (x > control.mouse_x):
                control.angleY += 0.04
                control.directionX = m.sin(control.angleY)
                control.directionZ = -m.cos(control.angleY)
            else:
                control.angleY -= 0.04
                control.directionX = m.sin(control.angleY)
                control.directionZ = -m.cos(control.angleY)
            control.mouse_x = x

''' Mouse tekerleği ile kameranın aşağı yukarı hareket etmesini sağlayan fonksiyon '''
def MouseWheel(*args):
    global control
    if args[1] == -1:
        if (control.yPos > 3):
            control.yPos -= 0.1
    elif args[1] == 1:
        if (control.yPos < 9):
            control.yPos += 0.1
    else:
        pass
    glutPostRedisplay()

''' Glut ile gerekli ekran/pencere/keyboard/mouse gibi işlemlerin yapıldı ana fonksiyon '''
def main():
    init()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(windowX, windowY)
    glutInitWindowPosition(0, 0)
    glutIdleFunc(changeScreen)
    glutCreateWindow(b"Beni Yakala 3D")
    glutDisplayFunc(changeScreen)
    glutIdleFunc(changeScreen)
    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyUp)
    glutMouseWheelFunc(MouseWheel)
    glutMouseFunc(mouse)
    glutPassiveMotionFunc(mouseMotion)
    glutMainLoop()
    glEnable(GL_DEPTH_TEST)

main()
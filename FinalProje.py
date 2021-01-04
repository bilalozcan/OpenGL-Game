from OpenGL.GLU import *

from Box import *
from Human import *
from Dog import *
import math as m
from MapTexture import *
import pygame
windowX = 1920
windowY = 1080
stopTime = 2.0
boxCordinate = []
boxList = []
def init():
    global boxCordinate
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/background-sounds.mp3'))
    pygame.mixer.Channel(0).set_volume(0.05)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/walk-human.mp3'))
    pygame.mixer.Channel(1).set_volume(0.8)
    pygame.mixer.Channel(1).stop()

    for i in range(0,6):
        boxCordinate.append([random.randint(-300,300),random.randint(-300,300)])

class Tus():
    keyW = False
    keyA = False
    keyD = False
class Human():
    sagBacakAngle = 0
    solBacakAngle = 0
    durum = 0
    humanSpace = 0
    humanSpaceControl = False
    angleY = 0.05
    topxPos = 0.0
    topzPos = 1.0
    directionX = 0.0
    directionZ = -1.0
    hareket = False
    engelVar = False
    carpismaSayisi =0


class Dog():
    sagBacakAngle = 0
    solBacakAngle = 0
    kuyruk = 0
    durum = 0
    hiz = 6.0
    hareket = False

class Camera():
    angleY = 0.05
    directionX = 0.0
    directionZ = -1.0
    directionXmouse = 0.0
    directionZmouse = 0.0
    directionYmouse = 0.0
    directionY = 0
    xPos = 0.0
    zPos = -5.0
    yPos = 8.0
    zoom = 0.2
    mouse_x = 0
    mouse_y = 0
    mouse_left = 1


tus = Tus()
camera = Camera()
human = Human()
dog = Dog()
MAIN_MENU_SCREEN = 0
GAME_SCREEN = 1
PAUSE_MENU_SCREEN = 2
CurrentScreen = MAIN_MENU_SCREEN
def changeScreen():
    global CurrentScreen
    if CurrentScreen == MAIN_MENU_SCREEN:
        return MainMenu()
    elif CurrentScreen == GAME_SCREEN:
        return display()
    elif CurrentScreen == PAUSE_MENU_SCREEN:
        return PauseMenu()

def MainMenu():
    pygame.mixer.Channel(0).pause()
    glClearColor(0.53, 0.88, 0.54, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glColor(1, 1, 0)
    glutSolidSphere(1, 20, 20)
    glPopMatrix()
    glutSwapBuffers()

def PauseMenu():
    pygame.mixer.Channel(0).pause()
    glClearColor(0.22, 0.44, 0.66, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glColor(1, 1, 0)
    glutSolidSphere(1, 20, 20)
    glPopMatrix()
    glutSwapBuffers()


def display():
    global camera,dog,human,boxCordinate, boxList
    pygame.mixer.Channel(0).unpause()
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 8.0 / 4.0, 1, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera.xPos, camera.yPos, camera.zPos, camera.xPos + camera.directionX + camera.directionXmouse,
              camera.yPos - camera.zoom + camera.directionY-0.18 + camera.directionYmouse,
              camera.zPos + camera.directionZ + camera.directionZmouse, 0, 1, 0)
    mapTexture(300, 100, 300)
    getDog(camera,dog,human)
    keyControl()
    for i in range(0,6):
        boxList.append(getBox(5,5,5,boxCordinate[i][0],2.5,boxCordinate[i][1]))
    getHuman(camera, human, boxList)
    glutSwapBuffers()

def keyControl():
    global camera,human,tus
    if(human.engelVar == False):
        if tus.keyW == True:
            if pygame.mixer.Channel(1).get_busy():
                pass
            else:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/walk-human.mp3'))
            camera.xPos += camera.directionX
            camera.zPos += camera.directionZ
            camera.yPos += camera.directionY
        elif(tus.keyA):
            human.angleY -= 0.1
        elif(tus.keyD):
            human.angleY +=0.1
def keyUp(*args):
    global  tus
    if args[0] == b"a":
        tus.keyA = False
    elif args[0] == b"d":
        tus.keyD = False
    elif args[0] == b"w":
        pygame.mixer.Channel(1).stop()
        if (human.engelVar == True):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/sounds/carpma.mp3'))
        human.hareket = False
        tus.keyW = False
    elif args[0] == b" ":
        pass

    glutPostRedisplay()

def keyPressed(*args):
    global camera, human,tus,CurrentScreen
    if args[0] == b'\r':
        CurrentScreen = GAME_SCREEN
    elif args[0] == b"p":
        CurrentScreen = PAUSE_MENU_SCREEN

    if args[0] == b"\x1b":
        glutDestroyWindow(b"Followww")
    if args[0] == b"a":
        tus.keyA =True
    elif args[0] == b"d":
        tus.keyD = True
    elif args[0] == b"w":
        human.hareket = True
        tus.keyW = True
    elif args[0] == b"s":
        human.engelVar = False
        camera.xPos -= camera.directionX
        camera.zPos -= camera.directionZ
        camera.yPos -= camera.directionY

    elif args[0] == b" ":
        if (human.humanSpace == 0):
            human.humanSpaceControl = True

    glutPostRedisplay()

def mouse(button, state, x, y):
    global camera
    if GLUT_LEFT_BUTTON == 0:
        if GLUT_DOWN == 0:
            camera.mouse_left = 1
        if GLUT_UP == 0:
            camera.mouse_left = 0


def mouseMotion(x, y):
    global camera,human
    if(human.engelVar == False):
        if (camera.mouse_x == 0):
            camera.mouse_x = x
            if (x > windowX / 2):
                camera.angleY += 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
            else:
                camera.angleY -= 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
        if (x > 1800):
            camera.mouse_x = x
            camera.angleY += 0.1
            camera.directionX = m.sin(camera.angleY)
            camera.directionZ = -m.cos(camera.angleY)
        if (x < 100):
            camera.mouse_x = x
            camera.angleY -= 0.1
            camera.directionX = m.sin(camera.angleY)
            camera.directionZ = -m.cos(camera.angleY)
        else:
            if (x > camera.mouse_x):
                camera.angleY += 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
            else:
                camera.angleY -= 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
            camera.mouse_x = x


def MouseWheel(*args):
    global camera
    if args[1] == -1:
        if (camera.yPos > 3):
            camera.yPos -= 0.1
    elif args[1] == 1:
        if (camera.yPos < 9):
            camera.yPos += 0.1
    else:
        pass
    print(camera.yPos)
    glutPostRedisplay()

def main():
    init()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(windowX, windowY)
    glutInitWindowPosition(0, 0)
    glutIdleFunc(changeScreen)
    glutCreateWindow(b"Followw")
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

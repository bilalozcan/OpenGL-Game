
from OpenGL.GLU import *
from Human import *
from Dog import *
import math as m
from MapTexture import*
import pygame

windowX = 1920
windowY=1080

def init():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/background-sounds.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)



class Human():
    sagBacakAngle = 0
    solBacakAngle = 0
    durum =0
human = Human()
def KosmaDurum(control):
    global human
    if(control == True):
        if (human.durum == 0):
            human.sagBacakAngle += 5
            human.solBacakAngle -= 5
            if(human.sagBacakAngle > 40):
                human.durum = 1
        elif (human.durum == 1):
            human.sagBacakAngle -= 5
            human.solBacakAngle += 5
            if(human.sagBacakAngle < -40):
                human.durum = 0
    else:
        human.sagBacakAngle = 0
        human.solBacakAngle = 0
    print("sag bacak",human.sagBacakAngle)


class Camera():
    angleX = 0.0
    angleY = 0.05
    directionX = 0.0
    directionZ = -1.0
    directionXmouse = 0.0
    directionZmouse = 0.0
    directionYmouse = 0.0
    directionY = 0
    xPos = 0.0
    zPos = 1.0
    yPos = 6.0
    zoom =0.2
    mouse_x =0
    mouse_y = 0
    mouse_left=1
    humanSpace = 0
    humanSpaceControl = False
    x =0
    y= 0

camera =Camera()
def getHuman():
    global camera ,human
    glPushMatrix()
    glTranslatef(0, 5, 0)
    #glTranslatef(camera.xPos+8*camera.directionX, 0, (camera.zPos)+8*camera.directionZ)
    glTranslatef(camera.xPos+8*camera.directionX , camera.humanSpace, (camera.zPos)+8*camera.directionZ )
    HumanSpace()
    glRotatef(-57.5*(camera.angleY), 0,1, 0)
    drawHuman(human)
    glPopMatrix()

def getDog():
    global camera
    glPushMatrix()
    glTranslatef(5, 2, -7)
    drawDog()
    glPopMatrix()

def display():
    global camera
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
    gluLookAt(camera.xPos, camera.yPos, camera.zPos, camera.xPos + camera.directionX+camera.directionXmouse, camera.yPos-camera.zoom + camera.directionY+camera.directionYmouse,
              camera.zPos + camera.directionZ+camera.directionZmouse, 0, 1, 0)
    mapTexture(300,100,300)
    getHuman()
    getDog()
    glutSwapBuffers()

def keyPressed(*args):
    global camera,human
    gelenTus = args[0]
    fraction = 2
    if args[0] == b"a":
        pass
        #camera.angleY -= 0.05
        #camera.directionX = m.sin(camera.angleY)
        #camera.directionZ = -m.cos(camera.angleY)
    elif args[0] == b"d":
        pass
        #camera.angleY += 0.05
        #camera.directionX = m.sin(camera.angleY)
        #camera.directionZ = -m.cos(camera.angleY)
    elif args[0] == b"w":
        ses = pygame.mixer.Sound("assets/sounds/walk-minecraft.mp3")
        ses.play()
        KosmaDurum(True)
        camera.xPos += camera.directionX*fraction
        camera.zPos += camera.directionZ*fraction
        camera.yPos += camera.directionY*fraction
    elif args[0] == b"s":
        camera.xPos -= camera.directionX * fraction
        camera.zPos -= camera.directionZ * fraction
        camera.yPos -= camera.directionY * fraction
    elif args[0] == b" ":
        if(camera.humanSpace==0):
            camera.humanSpaceControl = True
    glutPostRedisplay()
def HumanSpace():
    global camera
    if(camera.humanSpaceControl ):
        camera.humanSpace += 0.1
        if(camera.humanSpace>=2):
            camera.humanSpaceControl = False
    elif(camera.humanSpace>0):
        camera.humanSpace -= 0.2
        if(camera.humanSpace<0):
            camera.humanSpace=0
def mouse(button,state,x,y):
    global camera
    if GLUT_LEFT_BUTTON == 0:
        if GLUT_DOWN == 0:
            camera.mouse_left = 1
        if GLUT_UP == 0:
            camera.mouse_left= 0

"""def mouseMotion(x,y):
    global camera
    if camera.mouse_left:
        camera.directionXmouse += (x - camera.mouse_x)*0.0005
        camera.directionYmouse += -(y - camera.mouse_y)*0.0005"""
def mouseMotion(x,y):
    global camera
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
    if(x>1800):
        camera.mouse_x = x
        camera.angleY += 0.1
        camera.directionX = m.sin(camera.angleY)
        camera.directionZ = -m.cos(camera.angleY)
    if(x<100):
        camera.mouse_x = x
        camera.angleY -= 0.1
        camera.directionX = m.sin(camera.angleY)
        camera.directionZ = -m.cos(camera.angleY)
    else:
        if(x>camera.mouse_x):
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
        if(camera.yPos>3):
            camera.yPos -= 0.1
    elif args[1] == 1:
        if(camera.yPos<9):
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
    glutIdleFunc(display)
    glutCreateWindow(b"Followw")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(keyPressed)
    glutMouseWheelFunc(MouseWheel)
    glutMouseFunc(mouse)
    glutPassiveMotionFunc(mouseMotion)
    glutMainLoop()
    glEnable(GL_DEPTH_TEST)


main()
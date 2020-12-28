
from OpenGL.GL import *
from OpenGL.GLU import *
from Human import *
from Dog import *
import math as m
from MapTexture import*

class Camera():
    angleX = 0.0
    angleY = 0.05
    directionX = 0.0
    directionZ = -1.0
    directionY = 0
    xPos = 0.0
    zPos = 1.0
    yPos = 6.0

camera =Camera()
def getHuman():
    global camera
    glPushMatrix()
    glTranslatef(0, 5, 0)
    #glTranslatef(camera.xPos+8*camera.directionX, 0, (camera.zPos)+8*camera.directionZ)
    glTranslatef(camera.xPos+8*camera.directionX , 0, (camera.zPos)+8*camera.directionZ )
    glRotatef(-57.5*(camera.angleY), 0,1, 0)
    drawHuman()
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
    gluLookAt(camera.xPos, camera.yPos, camera.zPos, camera.xPos + camera.directionX, camera.yPos-0.3 + camera.directionY,
              camera.zPos + camera.directionZ, 0, 1, 0)
    mapTexture(300,100,300)
    getHuman()
    getDog()
    glutSwapBuffers()

def keyPressed(*args):
    global camera
    fraction = 2
    if args[0] == b"a":
        camera.angleY -= 0.05
        camera.directionX = m.sin(camera.angleY)
        camera.directionZ = -m.cos(camera.angleY)
    elif args[0] == b"d":
        camera.angleY += 0.05
        camera.directionX = m.sin(camera.angleY)
        camera.directionZ = -m.cos(camera.angleY)
    elif args[0] == b"w":
        camera.xPos += camera.directionX*fraction
        camera.zPos += camera.directionZ*fraction
        camera.yPos += camera.directionY*fraction
    elif args[0] == b"s":
        camera.xPos -= camera.directionX * fraction
        camera.zPos -= camera.directionZ * fraction
        camera.yPos -= camera.directionY * fraction
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(1920, 1080)
    glutInitWindowPosition(0, 0)
    glutIdleFunc(display)
    glutCreateWindow(b"Followw")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()
    glEnable(GL_DEPTH_TEST)

main()
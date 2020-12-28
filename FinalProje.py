from PIL import Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Human import *
import math as m

class Camera():
    angleX = 0.0
    angleY = 0.05
    directionX = 0.0
    directionZ = -1.0
    directionY = 0
    xPos = 0.0
    zPos = 1.0
    yPos = 12.0

camera =Camera()
def LoadTextures(str):
    # global texture
    glActiveTexture(GL_TEXTURE0)
    image = Image.open(str)

    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGB")

    glShadeModel(GL_SMOOTH)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glEnable(GL_TEXTURE_2D)


def getHuman():
    global camera
    glPushMatrix()
    glTranslatef(0, 5, 0)
    #glTranslatef(camera.xPos+8*camera.directionX, 0, (camera.zPos)+8*camera.directionZ)
    glTranslatef(camera.xPos+8*camera.directionX , 0, (camera.zPos)+8*camera.directionZ )
    glRotatef(-57.5*(camera.angleY), 0,1, 0)
    drawHuman()
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
    gluPerspective(60.0, 8.0 / 4.0, 1, 250)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera.xPos, camera.yPos, camera.zPos, camera.xPos + camera.directionX, camera.yPos-0.2 + camera.directionY,
              camera.zPos + camera.directionZ, 0, 1, 0)
    glPushMatrix()
    glActiveTexture(GL_TEXTURE0)
    LoadTextures("grass.png")
    glColor3f(0.55, 0.92, 0.49)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0), glVertex3f(-80.0, 0.0, -80.0)
    glTexCoord2f(0.0, 1.0), glVertex3f(-80.0, 0.0, 80.0)
    glTexCoord2f(1.0, 1.0), glVertex3f(80.0, 0.0, 80.0)
    glTexCoord2f(1.0, 0.0), glVertex3f(80.0, 0.0, -80.0)

    glEnd()
    glDisable(GL_TEXTURE_3D)
    LoadTextures("aa2.png")
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0),glVertex3f(-80.0, 0.0, -80.0)
    glTexCoord2f(0.0, 0.0),glVertex3f(-80, 30, -80.0)
    glTexCoord2f(1.0, 0.0),glVertex3f(80.0, 30.0, -80.0)
    glTexCoord2f(1.0, 1.0),glVertex3f(80.0, 0.0, -80.0)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0),glVertex3f(-80.0, 0.0, 80.0)
    glTexCoord2f(0.0, 0.0),glVertex3f(-80, 30, 80.0)
    glTexCoord2f(1.0, 0.0),glVertex3f(80.0, 30.0, 80.0)
    glTexCoord2f(1.0, 1.0),glVertex3f(80.0, 0.0, 80.0)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex3f(80.0, 0.0, -80.0)
    glTexCoord2f(0.0, 0.0), glVertex3f(80, 30, -80.0)
    glTexCoord2f(1.0, 0.0), glVertex3f(80.0, 30.0, 80.0)
    glTexCoord2f(1.0, 1.0), glVertex3f(80.0, 0.0, 80.0)
    glEnd()
    LoadTextures("aa1.png")
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex3f(-80.0, 0.0, 80.0)
    glTexCoord2f(0.0, 0.0), glVertex3f(-80, 30, 80.0)
    glTexCoord2f(1.0, 0.0), glVertex3f(-80.0, 30.0, -80.0)
    glTexCoord2f(1.0, 1.0), glVertex3f(-80.0, 0.0, -80.0)
    glEnd()
    glDisable(GL_TEXTURE_3D)
    glPopMatrix()
    getHuman()
    glutSwapBuffers()

def keyPressed(*args):
    global camera
    fraction = 1
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
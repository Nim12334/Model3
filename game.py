import pygame
from pygame.locals import *
from OpenGL.GL import*
from OpenGL.GLU import*
import numpy as np
import time
from PIL import Image
from OpenGL.GLUT import*
from OpenGL.GL.shaders import compileShader,compileProgram
r=1
g=1
b=0
r1=1
g1=1
b1=0
vertices=((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1))
edges=((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
surfaces=((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6))
color=((0,0,1),(0,0,1),(0,1,0),(0,1,0),(1,1,1),(1,1,1),(1,1,0),(1,1,0),(1,1,0),(2,1,0),(1,1,1),(0,1,1))




Texturepack=0,1,1,1,0,0,1,0
def Cube3d():

    glBegin(GL_QUADS)
    x=0
    for surface in surfaces:
        image = pygame.image.load("texture.jpg")
        datas = pygame.image.tostring(image, 'RGBA')

        glEnable(GL_TEXTURE_2D)
        texture_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.get_width(), image.get_height(),
                     0, GL_RGBA, GL_UNSIGNED_BYTE, datas)

        return texture_id
        glColor3fv(color[x])
        glVertex3fv(vertices[vertex])


    glEnd()





    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv(color[x])
            glVertex3fv(vertices[vertex])


    glEnd()
def main():

    start_time = time.time()
    pygame.init()

    display=(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(45,(display[0]/display[1]),0.1,50.0)
    glTranslatef(0,0,-5)
    pygame.display.set_caption("Model 3d(beta)")




    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()


            angle = 0
            x = 0
            y = 0
            z = 0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    angle+=10
                    x+=10
                if event.key==pygame.K_w:
                    angle+=10
                    x-=10
                if event.key==pygame.K_a:
                    angle+=10
                    y-=10
                if event.key==pygame.K_d:
                    angle += 10
                    y += 10
                if event.key==pygame.K_UP:
                    angle+=20
                if event.key==pygame.K_LEFT:
                    angle+=20
                    z+=20
                if event.key == pygame.K_RIGHT:
                    angle += 20
                    z =-20
                if event.key==pygame.K_DOWN:
                    glTranslatef(0,0,1.0)
                if event.key == pygame.K_e:
                    glTranslatef(1.0, 0, 0)
                if event.key == pygame.K_q:
                    glTranslatef(-1.0, 0, 0)

                if event.key == pygame.K_g:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_t:
                    glTranslatef(0, -1, 0)



            x1=glGetDoublev(GL_MODELVIEW_MATRIX)
            y_camera=x1[3][1]



            glRotatef(angle, x, y, z)
            Cube3d()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            pygame.display.flip()
            pygame.time.wait(1)

main()

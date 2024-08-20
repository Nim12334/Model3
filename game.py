import pygame
from pygame.locals import *
from OpenGL.GL import*
from OpenGL.GLU import*
import numpy as np
import time
vertices=((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1))
edges=((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
def Cube3d():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
def main():

    start_time = time.time()
    pygame.init()

    display=(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(45,(display[0]/display[1]),0.1,50)
    glTranslatef(0.0,0.0,-5)
    pygame.display.set_caption("Model 3d")




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















            glRotatef(angle, x, y, z)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            Cube3d()
            pygame.display.flip()
            pygame.time.wait(1)

main()

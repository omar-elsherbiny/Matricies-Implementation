#Imports
import pygame as pyg
from sys import exit as syexit
from MatrixObj import Matrix
from math import sin, cos, radians

pyg.init()

#Globals
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BG_COLOR=(40,40,40)
SIZE=30
SCREEN = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pyg.font.Font("freesansbold.ttf", 20)

#Main
def main():
    clock = pyg.time.Clock()

    S=100
    Ax,Ay,Az=45, 0, 0
    pointx=Matrix('3x1', [[1],[0],[0]])*S
    pointy=Matrix('3x1', [[0],[1],[0]])*S
    pointz=Matrix('3x1', [[0],[0],[1]])*S

    #MAIN LOOP
    run = True
    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                syexit()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    pass
        
        Ax += 0
        Ay += 0
        Az += 0
        rotX=Matrix('3x3',[[1,0,0],[0,cos(radians(Ax)),-sin(radians(Ax))],[0,sin(radians(Ax)),cos(radians(Ax))]])
        rotY=Matrix('3x3',[[cos(radians(Ay)),0,-sin(radians(Ay))],[0,1,0],[sin(radians(Ay)),0,cos(radians(Ay))]])
        rotZ=Matrix('3x3',[[cos(radians(Az)),-sin(radians(Az)),0],[sin(radians(Az)),cos(radians(Az)),0],[0,0,1]])
        rot=rotX@rotY@rotZ
        vrot=rot
        rx=vrot@pointx
        ry=vrot@pointy
        rz=vrot@pointz

        SCREEN.fill(BG_COLOR)
        pyg.draw.line(SCREEN,(255, 10, 50),(250,250),(rx.matrix[0][0]+250,-rx.matrix[1][0]+250),3)
        pyg.draw.line(SCREEN,(50, 255, 10),(250,250),(ry.matrix[0][0]+250,-ry.matrix[1][0]+250),3)
        pyg.draw.line(SCREEN,(10, 50, 255),(250,250),(rz.matrix[0][0]+250,-rz.matrix[1][0]+250),3)

        clock.tick(60)
        pyg.display.set_caption(f'Rendering--{int(clock.get_fps())}')
        pyg.display.update()

if __name__=='__main__':
    main()
# init angles
# put rotation
# alter rotation matrix
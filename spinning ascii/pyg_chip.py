#Imports
import pygame as pyg
from sys import exit as syexit
from MatrixObj import Matrix
from math import sin, cos, radians, sqrt
from random import randint

pyg.init()

#Globals
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BG_COLOR=(20,20,20)
SCREEN = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pyg.font.Font("freesansbold.ttf", 20)

def dist_3d(pnt1,pnt2):
    return sqrt((pnt1.matrix[0][0]-pnt2.matrix[0][0])**2+(pnt1.matrix[1][0]-pnt2.matrix[1][0])**2+(pnt1.matrix[2][0]-pnt2.matrix[2][0])**2)

#Main
def main():
    clock = pyg.time.Clock()

    S=100
    Ax,Ay,Az=15, 0, 0
    pointx=Matrix('3x1', [[1],[0],[0]])*S
    pointy=Matrix('3x1', [[0],[1],[0]])*S
    pointz=Matrix('3x1', [[0],[0],[1]])*S

    pnts=[]
    cpnts=[]
    rX=Matrix('3x3',[[1,0,0],[0,cos(radians(30)),-sin(radians(30))],[0,sin(radians(30)),cos(radians(30))]])
    for phi in range(-100,100,10):
        for theta in range(round(-70*cos(phi/100)),round(70*cos(phi/100)),10):
            if phi<80*cos(theta/100) and phi>-80*cos(theta/100):
                pnts.append(rX@Matrix('3x1',[[theta],[phi+20],[(theta**2-phi**2)/300+50]]))
                cr=randint(145,230)
                cpnts.append((cr,205*cr/230,150*cr/230))

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
        Ay += 2
        Az += 0
        rotX=Matrix('3x3',[[1,0,0],[0,cos(radians(Ax)),-sin(radians(Ax))],[0,sin(radians(Ax)),cos(radians(Ax))]])
        rotY=Matrix('3x3',[[cos(radians(Ay)),0,-sin(radians(Ay))],[0,1,0],[sin(radians(Ay)),0,cos(radians(Ay))]])
        rotZ=Matrix('3x3',[[cos(radians(Az)),-sin(radians(Az)),0],[sin(radians(Az)),cos(radians(Az)),0],[0,0,1]])
        rot=rotX@rotY@rotZ

        rx=rot@pointx
        ry=rot@pointy
        rz=rot@pointz

        rot_pnts=[rot@pnt for pnt in pnts]
        #rot_pnts.sort(key=lambda x: x.matrix[2][0])

        SCREEN.fill(BG_COLOR)
        #pyg.draw.line(SCREEN,(255, 10, 50),(250,250),(rx.matrix[0][0]+250,-rx.matrix[1][0]+250),3)
        #pyg.draw.line(SCREEN,(50, 255, 10),(250,250),(ry.matrix[0][0]+250,-ry.matrix[1][0]+250),3)
        #pyg.draw.line(SCREEN,(10, 50, 255),(250,250),(rz.matrix[0][0]+250,-rz.matrix[1][0]+250),3)
        
        for i,pnt in enumerate(rot_pnts):
            dist=dist_3d(pnt,Matrix('3x1',[[0],[50],[200]]))
            c=(220-dist/2)%255
            pyg.draw.circle(SCREEN,((c+2*cpnts[i][0])/3,(c+2*cpnts[i][1])/3,(c+2*cpnts[i][2])/3),(int(pnt.matrix[0][0]+250),int(-pnt.matrix[1][0]+250+10*sin(Ay/40))),8)
            #draw_text(lightness[round(c*7/85)],int(pnt.matrix[0][0]+250),int(-pnt.matrix[1][0]+250))

        clock.tick(60)
        pyg.display.set_caption(f'Rendering--{int(clock.get_fps())}')
        pyg.display.update()

if __name__=='__main__':
    main()
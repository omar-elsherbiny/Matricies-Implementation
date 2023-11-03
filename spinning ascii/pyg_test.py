#Imports
import pygame as pyg
from sys import exit as syexit
from MatrixObj import Matrix
from math import sin, cos, radians, sqrt

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

    R=70
    Rh=150
    S=100
    Ax,Ay,Az=30, 0, 0
    pointx=Matrix('3x1', [[1],[0],[0]])*S
    pointy=Matrix('3x1', [[0],[1],[0]])*S
    pointz=Matrix('3x1', [[0],[0],[1]])*S

    pnts=[]
    for phi in range(0,360,10):
        #rY=Matrix('3x3',[[cos(radians(phi)),0,-sin(radians(phi))],[0,1,0],[sin(radians(phi)),0,cos(radians(phi))]])
        rZ=Matrix('3x3',[[cos(radians(phi)),-sin(radians(phi)),0],[sin(radians(phi)),cos(radians(phi)),0],[0,0,1]])
        for theta in range(0,360,10):
            pnts.append(rZ@Matrix('3x1',[[0],[R*sin(radians(theta))+Rh],[R*cos(radians(theta))]]))

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
        
        Ax += 1
        Ay += 1
        Az += 1
        rotX=Matrix('3x3',[[1,0,0],[0,cos(radians(Ax)),-sin(radians(Ax))],[0,sin(radians(Ax)),cos(radians(Ax))]])
        rotY=Matrix('3x3',[[cos(radians(Ay)),0,-sin(radians(Ay))],[0,1,0],[sin(radians(Ay)),0,cos(radians(Ay))]])
        rotZ=Matrix('3x3',[[cos(radians(Az)),-sin(radians(Az)),0],[sin(radians(Az)),cos(radians(Az)),0],[0,0,1]])
        rot=rotX@rotY@rotZ

        rx=rot@pointx
        ry=rot@pointy
        rz=rot@pointz

        rot_pnts=[rot@pnt for pnt in pnts]
        rot_pnts.sort(key=lambda x: x.matrix[2][0])

        SCREEN.fill(BG_COLOR)
        pyg.draw.line(SCREEN,(255, 10, 50),(250,250),(rx.matrix[0][0]+250,-rx.matrix[1][0]+250),3)
        pyg.draw.line(SCREEN,(50, 255, 10),(250,250),(ry.matrix[0][0]+250,-ry.matrix[1][0]+250),3)
        pyg.draw.line(SCREEN,(10, 50, 255),(250,250),(rz.matrix[0][0]+250,-rz.matrix[1][0]+250),3)
        
        for pnt in rot_pnts:
            dist=dist_3d(pnt,Matrix('3x1',[[0],[50],[200]]))
            c=(220-dist/2)%255
            pyg.draw.circle(SCREEN,(c,c,c),(int(pnt.matrix[0][0]+250),int(-pnt.matrix[1][0]+250)),5)

        clock.tick(60)
        pyg.display.set_caption(f'Rendering--{int(clock.get_fps())}')
        pyg.display.update()

if __name__=='__main__':
    main()
# init angles
# put rotation
# alter rotation matrix
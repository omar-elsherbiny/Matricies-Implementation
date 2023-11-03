from MatrixObj import Matrix
from time import sleep
from math import sin, cos, radians
import os
import json

with open('config.json', 'r') as f: config=json.load(f)
s=config['size']

arr=[]
with open('initial.txt', 'r') as f: arr = f.readlines()
arr = [r.replace('\n','').split(',')[1:] for r in arr]
arr = [[int(i)-round(s/2) for i in r] for r in arr]

marr=[]
for r in range(s):
    for c in range(s):
        marr.append(Matrix('3x1',[[c-round(s/2)+1],[r-round(s/2)+1],[arr[r][c]]]))

def z_to_lightness(z):
    ls = config['lightness_string']
    return ls[round(z*len(ls)/s)]

Ax,Ay,Az=0,0,0
while True:
    os.system('cls')
    rotX=Matrix('3x3',[[1,0,0],[0,cos(radians(Ax)),-sin(radians(Ax))],[0,sin(radians(Ax)),cos(radians(Ax))]])
    rotY=Matrix('3x3',[[cos(radians(Ay)),0,-sin(radians(Ay))],[0,1,0],[sin(radians(Ay)),0,cos(radians(Ay))]])
    rotZ=Matrix('3x3',[[cos(radians(Az)),-sin(radians(Az)),0],[sin(radians(Az)),cos(radians(Az)),0],[0,0,1]])
    rot=rotX@rotY@rotZ
    for r in range(s):
        rs=''
        for c in range(s):
           rs += z_to_lightness(marr[s*r+c].matrix[2][0])
        print(rs)
    Ax += config['rot_X']
    Ay += config['rot_Y']
    Az += config['rot_Z']
    sleep(0.5)
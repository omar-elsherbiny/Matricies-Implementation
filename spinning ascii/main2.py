from MatrixObj import Matrix
from math import sin, cos, radians
from time import sleep
import json
import os

with open('config.json', 'r') as f: config=json.load(f)
s=config['size']

def print_arr(ar):
    print('\n'.join([' '.join([str(c) for c in r]) for r in ar]))

arr=[[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,4],
     [0,0,0,0,0,0,0,0,4,5],
     [0,0,0,0,5,0,0,4,5,6],
     [0,0,0,0,0,0,4,5,6,7],
     [0,0,0,0,0,4,5,6,7,8],
     [0,0,0,0,4,5,6,7,8,9],
     [0,0,0,4,5,6,7,8,9,9],
     [2,3,4,5,6,7,8,9,9,9]]

#marr=[[Matrix('3x1',[[j],[i],[c]]) for j,c in enumerate(r)] for i,r in enumerate(arr)]
marr=[]
for i,r in enumerate(arr):
    for j,c in enumerate(r):
        marr.append(Matrix('3x1',[[j-4.5],[-i+4.5],[c-4.5]]))

Ax,Ay,Az=0,180,0

while True:
    os.system('cls')
    rotX=Matrix('3x3',[[1,0,0],[0,cos(radians(Ax)),-sin(radians(Ax))],[0,sin(radians(Ax)),cos(radians(Ax))]])
    rotY=Matrix('3x3',[[cos(radians(Ay)),0,-sin(radians(Ay))],[0,1,0],[sin(radians(Ay)),0,cos(radians(Ay))]])
    rotZ=Matrix('3x3',[[cos(radians(Az)),-sin(radians(Az)),0],[sin(radians(Az)),cos(radians(Az)),0],[0,0,1]])
    rot=rotX@rotY@rotZ

    res=[[0 for i in range(10)] for j in range(10)]

    for m in marr:
        rm = rot@m
        try:
            res[int(-rm.matrix[1][0]+4.5)][int(rm.matrix[0][0]+4.5)] = int(rm.matrix[2][0]+4.5)
        except IndexError:
            print(rm.matrix)
    Ax += config['rot_X']
    Ay += config['rot_Y']
    Az += config['rot_Z']
    print_arr(res)
    print(Ay)
    sleep(0.1)
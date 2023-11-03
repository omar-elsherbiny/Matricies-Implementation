import json

f = open('config.json', 'r')
size=json.load(f)['size']
f.close()
st = [f',{round(size/2)}'*size + '\n' for i in range(size)]
f = open('initial.txt', 'w')
f.writelines(st)
f.close()
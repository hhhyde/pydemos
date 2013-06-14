from player import Player;
file=open('F:/name.txt', 'r')
ps=[]

for f in file.readlines():
    print(f),
    ff=Player()
    ff.name=f[1: 3]
    ps.append(ff)

for p in ps:
    print(p.name)

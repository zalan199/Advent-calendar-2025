
import itertools

counter=0
flag0=1

def round(y, x):
    y += x
    global counter, flag0
    flag=1
    

    if y<=0:
        counter -= int(y/100)-flag0
        y=y%100
        flag=0
            

    if y>99:
        if flag:
            counter += int(y/100)
        y=y%100
        
    flag0=1
    if y==0:
        flag0=0
        
    print(y, counter)
    return(y)
    
data=[]
with open("input.txt") as f:
    data.append(50)
    for i in f.readlines():
        x=i.strip()
        dir=1
        if x[0] == "L":
            dir=-1
        y=dir*int(x[1:])
        data.append(y)
    
trial=[50, -66, 32, -16, 200, -346]

res=list(itertools.accumulate(data, round))
print(res.count(0))

print(counter)

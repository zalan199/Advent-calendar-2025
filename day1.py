import itertools

def round(y, x):
    y += x
    if y<0:
        y=100+y%100
    if y>99:
        y=y%100
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
        

res=list(itertools.accumulate(data, round))
print(res.count(0))

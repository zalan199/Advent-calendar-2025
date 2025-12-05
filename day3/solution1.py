#-----file preprocess-----
data=[]
with open("input.txt") as f:
    for i in f.readlines():
        subdata=[]
        count=0
        while(1):
            try:
                subdata.append(int(i.strip()[count]))
                count+=1
            except:
                break
        data.append(subdata)
#print(data)

#------joltage count/batterie------
testdata=[2,3,6,1,4,3,1,2,7, 9, 1, 0, 0, 0]

def joltage(info):
    ma=info.index(max(info))
    if ma==(len(info)-1):
        lastD=max(info)
        firstD=max(info[:-1])
    else:
        firstD=max(info)
        lastD=max(info[(ma+1):])
    return int(str(firstD)+str(lastD))

#print(joltage(testdata))


#-------main-------
sum=0
for i in data:
    sum+=joltage(i)
print(sum)

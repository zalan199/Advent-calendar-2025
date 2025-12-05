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

testdata=[2,3,6,1,4,3,1,2,7, 9, 1, 0, 0, 0]

indexes = []
nest=0


while(len(indexes<12)):
    ma=info.index(max(info))
    indexes.append(ma)
    info = info[ma:]
    if info == []:
        nest-=1
        info = data[indexes[nest]]


def joltage(info, output, index):
    if len(output)==12:
        return (output)
    else:
        ma=info.index(max(info))
        if (ma==(len(info)-1)):
            output=output[:index]+[max(info)]
            joltage(info[:-1], output, 0)
        else:
            output=output[:index]+[max(info)]+output[index:]
            joltage(info[ma+1:], output, index+1)
            
print(joltage(testdata, [], 0))            
            
    

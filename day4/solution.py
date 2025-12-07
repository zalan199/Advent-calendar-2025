#-----file preprocess-----
data=[]
with open("input.txt") as f:
    for i in f.readlines():
        subdata=[]
        i.strip()
        for j in i:
            if j == "@":
                subdata.append(1)
            elif j == ".":
                subdata.append(0)
        data.append(subdata)
#print(data)

res=0
flag=True
vmi=0
res_old=0

while(flag):
    for i in range(len(data)):
        for j in range(len(data[i])):
            #determine environment variables
            if data[i][j]:
                if i == 0:
                    xDim = [0, 1]
                elif i == len(data)-1:
                    xDim = [-1, 0]
                else:
                    xDim = [-1,0,1]
            
                if j == 0:
                    yDim = [0, 1]
                elif j == len(data[i])-1:
                    yDim = [-1, 0]
                else:
                    yDim = [-1,0,1]
                sum=0
                
                #check environment papers
                for x in xDim:
                    for y in yDim:
                        #print(i, j, x, y, len(data), len(data[i]))
                        if data[i+x][j+y]:
                            sum +=1
                #add up removable papiers
                if sum < 5:
                    data[i][j]=0
                    res+=1

    #-------Check if all removables are removed  
    if res == res_old:
        flag=False
    res_old=res
 
print(res)
                        
                    

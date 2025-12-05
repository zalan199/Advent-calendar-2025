#-----file preprocess-----
data_out=[]
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
        data_out.append(subdata)

number_of_tags = 12
testdata=[2,3,6,1,4,3,1,2,7, 9, 1, 0, 0, 0]


#----------joltage count function--------------
def jolt(data):
    #-----init variables-----
    stack=[0, len(data)]
    result=[]
    res=""
    last=stack.pop()
    
    while(len(result)<number_of_tags):
        #------end of the list-----
        if not data[stack[-1]:last]:
            last=stack.pop()-1          #we need to know the end of yet unprocessed data
        else:
            result.append(data[stack[-1]:last].index(max(data[stack[-1]:last]))+stack[-1]+1) #the indexes of resulting number0
            stack.append(data[stack[-1]:last].index(max(data[stack[-1]:last]))+stack[-1]+1)     #stack to go back progress remainin data
        result.sort() #sorting result dataset
    for i in result:
        res+=str(data[i-1])     #creating the result in number, not list
    return int(res)


print(jolt(testdata))
        
        
    
            
    

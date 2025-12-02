#-----file processing----
set = []
with open("input.txt") as f:
    for i in f.readline().split(","):
        set.append(i.strip().split("-"))

#---main----
sum = 0
half=0

"""
set= [["11", "22"], ["95","115"], ["998", "1012"], ["1188511880","1188511890"], ["222220", "222224"], 
        ["1698522","1698528"], ["446443", "446449"], ["38593856","38593862"], ["565653", "565659"], ["824824821","824824827"], 
        ["2121212118", "2121212124"] ]
"""
print(set)
for [min, max] in set:
    if ( len(min)!=len(max) ) or (len(min)%2==0 and len(max)%2 ==0):
        half=int(len(min)/2)
        if half <=0:
            double="1"
        else:
            double=min[:half]
        #print(max)
        #print(( int(double*2) >=int(min) ))
        while int(double*2) <=int(max):
            if ( int(double*2) >=int(min) ):
                print(double*2)
                sum += int(double*2)
                #print(sum)
            double=str(int(double)+1)
            
print(sum)

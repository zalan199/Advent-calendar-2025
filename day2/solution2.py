#-----file processing----
set = []
with open("input.txt") as f:
    for i in f.readline().split(","):
        set.append(i.strip().split("-"))

sum=[]


#----brutforce :(------
for i in range(76576):
    for multiplier in range (2, 12):
        generate=int(str(i)*multiplier)
        
        if generate > 10000000000:
            continue
        for [min, max] in set:
            if (generate in range(int(min), int(max))) and (generate not in sum):
                print(generate)
                sum.append(generate)

sumnum=0
for i in sum:
    sumnum+=i
print(sumnum)

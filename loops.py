skills=["Reading","Listening","Speaking"]  #loops in list
for skill in skills:
    print(skill)


for i in range(1,10):  # loops with range
    print(i,end=" ")
print("\n")    



x=1
while(x<=5): #while loop
    print(x)
    x+=1
print("\n")     

for i in range(0,10): # continuse and break
    if i==5:
        continue
    print(i)
print("\n")     

for i in range(0,10):
    if i==4:
        break
    print(i)  
print("\n")     



for i in range(1,4): # nested loop
    for j in range(1,4):


        print(f"{i}x{j}={i*j}")

    
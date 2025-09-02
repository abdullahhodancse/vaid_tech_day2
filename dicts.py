employees={
    "name":"Abdullah Hodan",
    "age":23,
    "project":"Student management system"
}
print(employees)


print(employees["name"])
print(employees["age"])


employees["salary"]=25000   #new item add
print(employees)


employees.pop("age")  #pop diya delete kora 
print(employees)


del employees["salary"]   #del diya delte kora
print(employees)

for key,value in employees.items(): #dict e loop calano
    print(key,":",value)



print(employees.keys())
print(employees.values())
print (employees.items())
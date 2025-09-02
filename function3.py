def salary(*args,**kwargs):
    days=kwargs.get('days',None) # kwargs argument theke man neya
    rate=kwargs.get('rate',None)

    if days is None or rate is None: #kwargs na thakle positinal argument teke man neya
        if len(args)>=2:  # 2 tarbesi man thakle days and rate k 0,1 index e rakha
            days=args[0]
            rate=args[1]
        else:
            return "Insufficient parameters"
            
    Total_salary=days*rate
    return Total_salary
print(salary(30,2000)) #functon call

print (salary(days=20,rate=600)) # finction call other wway
    









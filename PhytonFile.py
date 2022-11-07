def F(a,b):
    if a>b:
        return 0
    if a==b:
        return 1
    if a<b:
        return F(a+1,b)+F(a+3,b)
print(F(2,15),"Hello")

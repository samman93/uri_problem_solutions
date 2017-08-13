a = int(input())
h=int(a/3600)
a = a%3600
m=int(a/60)
a = a%60
print(str(h)+":"+str(m)+":"+str(a))
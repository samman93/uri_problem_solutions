v = input().split(" ")
v1 = input().split(" ")
a = float(v[0])
b = float(v[1])
c = float(v1[0])
d = float(v1[1])

x = (((c-a)**2)+((d-b)**2))**.5

x  = '{:.4f}'.format(x )
print(x)

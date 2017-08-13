v = input().split(" ")
a = int(v[0])
b = int(v[1])
dct = {1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}

x = float(dct[a] * b)
x  = '{:.2f}'.format(x)
print("Total: R$ "+str(x))
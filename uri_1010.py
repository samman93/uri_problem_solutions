a = input().split(" ")
b = input().split(" ")
# b = float(input())
# c = float(input())
TOTAL = (int(a[1])*float(a[2]))+(int(b[1])*float(b[2]))
TOTAL  = '{:.2f}'.format(TOTAL )
#print("NUMBER = "+str(a))
print("VALOR A PAGAR: R$ "+str(TOTAL))
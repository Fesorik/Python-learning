x = float(input("Print price: "))
y = int(input("Print quantity: "))
b =  int(input("Print percent: "))

total1 = x * y
total2 = (b/100)*total1
print(f"Total: {total1},"f"Percent: {total2}", sep='\n')
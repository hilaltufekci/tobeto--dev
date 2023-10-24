number1 = int(input("1. Sayı: "))
number2 = int(input("2. Sayı: "))
number3 = int(input("3. Sayı: "))
 
if (number1 > number2) and (number1 > number3):
   print("En büyük sayı :{}".format(number1))
elif (number2 > number1) and (number2 > number3):
    print("En büyük sayı :{}".format(number2))
else:
   print("En büyük sayı :{}".format(number3))
 
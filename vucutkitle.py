kilo=int(input("Lütfen kilonuzu giriniz."))


boy=float(input("Lütfen boyunuzu giriniz."))


vki=(kilo/(boy*boy))

if vki < 18 :
    print("Vücut kitle indexiniz zayıf vki:{}" .format(vki))
elif vki<25:
    print("Vücut kitle indexiniz normal vki:{}" .format(vki))
elif vki<30:
    print("Vücut kitle indexiniz kilolu vki:{}" .format(vki))
else:
    print("Vücut kitle indexiniz obez vki:{}" .format(vki))







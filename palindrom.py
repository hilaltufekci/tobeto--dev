sayi = input("Sayıyı giriniz. ")
terssayi=sayi[::-1]

print('Girilen sayının tersi = %s' % (terssayi))
if terssayi == sayi:
    print('Girilen sayi palindrom')
else:
    print('Girilen sayi palindrom değil.')
#coding=windows-1251
print("Введите пятизначное число")
a=int(input())
ed=a%10
des=a%100//10
sot=a%1000//100
tys=a%10000//1000
dtys=a//10000
res=((des**ed)*sot)/(dtys-tys) 
print(res)
print("VSB Calc v1.5")
print(" ")

budzet = float(input("Budżet: "))

print(" ")

procent = float(input("Procent zysku: "))
x = float(input("Liczba klientów: "))

print(" ")

a = float(input("Koszty stałe: "))
b = float(input("Koszty zmienne - pasza: "))
c = float(input("Koszty zmienne - marchew: "))
d = float(input("Koszty zmienne - woda: "))
e = float(input("Koszty zmienne - paliwo: "))

koszty = a + b + c + d + e

o_procent = 1 + procent / 100

print(" ")
print("***************************************")
print(" ")

print("Wszystkie koszty:", "%.2f" % koszty)
print(" ")

zyskna0 = koszty / x
zyskna100 = koszty / x + 100
zysknaproc = (koszty / x) * o_procent

print("Cena biletu dla jednego klienta przy wyjściu na 0:", "%.2f" % zyskna0)
print("Cena biletu dla jednego klienta przy zysku 100 PLN na jednym kliencie:", "%.2f" % zyskna100)
print(("Cena biletu dla jednego klienta przy zysku"), procent, ("% na jednym kliencie:"), "%.2f" % zysknaproc) 
print(" ")
              
if (koszty > budzet):
    print("Za mało środków.")
    print(" ")

elif (budzet > koszty):
    print("Wystarczająco środków.")
    print(" ")

budzetna100 = (budzet - koszty) + (zyskna100 * x)
budzetnaproc = (budzet - koszty) + (zysknaproc * x)

print("Budżet po rajdzie przy zysku 100 PLN:", "%.2f" % budzetna100)
print(("Budżet po rajdzie przy zysku"), procent, ("%:"), "%.2f" % budzetnaproc)

print("VSB Calc v1.0")
print(" ")

budzet = float(input("Budżet: "))

print(" ")

procent = float(input("Procent zysku: "))
x = float(input("Liczba klientów: "))

print(" ")

a = float(input("Koszty stałe: "))
b = float(input("Koszty zmienne - paliwo: "))
c = float(input("Koszty zmienne - siano: "))
d = float(input("Koszty zmienne - słoma: "))
e = float(input("Koszty zmienne - pasza: "))

koszty = a + b + c + d + e

o_procent = 1 + procent / 100

print("Wszystkie koszty:", "%.2f" % koszty)
print(" ")

kosztyna0 = koszty / x
kosztyna100 = koszty / x + 100
kosztynaproc = (koszty / x) * o_procent

print("Cena biletu dla jednego klienta przy wyjściu na 0:", "%.2f" % kosztyna0)
print("Cena biletu dla jednego klienta przy zysku 100 PLN:", "%.2f" % kosztyna100)
print(("Cena biletu dla jednego klienta przy zysku"), procent, ("%:"), "%.2f" % kosztynaproc) 
print(" ")
              
if (koszty > budzet):
    print("Za mało środków.")
    print(" ")

elif (budzet > koszty):
    print("Wystarczająco środków.")
    print(" ")

budzetna100 = (budzet - koszty) + (x * 100)
budzetnaproc = (budzet - koszty) + ((koszty / x) * o_procent)

print("Budżet po rajdzie przy zysku 100 PLN:", "%.2f" % budzetna100)
print(("Budżet po rajdzie przy zysku"), procent, ("%:"), "%.2f" % budzetnaproc)

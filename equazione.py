from math import sqrt


a = 0
while a == 0:
    a = float(input("Inserisci il coefficiente a: "))
b = float(input("Inserisci il coefficiente b: "))
c = float(input("Inserisci il coefficiente c: "))


delta = b**2 - 4 * a * c


if delta < 0:
    print("Delta negativo. Nessuna soluzione reale (impossibile).")
elif delta == 0:
    x = (-b) / (2 * a)
    print("Delta nullo. Unica soluzione x=", x)
else:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print("Delta positivo. Due soluzioni reali x1=", x1, " x2=", x2)
number = int(input("Inserisci un numero intero compreso tra 0 e 99999: "))
i0 = number % 10
number = number // 10
i1 = number % 10
number = number // 10
i2 = number % 10
number = number // 10
i3 = number % 10
i4 = number // 10
print("Le cifre sono: ");
print(i4)
print(i3)
print(i2)
print(i1)
print(i0)
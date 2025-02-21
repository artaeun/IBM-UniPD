"""
Scrivere un programma che riceva in input un numero decimale,
lo converta in binario e lo stampi in output
"""

decimal = int(input("Enter a decimal integer: "))
if decimal == 0: 
    print(0)
else:
    print("Quotient Remainder Binary")
    bstring = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bstring = str(remainder) + bstring
    print("The binary representation is", bstring)  

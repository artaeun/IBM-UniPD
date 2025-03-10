# sortThreeStrings.py
print("Inserire tre stringhe, una per riga")
s1 = input()
s2 = input()
s3 = input()
if s1 <= s2 <= s3 :
   min = s1  
   mid = s2
   max = s3
elif s1 <= s3 <= s2 :
   min = s1  
   mid = s3
   max = s2
elif s2 <= s1 <= s3 :
   min = s2  
   mid = s1
   max = s3
elif s2 <= s3 <= s1 :
   min = s2  
   mid = s3
   max = s1
elif s3 <= s1 <= s2 :
   min = s3  
   mid = s1
   max = s2
else : # s3 <= s2 <= s1
   min = s3  
   mid = s2
   max = s1
print("Le stringhe in ordine crescente sono:")
print(min)
print(mid)
print(max)
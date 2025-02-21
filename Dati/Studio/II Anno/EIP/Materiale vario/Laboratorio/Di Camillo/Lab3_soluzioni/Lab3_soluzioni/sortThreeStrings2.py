# sortThreeStrings2.py
print("Inserire tre stringhe, una per riga")
s1 = input()
s2 = input()
s3 = input()
if s1 <= s2 :
   if s1 <= s3 : 
      min = s1  
      if s2 <= s3 :
         mid = s2
         max = s3
      else :
         mid = s3
         max = s2
   else : 
      min = s3
      mid = s1
      max = s2
else : # s2 < s1
   if s2 <= s3 :
      min = s2
      if s1 <= s3 :
         mid = s1
         max = s3
      else :
         mid = s3
         max = s1
   else :
      min = s3
      mid = s2
      max = s1
print("Le stringhe in ordine crescente sono:")
print(min)
print(mid)
print(max)
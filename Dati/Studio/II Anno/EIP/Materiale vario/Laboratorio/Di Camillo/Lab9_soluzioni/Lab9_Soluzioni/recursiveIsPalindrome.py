# recursiveIsPalindrome.py

def main() :
   s = input("Inserire la stringa da verificare: ")
   if recursiveIsPalindrome(s) :
      print('"%s" è un palindromo' % s);
   else :
      print('"%s" non è un palindromo' % s);
  
def recursiveIsPalindrome(s) :
   if len(s) < 2 :
      return True
   if s[0] != s[-1] :
      return False
   return recursiveIsPalindrome(s[1 : -1])
   
main()
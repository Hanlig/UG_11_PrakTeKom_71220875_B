x = input('masukan kata: bukan katak')
palindrom = True

panjang_x = len(x)

for i in range (panjang_x//2):
     if (x(i) !=[panjang_x-i-1]):
      polindrom = False
     break
 
if polindrom:
     print(x, 'adalah polindrome!')               
else:
    print(x,'bukan palindrome!'); 

def prime(n):
  x=0
  for i in range(2,(n//2)+1):
    if n%i==0:
      x=1
      break;
  if x==0:
    print(n)
prime(13)    
    

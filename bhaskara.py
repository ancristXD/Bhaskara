def bhaskara(a,b,c):
  delta = b**2 - 4*a*c

  if delta < 0:
    return "sem raízes reais"

  elif delta == 0:
    x = -b / (2*a)
    return(x,1)

  else:
    x1 = (-b + delta**0.5)/ (2*a)
    x2 = (-b - delta**0.5)/ (2*a)
    return (x1 , x2)

a = float(input("digite o valor de a:"))
b = float(input("digite o valor de b:"))
c = float(input("digite o valor de c:"))

print(bhaskara(a,b,c))
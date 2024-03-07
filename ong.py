def calcular_factorial(n):
  resultado = 1
  for i in range(1, n + 1):
    resultado *= i
  return resultado

def calcular_productoria(lista):
  resultado = 1
  for num in lista:
    resultado *= num
  return resultado

def calcular(**kwargs):
  for key, value in kwargs.items():
    if 'fact' in key:
      print(f"El factorial de {value} es {calcular_factorial(value)}")
    elif 'prod' in key:
      print(f"La productoria de {value} es {calcular_productoria(value)}")

calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
import sys

precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral, operacion):
  if operacion == 'mayor':
    filtro = {k:v for k,v in diccionario.items() if v > umbral}
  elif operacion == 'menor':
    filtro = {k:v for k,v in diccionario.items() if v < umbral}
  else:
    print("Lo sentimos, no es una operación válida")
    return None  
  return filtro

def resultados(filtrados, operacion):
  if filtrados:
    print(f"Los productos {operacion} al umbral son: {', '.join(filtrados.keys())}")
  else:
    print("No hay productos que cumplan con la condición especificada.")


if len(sys.argv) == 2:
  umbral = int(sys.argv[1])
  operacion = 'mayor'
elif len(sys.argv) == 3 and sys.argv[2] in ['mayor', 'menor']:
  umbral = int(sys.argv[1])
  operacion = sys.argv[2]
else:
  print("Uso incorrecto del programa. Ejemplo: python filtro.py 30000 [mayor|menor]")
  sys.exit(1)

filtrados = filtrar(precios, umbral, operacion)
resultados(filtrados, operacion)
matricula = 120000
seguro = 25000
edad = 0
plan = ''
descuento_matricula = 0.0
 
 
edad = int(input("Ingrese su edad (numero entero): "))
plan = input("Ingrese su plan (PRO, ELITE o BASICO): ")
 
 
 
 
if edad <= 25 and plan in ("PRO", "ELITE"):
 
 
  descuento_matricula = 0.20
 
 
elif edad <= 25 and plan == "BASICO":
 
 
  descuento_matricula = 0.10
 
 
elif 26 <= edad <= 50 and plan in ("PRO", "ELITE"):
 
 
  descuento_matricula = 0.15
 
 
elif 26 <= edad <= 50 and plan == "BASICO":
 
 
  descuento_matricula = 0.05
 
 
else:
 
 
  descuento_matricula = 0
 
 
 
 
valor_matricula = matricula - (matricula*descuento_matricula)
 
 
 
 
if plan == "ELITE" :
 
 
  descuento_seguro = 0.50
 
 
elif plan == "ELITE" and edad > 40:
 
 
  descuento_seguro = 0.60
 
 
else:
 
 
  descuento_seguro = 0
 
 
 
 
valor_seguro = seguro - (seguro*descuento_seguro)
 
 
 
 
print("Valor final matrícula: $", valor_matricula)
 
 
print("Valor final seguro: $", valor_seguro)
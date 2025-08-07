pesos = int(input('what you have left in pesos? ')) 
soles = int(input('what you have left in soles? '))
reais = int(input('what you have left in reais? '))

usd = int(pesos/4122.93+soles/3.59+reais/5.54)

print(float(usd))
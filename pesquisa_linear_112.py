lista = [ 10,  20,  80,  30,  60, 50, 110, 100,  130, 170]

numero = int(input("Digite um numero: "))
sinal = True
contador = 0

while  sinal:

    item = lista[contador]

    if numero ==  item:
        resultado = numero
        sinal = False
        print(f"O numero {numero} ocupa a posição {contador}")
    else:
        contador += 1
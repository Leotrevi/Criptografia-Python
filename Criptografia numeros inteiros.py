
num = int(input("Digite um numero inteiro\n"))

par = ",5"
impar = ",3"

if num%2 == 0:
    num = num + 33
    print(str(num)+",5")

elif num%2 > 0:
    num = num + 21
    print(str(num)+",3")

else:
    print("Caiu no else")
    
 
#descriptografia

numero = float(input("\bDigite o número criptografado (utilizando .) para a descriptografia: \b"))

numero_par = numero
numero_impar = numero

numero_par = numero_par - 0.5 - 33 
numero_impar = numero_impar - 0.3 - 21

if numero_par%2 == 0:
    print(numero_par)

elif numero_impar%2 > 0:
    print(numero_impar)

else:
    print("Caiu no else")



"""
numero.split(",")



numero[2] = " "
print(numero)

"""








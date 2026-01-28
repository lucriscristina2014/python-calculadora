# Titulo da calculadora
print("Calculadora em python")

# Obtendo os numeros e operação
num1 = float(input("digite o primeiro numero:"))
operador = input("digite o operador (+,-):")
num2 = float(input("digite o segundo numero:"))

# Realizando a operação
if operador == "-":
    resultado = num1 - num2   
elif operador == "+":  
    resultado = num1 + num2
else:
    print("Operador Inválido")
    exit()

# Exibindo o resultado
print("resultado:", resultado)

num1 = int(input("Digite um números: "))
ope = input("Digite a operação: ")
num2 = int(input("Digite um número: "))

if ope == "+":
    print(num1 + num2)
elif ope == "-":
    print(num1 - num2)
elif ope == "*":
    print(num1 * num2)

elif ope == "/":
 if num2 != 0:
        print(num1 / num2)
 else:
        print("Erro: divisão por zero não é permitida.")


else:
    print("Operação inválida. Use +, -, * ou /.")

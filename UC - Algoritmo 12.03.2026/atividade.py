#questao1
def calcularsomaeproduto():

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2
    produto = num1 * num2

    print(f"A soma é: {soma}")
    print(f"O produto é: {produto}")

calcularsomaeproduto()

#questao2
def calcularSalario(hora, totalHoras):

    salarioTotal = hora * totalHoras
    return salarioTotal

valor = float(input("Digite o valor por hora: R$ "))
horas = float(input("Digite o total de horas trabalhadas: "))

total = calcularSalario(valor, horas)

print(f"O salário total é: R$ {total:.2f}")

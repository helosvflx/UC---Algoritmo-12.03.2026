#Sem função
print("Python é facil")
print("Python é facil")
print("Python é facil")

#Com função
def exibirMensagem():
    print("Olá, mundo!")

exibirMensagem()

#Função com parâmetro
def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")
saudar("Bruno")

def exibirMensagem(nome, mensagem):
    print(f"{mensagem}, {nome}")

exibirMensagem("Ana", "Bom dia")

#parametros nomeados
exibirMensagem(nome = "Bruno", mensagem = "Boa noite")


#função que retorna média
def calcularMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media 

resultado = calcularMedia(8.0, 9.0)
print(f"Média: {resultado}")
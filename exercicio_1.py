print("Bem-vindo(a) ao nosso site! Para comprar um ingresso primeiro é necessário saber a sua idade")
idade_str = input("Quantos anos você tem?")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade. Você pode comprar o ingresso.")
else:
    if (idade <= 12):
        print("Você é uma criança. Você não pode comprar o ingresso.")
    elif (idade > 12):
        print("Você é um adolescente. Você não pode comprar o ingresso.")
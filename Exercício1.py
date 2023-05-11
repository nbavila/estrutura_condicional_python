print("Bem vindo a loja do Lucas Lima de Ávila")
produto = float(input("Entre com valor do produto: "))
quantidade = int(input("Entre com valor da quantidade: "))
# multiplicação do produto e da quantidade, resultando no total do valor
total = produto * quantidade
print("O valor sem desconto foi: R$ {:.2f}".format(total))

if quantidade <= 9:
    # cálculo do desconto de 0% do produto
    desconto = total * 0 /100
    # cálculo do produto com o desconto incluso
    total = total - desconto
    print("O valor com desconto foi: R$ {:.2f}".format(total), ("(desconto 0%)"))
elif quantidade >= 10 and quantidade <= 99:
    # cálculo do desconto de 5% do produto
    desconto = total * 5 / 100
    # cálculo do produto com o desconto incluso
    total = total - desconto
    # valor total do produto, com o desconto de 5% aplicado
    print("O valor com desconto foi: R$ {:.2f}".format(total), "(desconto 5%)")
elif quantidade >= 100 and quantidade <= 999:
    # cálculo do desconto de 10% do produto
    desconto = total * 10 / 100
    # cálculo do produto com o desconto incluso
    total = total - desconto
    # valor total do produto, com o desconto de 10% aplicado
    print("O valor com desconto foi: R$ {:.2f}".format(total), "(desconto 10%)")
else:
        # cálculo do desconto de 15% do produto
        desconto = total * 15 / 100
        # cálculo do produto com o desconto incluso
        total = total - desconto
        # valor total do produto, com o desconto de 15% aplicado
        print("O valor com desconto foi: R$ {:.2f}".format(total), "(desconto 15%)")

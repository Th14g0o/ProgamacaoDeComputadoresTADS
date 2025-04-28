preco = int(input())
qtd = int(input())
saldo = int(input())

print("A pagar: {}\nTroco  : {}".format(preco * qtd, saldo - preco * qtd))
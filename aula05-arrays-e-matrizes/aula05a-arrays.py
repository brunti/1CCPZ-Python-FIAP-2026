lista_frutas = ["Banana", "Maça", "Morango"]

#Lista_fruta[0] = "Banana"
#Lista_fruta[1] = "Maça"
#Lista_fruta[2] = "Morango"
print(lista_frutas[0])

lista_frutas.append("Uva")
print(lista_frutas[-1])

tamanho = len(lista_frutas)
print(tamanho)

for i in range(tamanho):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)

msg = "Oi Fulano!"

for i in range(len(msg)):
    print(msg[i])
from linkedlist import LinkedList

class Teste:
    if __name__ == '__main__':
        lista = LinkedList()

        lista.append(9)
        lista.append(80)
        lista.append(60)
        lista.append(32)
        print(len(lista))
        print(lista.index(80))
        lista.insert(0, 22)
        lista.insert(3, 852)
        lista.remove(9)
        print(len(lista))
        # lista.insert(len(lista),50)
        print(lista[0])
        # print(len(lista)-1)
        print(lista)
        lista.remove(80)
        print(lista)
        lista.remove(852)
        print(lista)


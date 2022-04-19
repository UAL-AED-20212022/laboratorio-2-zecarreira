from models.LinkedList import LinkedList
from models.Node import Node

def main():
    lista_ligada = LinkedList()

    while True:
        comandos = input().split()

        if comandos[0] == "RPI":
            lista_ligada.insert_at_start(comandos[1])
            lista_ligada.traverse_list()


        elif comandos[0] == "RPF":
            lista_ligada.insert_at_end(comandos[1])
            lista_ligada.traverse_list()


        elif comandos[0] == "RPDE":
            lista_ligada.insert_after_item(comandos[1],comandos[2])
            lista_ligada.traverse_list()

        elif comandos[0] == "RPAE":
            lista_ligada.insert_before_item(comandos[1],comandos[2])
            lista_ligada.traverse_list()

        elif comandos[0] == "RPII":
            lista_ligada.insert_at_index(int(comandos[1]),comandos[2])
            lista_ligada.traverse_list()

        elif comandos[0] == "VNE":
            print(f"O número de elementos são {lista_ligada.get_count()}")

        elif comandos[0] == "VP":
            if lista_ligada.search_item(comandos[1]) == True:
                print(f"O país {comandos[1]} encontra-se na lista.")
            else:
                print(f"O país {comandos[1]} não se encontra na lista.")

        elif comandos[0] == "EPE":
            a = lista_ligada.start_node.get_item()
            print(f"O país {a} foi eliminado da lista.")
            lista_ligada.delete_at_start()

        elif comandos[0] == "EUE":
            b = lista_ligada.get_last_node()
            print(f"O país {b} foi eliminado da lista.")
            lista_ligada.delete_at_end()

        elif comandos[0] == "EP" and (len(comandos) == 2):

            if lista_ligada.search_item(comandos[1]) == False:
                print(f"O país {comandos[1]} não se encontra na lista.")
            else:
                print(f"O país {comandos[1]} foi eliminado da lista.")
                lista_ligada.delete_element_by_value(comandos[1])

        elif comandos[0] == "lista":
            lista_ligada.traverse_list()
            print()

                
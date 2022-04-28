
from models.LinkedList import LinkedList

def main():

    try:

        lista_ligada = LinkedList()

        while True:

            comandos = input().split()

            if comandos[0] == "RPI":      #Registar país no fim da lista

                lista_ligada.insert_at_start(comandos[1])

                lista_ligada.traverse_list()
                    
            elif comandos[0] == "RPF":     #Registar país no fim da lista

                lista_ligada.insert_at_end(comandos[1])

                lista_ligada.traverse_list()

            elif comandos[0] == "RPDE":     #Registar país depois de outro elemento já registado

                lista_ligada.insert_after_item(comandos[2], comandos[1])

                lista_ligada.traverse_list()

            elif comandos[0] == "RPAE":     #Registar país antes outro elemento.

                lista_ligada.insert_before_item(comandos[2], comandos[1])

                lista_ligada.traverse_list()
                
            elif comandos[0] == "RPII":     #Registar pais num determinado indice

                lista_ligada.insert_at_index(int(comandos[2]), comandos[1])

                lista_ligada.traverse_list()

            elif comandos[0] == "VNE":

                temp = lista_ligada.get_count()
                print(f"O número de elementos são {temp}.")

            elif comandos[0] == "VP":

                if lista_ligada.search_item(comandos[1]):
                    print(f"O país {comandos[1]} encontra-se na lista.")
                else:
                    print(F"O país {comandos[1]} não se encontra na lista.")
                    
            elif comandos[0] == "EPE":

                temp = lista_ligada.start_node.get_item()

                print(f"O país {temp} foi eliminado da lista.")

                lista_ligada.delete_at_start()
            
            elif comandos[0] == "EUE":
                
                temp = lista_ligada.get_last_node()

                print(f"O país {temp} foi eliminado da lista.")

                lista_ligada.delete_at_end()

            elif comandos[0] == "EP":

                temp = comandos[1]

                if lista_ligada.search_item(comandos[1]) == True:

                    print(f"O país {temp} foi eliminado da lista.")

                    lista_ligada.delete_element_by_value(comandos[1])

                else:
                    print(f"O país {temp} encontra-se na lista.")

            else:
                print()

    except EOFError:
                return
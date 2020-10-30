import re

#Clase Menu , Para Que El Usuario Permita Elegir que Buscar , Como y  en que Paginas
class menu:
    def __init__(self):

        #Whiles True que me permite mantener al usuario ahi , hasta que Los Valores Sean Dentro De Lo Deseado
        while True:
            self.__a_buscar = input("¿Que Desea Buscar? \n")

            #El Metodo IsSpace() Me Permite Saber Si El Valor Ingresado es solamente espacios
            if not self.__a_buscar.isspace():
                break
        
        while True:
            try:
                #Utilizo int(input("...")) para asegurarme que lo que entre en el sistema sea si o si Un integer , caso contrario entra en el Except ya que el int() tira error
                self.__metodo_busqueda = int(input("¿Que Metodo De Busqueda Quiere Utilizar? \n 1)Frase Completa \n 2)Que Contenga Todas Las Palabras \n 3)Que Contenga Algunas Palabras \n "))
                if(self.__metodo_busqueda < 4 and self.__metodo_busqueda > 0):
                    break
                else:
                    print("Esa No Es Una Opcion Valida")
            except:
                print("Tiene que ingresar Un Numero")
        
        while True:
            self.__paginas_a_buscar = input("¿En Que Paginas Desea Buscar? (Escribir De Esta Manera Si es mas de 1 pagina.  1,2,3,4,5) \n 1)Garbarino \n 2)Rodo \n 3)Compumundo \n 4)Fravega \n")
            match = re.fullmatch("^[1-4]?[,[1-4]+$",self.__paginas_a_buscar)

            if(match != None):
                #Verificamos Que Se Cumpla La Expresion Regular con un match igual de largo que lo ingresado
                if len(match.string) == len(self.__paginas_a_buscar):

                 if self.__verificar_valores(self.__paginas_a_buscar):
                      break



            
    #Metodo Para Verificar Cada Caracter Separado por ","

    def __verificar_valores(self,linea):
        valores_separados = linea.split(",")

        #Caso De Que Algun Valor Del Input no coincida con las opciones , returnee False
        for valor in valores_separados:
            if int(valor) > 4 or int(valor) < 1:

                #Envio Mensaje De Error Y Corto Operaciones
                print("Algun Numero No Existe En Las Opciones")
                return False

        #Este For Es Para Evaluar que no existan 2 valores iguales separados por "," Ej: 1,1 o 1,2,1
        for itinerable in range(0,len(valores_separados)):

            for valor_a_evaluar in range(itinerable +1 , len(valores_separados)):

                if int(valores_separados[itinerable]) == int(valores_separados[valor_a_evaluar]):
                    print("Existen 2 Numeros Repetidos , Eso No Puede Ocurrir")
                    return False
                    
        #Caso De Que todos Los valores Coincidan con las opciones retunee True
        return True


    #Metodos Get....

    def geta_buscar(self):
        return self.__a_buscar
    
    def getmetodo_busqueda(self):
        return self.__metodo_busqueda
    
    def getpaginas_a_buscar(self):
        return self.__paginas_a_buscar

if __name__ == "__main__":
    casa = menu()
    print(casa.geta_buscar())
    print(casa.getmetodo_busqueda())
    print(casa.getpaginas_a_buscar())

import re
from ordenador import organizador
from scrapy.crawler import CrawlerProcess
from tp_2020.tp_2020.spiders.rodo import RodoSpider
from tp_2020.tp_2020.spiders.fravega import FravegaSpider
from tp_2020.tp_2020.spiders.compumundo import CompumundoSpider
from tp_2020.tp_2020.spiders.garbarino import GarbarinoSpider
from filtrador import Filtrador

#Clase Menu , para que el usuario permita elegir que buscar, como y en que páginas
class Menu:
    def __init__(self):

        #While es True que me permite mantener al usuario ahi ,
        #hasta que los valores sean dentro de lo deseado
        while True:
            self.__a_buscar = input("¿Que desea buscar? \n")

            #El Metodo IsSpace() Me Permite Saber Si El Valor Ingresado es solamente espacios
            if not self.__a_buscar.isspace():
                break

        while True:
            try:
                #Utilizo int(input("...")) para asegurarme que lo que entre en el sistema sea
                #si o si Un integer , caso contrario entra en el Except ya que el int() tira error
                self.__metodo_busqueda = int(input(
                        "¿Que metodo de busqueda quiere utilizar?" +
                        " \n 1)Frase completa \n 2)Que contenga todas las palabras "+
                        " \n 3)Que contenga algunas palabras \n ")
                    )
                if(self.__metodo_busqueda < 4 and self.__metodo_busqueda > 0):
                    break
                else:
                    print("Esa no es una opcion valida")
            except:
                print("Tiene que ingresar un numero")

        while True:
            self.__paginas_a_buscar = input(
                "¿En que paginas desea buscar? "+
                " (Escribir de esta manera si es mas de 1 pagina. 1,2,3,4,5) "+
                " \n 1)Garbarino \n 2)Rodo \n 3)Compumundo \n 4)Fravega \n")
            match = re.fullmatch("^[1-4]?[,[1-4]+$",self.__paginas_a_buscar)

            if(match != None):
                #Verificamos Que Se Cumpla La Expresion Regular con un match igual
                #de largo que lo ingresado
                if len(match.string) == len(self.__paginas_a_buscar):

                 if self.__verificar_valores(self.__paginas_a_buscar):
                      break

        # Acá debería scrapearse los 4 marketplaces
        scrapeo = self.scrapear()
        print(scrapeo)


    #Metodo Para Verificar Cada Caracter Separado por ","
    def __verificar_valores(self,linea):
        valores_separados = linea.split(",")

        #Caso De Que Algun Valor Del Input no coincida con las opciones , returnee False
        for valor in valores_separados:
            if int(valor) > 4 or int(valor) < 1:

                #Envio Mensaje De Error Y Corto Operaciones
                print("Algun numero no existe en las opciones")
                return False

        #Este For Es Para Evaluar que no existan 2 valores iguales separados por "," Ej: 1,1 o 1,2,1
        for itinerable in range(0,len(valores_separados)):

            for valor_a_evaluar in range(itinerable +1 , len(valores_separados)):

                if int(valores_separados[itinerable]) == int(valores_separados[valor_a_evaluar]):
                    print("Existen 2 numeros repetidos, eso no puede ocurrir")
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

    def __elegir_tipo_de_filtrado(self,numero,resultados_busqueda ):
        res = []
        if numero == 1:
            res = Filtrador.frase_completa(resultados_busqueda, self.__a_buscar)
        elif numero == 2:
            res = Filtrador.contenga_todas_las_palabras(resultados_busqueda, self.__a_buscar)
        elif numero == 3:
            res = Filtrador.contenga_algunas_palabras(resultados_busqueda, self.__a_buscar)

        return res

    def scrapear(self):
        paginas_busqueda_split = str(self.__paginas_a_buscar).split(",")
        process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
        #Con Esto Se Seleccionan que Spiders vamos a usar
        for pagina in paginas_busqueda_split:
            if pagina == "1":
                process.crawl(GarbarinoSpider,self.__a_buscar)
            if pagina == "2":
                process.crawl(RodoSpider,self.__a_buscar)
            if pagina == "3":
                process.crawl(CompumundoSpider,busqueda=self.__a_buscar)
            if pagina == "4":
                process.crawl(FravegaSpider,self.__a_buscar)

        #Se Ejecutan Las Spiders, el parameto stop_after_crawl=true , determina que hasta que no se terminen de scrapear todas las spider no pare
        process.start()
        resultados_busqueda = []
        for resultado in paginas_busqueda_split:
            if resultado == "1":
                resultados_busqueda = resultados_busqueda + GarbarinoSpider.respuesta
            if resultado == "2":
                resultados_busqueda = resultados_busqueda + RodoSpider.respuesta
            if resultado == "3":
                resultados_busqueda = resultados_busqueda + CompumundoSpider.respuesta
            if resultado == "4":
                resultados_busqueda = resultados_busqueda + FravegaSpider.respuesta

        Filtrador.contenga_algunas_palabras(resultados_busqueda, self.__a_buscar)

        resultados_busqueda = self.__elegir_tipo_de_filtrado(self.__metodo_busqueda,
                resultados_busqueda )
        organizador(resultados_busqueda,self.__metodo_busqueda,self.__a_buscar)

if __name__ == "__main__":
    casa = Menu()
    casa.geta_buscar()
    casa.getmetodo_busqueda()
    casa.getpaginas_a_buscar()

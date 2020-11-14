import datetime
import csv

class organizador:
    def __init__(self,lista_resultados,metodo_busqueda,buscado):
        self.resultados = lista_resultados
        self.metodo_busqueda = metodo_busqueda
        self.buscado = buscado.replace("+","_")
        #Aca Se Tiene Que Seleccionar segun El Tipo De Busqueda El Metodo De seleccion
        
        if metodo_busqueda == 1: 
            self.resultados = self.busqueda_exacta(self.resultados.copy())
        if metodo_busqueda == 2:
            self.resultados = self.busqueda_con_las_palabras(self.resultados.copy())
        if metodo_busqueda == 3:
            self.resultados = self.busqueda_con_algunas_palabras(self.resultados.copy())
        
        self.escribir_Csv(self.resultados)

    def escribir_Csv(self,resultados):
        dateNow = datetime.datetime.now()
        with open(self.buscado+"_"+str(dateNow.year)+"-"+str(dateNow.month)+"-"+str(dateNow.day)+".csv","w",encoding="utf-8",newline="") as archivo:
            writer = csv.DictWriter(archivo,delimiter="," ,fieldnames = ["producto","precio","link","fecha"])
            writer.writeheader()
            for resultado in resultados:
                writer.writerow({"producto":resultado[0],"precio":resultado[1],"link":resultado[2]})#,"fecha":resultado[3]})
            

    def busqueda_exacta(self,lista_de_resultados):
        #Aca Se hace cual sacamos y cual no
        return lista_de_resultados
    
    def busqueda_con_las_palabras(self,lista_de_resultados):
        #Aca se hace cual sacamos y cual no
        return lista_de_resultados
    
    def busqueda_con_algunas_palabras(self,lista_de_resultados):
        #Aca se hace cual sacamos y cual no
        return lista_de_resultados
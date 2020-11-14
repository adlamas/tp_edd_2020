import datetime
import csv

class organizador:
    def __init__(self,lista_resultados,metodo_busqueda,buscado):
        self.resultados = lista_resultados
        self.metodo_busqueda = metodo_busqueda
        self.buscado = buscado.replace("+","_")
        self.escribir_Csv(self.resultados)

    def escribir_Csv(self,resultados):
        dateNow = datetime.datetime.now()
        with open(self.buscado+"_"+str(dateNow.year)+"-"+str(dateNow.month)+"-"+str(dateNow.day)+".csv","w",encoding="utf-8",newline="") as archivo:
            writer = csv.DictWriter(archivo,delimiter="," ,fieldnames = ["producto","precio","link","fecha"])
            writer.writeheader()
            for resultado in resultados:
                writer.writerow({"producto":resultado[0],"precio":resultado[1],"link":resultado[2]})#,"fecha":resultado[3]})

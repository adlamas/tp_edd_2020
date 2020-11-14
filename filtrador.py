class Filtrador:

    def frase_completa(self, resultados_sin_filtrar, frase):
        resultado_total_filtrado = []
        for arreglo_prod in resultados_sin_filtrar:
            if frase in arreglo_prod[0]:
                resultado_total_filtrado.append(arreglo_prod)

        return resultado_total_filtrado

    def contenga_todas_las_palabras(self, resultados_sin_filtrar, frase):
        resultado_total_filtrado = []
        array_palabras = frase.split()
        for arreglo_prod in resultados_sin_filtrar:
            guardia = True
            for palabra in array_palabras:
                if palabra not in arreglo_prod[0]:
                    guardia = False
                    break

            if guardia == True:
                resultado_total_filtrado.append(arreglo_prod)

        return resultado_total_filtrado

    def contenga_algunas_palabras(self, resultados_sin_filtrar, frase):
        resultado_total_filtrado = []
        array_palabras = frase.split()
        for arreglo_prod in resultados_sin_filtrar:
            guardia = False
            for palabra in array_palabras:
                if palabra in arreglo_prod[0]:
                    guardia = True
                    break

            if guardia == True:
                resultado_total_filtrado.append(arreglo_prod)

        return resultado_total_filtrado

import importlib
import importlib.util
spec = importlib.util.spec_from_file_location("Filtrador", "filtrador.py")
filtrador = importlib.util.module_from_spec(spec)
spec.loader.exec_module(filtrador)
filtrador.Filtrador()

def test_frase_completa_ok():
    frase = 'Heladera con freezer'
    fi = filtrador.Filtrador()
    resultados = [
        ['Una Heladera con freezer V540 2019 Philips',1,1],
        ['Una Heladera sin freezer V540 2019 Philips',1,1],
        ['Heladera con freezer L302 2017 Philco',1,1]
    ]
    #import pdb; pdb.set_trace()
    res = fi.frase_completa(resultados, frase)
    assert(res == [resultados[0], resultados[2]])

def test_algunas_palabras_ok():
    frase = 'Heladera'
    fi = filtrador.Filtrador()
    resultados = [
        ['Una Heladera con freezer V540 2019 Philips',1,1],
        ['Una Heladera sin freezer V540 2019 Philips',1,1],
        ['freezer L302 2017 Philco',1,1]
    ]
    #import pdb; pdb.set_trace()
    res = fi.contenga_algunas_palabras(resultados, frase)
    assert(res == [resultados[0], resultados[1]])


def test_todas_las_palabras():
    frase = 'Heladera Freezer'
    fi = filtrador.Filtrador()
    resultados = [
        ['Una Heladera V540 2019 Philips',1,1],
        ['Una Heladera sin Freezer V540 2019 Philips',1,1],
        ['Freezer L302 2017 Philco Heladera',1,1]
    ]
    #import pdb; pdb.set_trace()
    res = fi.contenga_todas_las_palabras(resultados, frase)
    assert(res == [resultados[1], resultados[2]])

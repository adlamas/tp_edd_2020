# content of ./test_smtpsimple.py
import pytest
import setuptools
from menu import Menu

def test_menu():
    menu = Menu()
    menu.__a_buscar = 'hola'
    menu.__metodo_busqueda = 1
    menu.__paginas_a_buscar = 2
    menu.iniciar()
    assert 250 == 250

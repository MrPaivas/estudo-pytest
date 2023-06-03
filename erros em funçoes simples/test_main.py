import pytest

from main import *


def testa_soma():
    dois_mais_dois = soma_com_2(2)
    assert dois_mais_dois == 4

def testa_sub():
    dois_menos_dois = subtrai_2(2)
    assert dois_menos_dois == 0

def testa_mult():
    dois_multi_dois = multiplica_2(2)
    assert dois_multi_dois == 4

def testa_div():
    dois_div_dois = divide_2(2)
    assert dois_div_dois == 1
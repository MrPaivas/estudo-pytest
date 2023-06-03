import pytest
from main import *

class TestMyClass():
    def test_oferece_leite(self):
        chama_classe = MeuFihQuer("LEITE")
        testar = chama_classe.mim_deh_papai()
        assert testar == False

    def test_oferece_bolacha(self):
        chama_classe = MeuFihQuer("BOLACHA")
        testar = chama_classe.mim_deh_papai()
        assert testar == False

    def test_oferece_cachaca(self):
        chama_classe = MeuFihQuer("CACHAÇA")
        testar = chama_classe.mim_deh_papai()
        assert testar == True
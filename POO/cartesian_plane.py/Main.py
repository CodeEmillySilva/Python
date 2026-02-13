from EspacoGeometrico import EspacoGeometrico
from ObjetoSobrepostoException import ObjetoSobrepostoException
from Ponto2D import Ponto2D
from Reta import Reta

reta1 = Reta(1,2)
reta2 = Reta(1,1)
reta3 = Reta(2,-2)

pontoA = Ponto2D(3,4)
pontoB = Ponto2D(2,3)
pontoC = Ponto2D(4,6)
pontoD = Ponto2D(3,2)

adicionar = EspacoGeometrico()

try:
    adicionar.adicionarReta(reta1)
    print("Reta1 adicionada com sucesso")
except ObjetoSobrepostoException as erro:
    print(erro)

try:
    adicionar.adicionarReta(reta2)
    print("Reta2 adicionada com sucesso")
except ObjetoSobrepostoException as erro:
    print(erro)

try:
    adicionar.adicionarReta(reta3)
    print("Reta3 adicionada com sucesso")
except ObjetoSobrepostoException as erro:
    print(erro)

try:
    adicionar.adicionarPonto(pontoA)
    print("PontoA adicionada com sucesso")
except ObjetoSobrepostoException as erro:
    print(erro)

try:
    adicionar.adicionarPonto(pontoB)
    print("PontoB adicionada com sucesso")
except ObjetoSobrepostoException as erro:
    print(erro)

try:
    adicionar.adicionarPonto(pontoC)
    print("PontoC adicionada com sucesso")
except ObjetoSobrepostoException as erro:
    print(erro)

try:
    adicionar.adicionarPonto(pontoD)
    print("PontoD adicionada com sucesso")
except ObjetoSobrepostoException as erro:
    print(erro)

print("\n")
print(adicionar)

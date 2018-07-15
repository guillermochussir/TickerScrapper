import json
import sys
from classes.extractor import Extractor
from classes.pedido import Pedido

def LlevarPedido(parametro,extractor):
    pedido = Pedido(parametro)
    extractor.extraer(pedido)

if __name__ == '__main__':
    with open('configs/urls.json') as f:
        NombresPedidos = json.load(f)
    if len(sys.argv) == 1:
        print ("Me podés pedir: {0}".format(list(NombresPedidos.keys())))
    elif sys.argv[1] in list(NombresPedidos.keys()):
        _parametro = sys.argv[1]
        _extractor = Extractor()
        print ("Sale {0} con fritas".format(_parametro))
        LlevarPedido(_parametro,_extractor)
    else:
        print ("Pedido incorrecto. Me podés pedir: {0}".format(list(NombresPedidos.keys())))
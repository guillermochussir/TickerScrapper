import json
import sys
from extractor import Extractor
from pedido import Pedido

def LlevarPedido(parametro,extractor):
    if parametro == "GetFundsProducts":
        with open('urls.json') as f:
            urls = json.load(f)
        url = urls["GetFundsProducts"] + urls["GetFundsProductsParams"]
    elif parametro == "GetPriceData":
        with open('urls.json') as f:
            urls = json.load(f)
        url = urls["GetPriceData"]
    elif parametro == "GetIndustryGroupPieData":
        with open('urls.json') as f:
            urls = json.load(f)
        url = urls["GetIndustryGroupPieData"]
    elif parametro == "GetIndustrySectorPieData":
        with open('urls.json') as f:
            urls = json.load(f)
        url = urls["GetIndustrySectorPieData"]
    elif parametro == "GetCompositionPieData":
        with open('urls.json') as f:
            urls = json.load(f)
        url = urls["GetCompositionPieData"]
    else:
        print ("Perdón, lo que me pediste no está en el menu")
        exit()
    pedido = Pedido(url)
    extractor.extraer(pedido)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print ("Me podés pedir: GetFundsProducts, GetPriceData, GetIndustryGroupPieData, GetIndustrySectorPieData, GetCompositionPieData")
    else:
        _parametro = sys.argv[1] 
        _extractor = Extractor()
        print ("Sale {0} con fritas".format(_parametro))
        LlevarPedido(_parametro,_extractor)
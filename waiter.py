import json
from extractor import Extractor
from pedido import Pedido

def main(extractor,pedido):
    extractor.extraer(pedido)


if __name__ == '__main__':
    _extractor = Extractor()
    with open('urls.json') as f:
        urls = json.load(f)
    url = urls["GetFundsProducts"] + urls["GetFundsProductsParams"]
    _pedido = Pedido(url)
    main(_extractor,_pedido)
import requests
import pandas as pd
import json
import csv

class Extractor:

    def ConseguirURL(self,pedido):
        with open('urls.json') as f:
            urls = json.load(f)
        return urls[pedido.nombre]

    def request(self, url):
        for tries in range(1, 4):
            try:
                print (url)
                r = requests.get(url)
                return r.text
            except Exception as e:
                print (e.reason)
                if tries < 3:
                    print ('hubo un error. reintentando en 5 segundos')
                    time.sleep(5)
                else:
                    print ('tercer error.')

    def extraer(self, pedido):
        url = self.ConseguirURL(pedido)
        with open('PedidosaTickers.json') as f:
            PedidosaTickers = json.load(f)
        if pedido.nombre in PedidosaTickers:
            with open('GetFundsProducts.csv','rt') as f:
                reader = csv.reader(f)
            next(reader)  # Skip header row
            df = []
            for row in reader:
                ticker = row[4]
                urlfinal = url + ticker
                fundValues = json.loads(self.request(urlfinal))
                fundValues = fundValues["fundValues"]
                for i in fundValues:
                    i['ticker'] = ticker
                for i in fundValues:
                    df.append(i)
            df = pd.DataFrame.from_records(df)
            if df is not None:
                print(str(len(df)) + ' filas')
                print ('exportando a {0}.csv'.format(pedido.nombre))
                df.to_csv('{0}.csv'.format(pedido.nombre), index=False)
            else:
                print ('error. df vacío')
        else:
            records = json.loads(self.request(url))

            records = records["records"]
            df = pd.DataFrame.from_records(records)
            if df is not None:
                print(str(len(df)) + ' filas')
                print ('exportando a {0}.csv'.format(pedido.nombre))
                df.to_csv('{0}.csv'.format(pedido.nombre), index=False)
            else:
                print ('error. df vacío')
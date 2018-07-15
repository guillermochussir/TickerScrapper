import requests
import pandas as pd
import json
import csv
import os.path

class Extractor:

    def ConseguirURL(self,pedido):
        with open('configs/urls.json') as f:
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

    def exportar(self,df,pedido):
        df = pd.DataFrame.from_records(df)
        if df is not None:
            print(str(len(df)) + ' filas')
            print ('exportando a {0}.csv'.format(pedido.nombre))
            df.to_csv('output/{0}.csv'.format(pedido.nombre), index=False)
        else:
            print ('error. df vacío')

    def extraer(self, pedido):
        url = self.ConseguirURL(pedido)
        with open('configs/PedidosaTickers.json') as f:
            PedidosaTickers = json.load(f)
        if pedido.nombre in PedidosaTickers:
            if os.path.isfile("output/GetFundsProducts.csv") == False:
                print ("output/GetFundsProducts.csv not found")
                print ("Para generar GetFundsProducts.csv, ejecutar waiter.py GetFundsProducts")
                exit()
            with open('output/GetFundsProducts.csv','rt') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                df = []
                for row in reader:
                    ticker = row[4]
                    urlfinal = url + ticker
                    fundValues = json.loads(self.request(urlfinal))
                    if pedido.nombre == "GetPriceData":
                        fundValues = fundValues["fundValues"]
                    for i in fundValues:
                        i['ticker'] = ticker
                    for i in fundValues:
                        df.append(i)
            self.exportar(df,pedido)
        else:
            records = json.loads(self.request(url))

            df = records["records"]
            self.exportar(df,pedido)
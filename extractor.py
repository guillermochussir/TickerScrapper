import requests
import pandas as pd
import json

class Extractor:

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
        records = json.loads(self.request(pedido.url))
        records = records["records"]
        df = pd.DataFrame.from_records(records)
        if df is not None:
            print(str(len(df)) + ' fondos scrappeados')
            print ('exportando a funds.csv')
            df.to_csv('funds.csv', index=False)
        else:
            print ('error. df vacío')
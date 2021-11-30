'''
PROJETO INTEGRADOR DE ENGENHARIA DE COMPUTAÇÃO - UNIVESP - NOVEMBRO/2021

#Funcionalidade: Este aplicativo  abre campos para preenchimento e ao clicar no borão "Salvar", salva os dados preenchidos em um banco de dados na nuvem, o "Firebase" da Google.

Para montagem do aplicativo, foi utilizada a biblioteca "Kivy".
Dentro da biblioteca Kivy, foi utilizada a "Kivy MD (Kivy Material Design", que possui ferramentas gráficas que facilitam a montagem de aplicativos.

Link para a biblioteca: https://kivy.org/#home
Link para a documentação: https://kivy.org/doc/stable/
'''


## Biblioteca Kivy para montagem da interface do aplicativo
from kivymd.app import MDApp


## Comunicação com o banco de dados via HTTPS
import requests
import os
import certifi

os.environ["SSS_CERT_FILE"] = certifi.where()

## Código
class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette =  'Purple'

    def on_start(self):
        pass


    def lancar_novo(self, vencimento, credor, descricao, parcela, valor):
        dados = f'{{"vencimento": "{vencimento}", "credor": "{credor}", "descricao": "{descricao}", "numero_parcela": "{parcela}", "valor": "{valor}"}}'

        requests.post(f"https://piunivespcontasapagar-default-rtdb.firebaseio.com/lancamentos.json", data=dados)


if __name__=="__main__":
    App().run()
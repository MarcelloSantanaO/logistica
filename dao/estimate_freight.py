import requests
import json
import xml.etree.ElementTree as ET
import re


class Pricing:
    def estimate_correios(self, cep_origem: str, cep_destino: str, peso: str, comprimento: float, altura: float, largura: float, diametro: float) -> dict:
        list_calc = []
        final_result = {'Code': '', 'Value': 5000, 'Time': ''}
        cod = [{'name': 'pac', 'code': '04510'}, {'name': 'sedex', 'code': '04014'}]
        for code in cod:
            request = requests.get( url="http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo",
            params={'nCdEmpresa': '', 'sDsSenha': '','nCdServico': code['code'], 'sCepOrigem':cep_origem,
                'sCepDestino': cep_destino, 'nVlPeso': peso,'nCdFormato': 1,'nVlComprimento': comprimento,
                'nVlAltura': altura,'nVlLargura': largura, 'nVlDiametro': diametro, 'sCdMaoPropria': 'N', 'nVlValorDeclarado': 0,
                'sCdAvisoRecebimento': 'N'
                    })
            tree =  ET.ElementTree(ET.fromstring(request.content))
            filtro = "*"
            valor = 0
            prazo = ''
            root = tree.getroot()
            for child in root.iter(filtro):
                if child.tag == '{http://tempuri.org/}Valor':
                    valor = float(re.sub(',','.', child.text))
                if child.tag == '{http://tempuri.org/}PrazoEntrega':
                    prazo = child.text
            dicionario = {'Time': prazo, 'Value': valor, 'Code': code['name']}
            list_calc.append(dicionario)
            newlist = sorted(list_calc, key=lambda k: k['Value'])
        return newlist[0]

import csv
import numpy as np


class InmetConverter:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def gerar_temperaturas(self):
        with open(self.arquivo, 'r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file, delimiter=';')
            linhas_arquivo = list(reader)

        total_linhas = 9 + (365 * 24)
        temperaturas = np.zeros((365, 24))
        j = 0
        k = 0
        x = 8

        for i in range(9, total_linhas - 2):
            if k == 23:
                j += 1
                k = -1
                x = 8

            if 10 <= k <= 23:
                colunas = linhas_arquivo[i]
                if len(colunas) > 7 and colunas[7]:
                    temperaturas[j][x] = float(colunas[7].replace(',', '.'))
                x += 1
            k += 1

        return temperaturas

    def gerar_radiacao_solar(self):
        with open(self.arquivo, 'r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file, delimiter=';')
            linhas_arquivo = list(reader)

        total_linhas = 9 + (365 * 24)
        radiacao_solar = np.zeros((365, 24))
        j = 0
        k = 0
        x = 0

        for i in range(9, total_linhas):
            if k == 23:
                j += 1
                k = -1
                x = 0

            k += 1
            if k < 10 or k > 23:
                continue

            colunas = linhas_arquivo[i]

            if len(colunas) > 6 and colunas[6]:
                valorStr = colunas[6].replace(',', '.')
                if valorStr == '':
                    radiacao_solar[j][x] = 0
                else:
                    radiacao_solar[j][x] = float(valorStr)

            x += 1

        return radiacao_solar




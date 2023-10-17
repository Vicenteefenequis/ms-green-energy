import math
from math import exp

import numpy as np

from core_apps.energy_converter.funcoes.Funcao import gama, cosd, sind, acosd, et, temp_celula, gerar_horas_oficiais, \
    deltad
from core_apps.energy_converter.logic.coeficiente_perez import CoeficientePerez


def transformar_dados_em_24_horas(matriz):
    n_linhas = 365
    n_colunas = 24
    dados_24_horas = [[0.0] * n_colunas for _ in range(n_linhas)]

    for i in range(n_linhas):
        for j in range(len(matriz[i])):
            dados_24_horas[i][j + 6] = matriz[i][j]

    return dados_24_horas


def gerarPotenciaSaida(k0, k1, k2, pfv):
    pSaida = np.zeros(pfv.shape)
    for i in range(len(pfv)):
        for j in range(len(pfv[i])):
            potencia = np.roots([k2, 1 + k1, k0 - pfv[i][j]])
            pSaida[i][j] = max(potencia)
    return pSaida


class GeradorPotenciaFotovoltaico:

    def __init__(self, temperaturas, radSolarHoriz, parametrosFotovoltaico):
        self.temperaturas = temperaturas
        self.radSolarHoriz = radSolarHoriz
        self.parametrosArranjoFotovoltaico = parametrosFotovoltaico.parametros_arranjo_fotovoltaico
        self.orienAzimutal = parametrosFotovoltaico.orien_azimutal
        self.inclinacao = parametrosFotovoltaico.inclinacao
        self.latLocal = parametrosFotovoltaico.lat_local
        self.longLocal = parametrosFotovoltaico.long_local
        self.longPadrao = parametrosFotovoltaico.long_padrao
        self.altLocal = parametrosFotovoltaico.alt_local
        self.constSolar = parametrosFotovoltaico.const_solar
        self.albedo = parametrosFotovoltaico.albedo

    def gerar(self):
        teta = np.zeros((365, 14))
        tetaz = np.zeros((365, 14))
        i0 = np.zeros((365, 14))
        kt = np.zeros((365, 14))
        kd = np.zeros((365, 14))
        e = np.zeros((365, 14))
        e0 = np.zeros((365, 14))
        f1 = np.zeros((365, 14))
        f2 = np.zeros((365, 14))
        a = np.zeros((365, 14))
        b = np.zeros((365, 14))
        rdh = np.zeros((365, 14))
        rbh = np.zeros((365, 14))
        iginc = np.zeros((365, 14))
        ibinc = np.zeros((365, 14))
        am = np.zeros((365, 14))
        delta = np.zeros((365, 14))
        in_ = np.zeros((365, 14))
        is_ = np.zeros((365, 14))
        ir = np.zeros((365, 14))
        horasOficiais = gerar_horas_oficiais(6, 19)
        for i in range(365):
            for j in range(14):
                diaAno = i + 1
                horaSolar = (horasOficiais[j] + (4 * (self.longPadrao - self.longLocal) + et(i + 1))) / 60
                omega = (horaSolar - 12) * 15

                # Calcula o ângulo de incidência para superfícies inclinadas e orientadas em qualquer direção
                teta[i][j] = acosd(((sind(self.latLocal) * cosd(self.inclinacao)) - (
                        cosd(self.latLocal) * sind(self.inclinacao) * cosd(self.orienAzimutal))) * sind(
                    delta[i][j]) +
                                   (((cosd(self.latLocal) * cosd(self.inclinacao)) + (
                                           sind(self.latLocal) * sind(self.inclinacao) * cosd(
                                       self.orienAzimutal))) * cosd(deltad(diaAno)) * cosd(omega)) +
                                   (cosd(deltad(diaAno)) * sind(self.inclinacao) * sind(self.orienAzimutal) * sind(
                                       omega)))

                # Calcula o ângulo de incidência em superfícies horizontais
                tetaz[i][j] = acosd(
                    sind(deltad(i)) * sind(self.latLocal) + cosd(deltad(i)) * cosd(self.latLocal) * cosd(omega))

                # Calcula o fator de correção de excentricidade da órbita terrestre
                e0[i][j] = 1.000110 + 0.034221 * cosd(gama(i)) + 0.001280 * sind(gama(i)) + 0.000719 * cosd(
                    2 * gama(i)) + 0.000077 * sind(2 * gama(i))

                # Calcula a irradiação solar extraterrestre ao longo do ano
                i0[i][j] = self.constSolar * e0[i][j] * cosd(tetaz[i][j])
                i0[i][j] = max(i0[i][j], 0)

                # Modelo de Erbs e outros
                # Cálculo do índice de claridade (kt)
                if i0[i][j] == 0:
                    kt[i][j] = 0
                else:
                    kt[i][j] = self.radSolarHoriz[i][j] / i0[i][j]

                # Cálculo do kd
                if kt[i][j] <= 0.22:
                    kd[i][j] = 1.0 - 0.09 * kt[i][j]
                elif kt[i][j] <= 0.80:
                    kd[i][j] = 0.9511 - 0.1604 * kt[i][j] + 4.388 * (pow(kt[i][j], 2)) - 16.638 * pow(kt[i][j],
                                                                                                      3) + 12.336 * pow(
                        kt[i][j], 4)
                else:
                    kd[i][j] = 0.165

                    # Calcula a parcela de radiação difusa no plano horizontal
                rdh[i][j] = self.radSolarHoriz[i][j] * kd[i][j]

                # Calcula a parcela de radiação direta no plano horizontal
                rbh[i][j] = self.radSolarHoriz[i][j] - rdh[i][j]

                # Calcula a irradiação direta incidente em uma superfície inclinada
                ibinc[i][j] = rbh[i][j] * (cosd(teta[i][j]) / cosd(tetaz[i][j]))
                ibinc[i][j] = max(ibinc[i][j], 0)
                if ibinc[i][j] > i0[i][j]:
                    ibinc[i][j] = i0[i][j]

                # Calcula a massa de ar relativa
                am[i][j] = exp(-0.0001184 * self.altLocal) / (
                        cosd(tetaz[i][j]) + 0.5057 * pow(96.08 - tetaz[i][j], -1.634))
                am[i][j] = max(am[i][j], 0)

                # Calcula o índice de brilho do céu
                if i0[i][j] == 0:
                    delta[i][j] = 0
                else:
                    delta[i][j] = (rdh[i][j] * am[i][j]) / i0[i][j]
                if delta[i][j] > 1:
                    delta[i][j] = 1

                # Calcula o índice de claridade
                in_[i][j] = rbh[i][j] / cosd(tetaz[i][j])
                e[i][j] = (((rdh[i][j] + in_[i][j]) / rdh[i][j]) + 1.041 * pow((tetaz[i][j] * math.pi / 180),
                                                                               3)) / (
                                  1 + 1.041 * pow((tetaz[i][j] * math.pi / 180), 3))
                e[i][j] = max(e[i][j], 0)

                if e[i][j] <= 1.065:
                    e[i][j] = 1
                elif e[i][j] <= 1.23:
                    e[i][j] = 2
                elif e[i][j] <= 1.5:
                    e[i][j] = 3
                elif e[i][j] <= 1.95:
                    e[i][j] = 4
                elif e[i][j] <= 2.80:
                    e[i][j] = 5
                elif e[i][j] <= 4.50:
                    e[i][j] = 6
                elif e[i][j] <= 6.20:
                    e[i][j] = 7
                else:
                    e[i][j] = 8

                iPerez = int(e[i][j]) - 1
                f1[i][j] = CoeficientePerez.COEFIC_PEREZ[iPerez][0] + CoeficientePerez.COEFIC_PEREZ[iPerez][1] * \
                           delta[i][j] + CoeficientePerez.COEFIC_PEREZ[iPerez][2] * tetaz[i][j] * math.pi / 180
                f2[i][j] = CoeficientePerez.COEFIC_PEREZ[iPerez][3] + CoeficientePerez.COEFIC_PEREZ[iPerez][4] * \
                           delta[i][j] + CoeficientePerez.COEFIC_PEREZ[iPerez][5] * tetaz[i][j] * math.pi / 180
                a[i][j] = max(0, cosd(teta[i][j]))
                b[i][j] = max(cosd(85), cosd(tetaz[i][j]))

                # Calcula a irradiação solar difusa no plano inclinado e orientado em qualquer direção
                is_[i][j] = rdh[i][j] * (
                        0.5 * (1 + cosd(self.inclinacao)) * (1 - f1[i][j]) + f1[i][j] * (a[i][j] / b[i][j]) +
                        f2[i][j] * sind(-self.inclinacao))

                # Calcula a irradiação solar de albedo no plano inclinado e orientado em qualquer direção
                ir[i][j] = 0.5 * (self.radSolarHoriz[i][j] * self.albedo * (1 - cosd(self.inclinacao)))

                # Calcula a irradiação solar global no plano inclinado e orientado em qualquer direção
                iginc[i][j] = is_[i][j] + ir[i][j] + ibinc[i][j]
        igincFull = transformar_dados_em_24_horas(iginc)
        tempsCelula = self.calcularTempCelula(igincFull)
        pmp = self.calcularPotenciaMaximaFornecida(igincFull, tempsCelula)
        efSpmp = self.gerarEficienciaSeguidorMaximo(pmp)
        pfv = self.calcularPotenciaEntregueInversor(pmp, efSpmp)
        pfvNormalizado = self.calcularPotenciaEntregueInversorNormalizado(pfv)

        # Obter os parâmetros do inversor
        efInv100 = self.parametrosArranjoFotovoltaico.eficienInsersor100PorCento
        efInv50 = self.parametrosArranjoFotovoltaico.eficienInsersor50PorCento
        efInv10 = self.parametrosArranjoFotovoltaico.eficienInsersor10PorCento

        k0 = (1.0 / 9.0) * (1.0 / efInv100) - (1.0 / 4.0) * (1.0 / efInv50) + (5.0 / 36.0) * (1.0 / efInv10)
        k1 = -(4.0 / 3.0) * (1.0 / efInv100) + (33.0 / 12.0) * (1.0 / efInv50) - (5.0 / 12.0) * (
                1.0 / efInv10) - 1
        k2 = (20.0 / 9.0) * (1 / efInv100) - (5.0 / 2.0) * (1.0 / efInv50) + (5.0 / 18.0) * (1.0 / efInv10)

        # Resolva a equação do segundo grau para obter pSaida
        pSaida = gerarPotenciaSaida(k0, k1, k2, pfv)

        # Suponha que você tenha uma função para resolver a equação do segundo grau em pfvNormalizado

        # Retorna o resultado desejado
        return self.gerarPotenciaSaidaNominal(pfv, pSaida, k0)

    def calcularTempCelula(self, matriz):
        tempsCelula = np.zeros((365, 24))
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                tempsCelula[i][j] = temp_celula(self.temperaturas[i][j], matriz[i][j],
                                                self.parametrosArranjoFotovoltaico.tempNominalCelula)
        return tempsCelula

    def calcularPotenciaMaximaFornecida(self, igincFull, tempsCelula):
        potenciasMaximas = np.zeros((365, 24))
        for i in range(len(igincFull)):
            for j in range(len(igincFull[i])):
                potenciasMaximas[i][j] = self.parametrosArranjoFotovoltaico.potenNominalArranjo * \
                                         igincFull[i][
                                             j] / self.parametrosArranjoFotovoltaico.inrradianciaEnsaioPadrao * \
                                         (1 - self.parametrosArranjoFotovoltaico.coeficienteTempMaximaPotencia *
                                          (tempsCelula[i][
                                               j] - self.parametrosArranjoFotovoltaico.tempEnsaioPadrao))
        return potenciasMaximas

    def gerarEficienciaSeguidorMaximo(self, pmp):
        efSpmp = np.zeros((365, 24))
        for i in range(len(pmp)):
            for j in range(len(pmp[i])):
                if pmp[i][j] < 0.2 * self.parametrosArranjoFotovoltaico.potenNominalInversor:
                    efSpmp[i][j] = 0.85
                else:
                    efSpmp[i][j] = 0.98
        return efSpmp

    def calcularPotenciaEntregueInversor(self, pmp, efSpmp):
        pfv = pmp * efSpmp
        return pfv

    def calcularPotenciaEntregueInversorNormalizado(self, pfv):
        pfvNormalizado = pfv / self.parametrosArranjoFotovoltaico.potenNominalInversor
        return pfvNormalizado

    def gerarPotenciaSaidaNominal(self, pfv, pSaida, k0):
        pSaidaNominal = np.zeros(pfv.shape)
        potenNominalInversor = self.parametrosArranjoFotovoltaico.potenNominalInversor
        potenMaximaInversor = self.parametrosArranjoFotovoltaico.potenMaximaInversor

        for i in range(len(pSaida)):
            for j in range(len(pSaida[i])):
                pSaidaNominal[i][j] = pSaida[i][j] * potenNominalInversor
                if pSaidaNominal[i][j] >= potenMaximaInversor:
                    pSaidaNominal[i][j] = potenMaximaInversor
                elif pfv[i][j] <= k0 * potenNominalInversor:
                    pSaidaNominal[i][j] = 0
                else:
                    pSaidaNominal[i][j] = pSaida[i][j] * potenNominalInversor
        return pSaidaNominal

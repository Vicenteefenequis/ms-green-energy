from core_apps.energy_converter.funcoes.Funcao import ceil_2d_array, div, mult
from core_apps.energy_converter.funcoes.inmet_converter import InmetConverter
from core_apps.energy_converter.logic.photovoltaic_potential_generator import GeradorPotenciaFotovoltaico
from core_apps.energy_converter.model.input_params import ParamsGeneral


def main():
    parametros_entrada = carregar_parametros_entrada()
    resultados_ano = []

    for dia in range(365):
        resultado_dia = geracao_energia(parametros_entrada, dia)
        resultados_ano.append(resultado_dia)

    print("Média anual:", calcular_media_anual_fotovoltaico(resultados_ano))


def calcular_media_anual_fotovoltaico(matrizGeracaoFotovoltaico):
    somaTotalFotovoltaico = 0
    totalDias = len(matrizGeracaoFotovoltaico)
    totalHoras = len(matrizGeracaoFotovoltaico[0])

    for dia in range(totalDias):
        for h in range(totalHoras):
            if matrizGeracaoFotovoltaico[dia][h] != 0:
                somaTotalFotovoltaico += matrizGeracaoFotovoltaico[dia][h]

    mediaAnualFotovoltaico = somaTotalFotovoltaico / 12

    return mediaAnualFotovoltaico


# Exemplo de uso:
# matrizGeracaoFotovoltaico = ...  # Alguma matriz 2D
# mediaFotovoltaico = calcular_media_anual_fotovoltaico(matrizGeracaoFotovoltaico)
# print("Média Anual Fotovoltaico:", mediaFotovoltaico


def geracao_energia(parametros_entrada, dia):
    parametros_fotovoltaico = parametros_entrada.parametros_fotovoltaico
    conversor_inmet = InmetConverter("csv/dados_meteorologicos.csv")
    temperaturas = conversor_inmet.gerar_temperaturas()
    radiacao_solar = conversor_inmet.gerar_radiacao_solar()
    div(radiacao_solar, 3.6)
    gerador = GeradorPotenciaFotovoltaico(temperaturas, radiacao_solar, parametros_fotovoltaico).gerar()
    print("DIA: " + str(dia) + " - " + str(gerador[dia]))
    mult(gerador, parametros_fotovoltaico.parametros_arranjo_fotovoltaico.areaM2)
    div(gerador, 1000)
    ceil_2d_array(gerador, 4)
    return gerador[dia]


def carregar_parametros_entrada():
    carregador_parametros_entrada = ParamsGeneral()
    return carregador_parametros_entrada.carregar_arquivo()


if __name__ == "__main__":
    main()

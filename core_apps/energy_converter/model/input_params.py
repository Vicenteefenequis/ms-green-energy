from core_apps.energy_converter.model.parametros_arranjo_fotovoltaico import ParametrosArranjoFotovoltaico
from core_apps.energy_converter.model.parametros_fotovoltaico import ParametrosFotovoltaico


class InputParams:
    def __init__(self, parametros_fotovoltaico, dia_ano_geracao_grafico):
        self.parametros_fotovoltaico = parametros_fotovoltaico
        self.dia_ano_geracao_grafico = dia_ano_geracao_grafico

    def get_parametros_fotovoltaico(self):
        return self.parametros_fotovoltaico

    def get_dia_ano_geracao_grafico(self):
        return self.dia_ano_geracao_grafico

    def __str__(self):
        return f"ParametrosEntrada{{parametros_fotovoltaico={self.parametros_fotovoltaico}, dia_ano_geracao_grafico={self.dia_ano_geracao_grafico}}}"


def _get_int(properties, nome_propriedade):
    if nome_propriedade in properties:
        return int(properties[nome_propriedade])
    return 0


class ParamsGeneral:
    def carregar_arquivo(self):
        properties = {
            "TemperaturaNominalCelula": 45,
            "PotenciaNominalArranjo": 380,
            "PotenciaNominalInversor": 380,
            "PotenciaMaximaInversor": 380,
            "IrrandianciaSolarEnsaioPadrao": 1000,
            "CoeficienteTemperaturaMaxima": -0.0041,
            "TemperaturaEnsaioPadrao": 25,
            "Eficiencia100PorCento": 0.978,
            "Eficiencia50PorCento": 0.982,
            "Eficiencia10PorCento": 0.973,
            "AreaM2": 60,
            "OrientecaoAzimutal": 38,
            "Inclinacao": 15,
            "LatitudeLocal": -13.309528,
            "LongitudeLocal": -49.117478,
            "LongitudePadrao": 45,
            "AltitudeLocal": 365,
            "ConstanteSolar": 1367,
            "Albedo": 0.35,
            "DiaAnoGeracaoGrafico": 259,
        }

        temp_nominal_celula = properties["TemperaturaNominalCelula"]
        poten_nominal_arranjo = properties["PotenciaNominalArranjo"]
        poten_nominal_inversor = properties["PotenciaNominalInversor"]
        poten_maxima_inversor = properties["PotenciaMaximaInversor"]
        inrradiancia_ensaio_padrao = properties["IrrandianciaSolarEnsaioPadrao"]
        coeficiente_temp_maxima_potencia = properties["CoeficienteTemperaturaMaxima"]
        temp_ensaio_padrao = properties["TemperaturaEnsaioPadrao"]
        eficien_inversor_100_por_cento = properties["Eficiencia100PorCento"]
        eficien_inversor_50_por_cento = properties["Eficiencia50PorCento"]
        eficien_inversor_10_por_cento = properties["Eficiencia10PorCento"]
        area_m2 = properties["AreaM2"]
        parametros_arranjo_fotovoltaico = ParametrosArranjoFotovoltaico(
            temp_nominal_celula,
            poten_nominal_arranjo,
            poten_nominal_inversor,
            poten_maxima_inversor,
            inrradiancia_ensaio_padrao,
            coeficiente_temp_maxima_potencia,
            temp_ensaio_padrao,
            eficien_inversor_100_por_cento,
            eficien_inversor_50_por_cento,
            eficien_inversor_10_por_cento,
            area_m2
        )

        orien_azimutal = properties["OrientecaoAzimutal"]
        inclinacao = properties["Inclinacao"]
        lat_local = properties["LatitudeLocal"]
        long_local = properties["LongitudeLocal"]
        long_padrao = properties["LongitudePadrao"]
        alt_local = properties["AltitudeLocal"]
        const_solar = properties["ConstanteSolar"]
        albedo = properties["Albedo"]
        parametros_fotovoltaico = ParametrosFotovoltaico(
            orien_azimutal,
            inclinacao,
            lat_local,
            long_local,
            long_padrao,
            alt_local,
            const_solar,
            albedo,
            parametros_arranjo_fotovoltaico
        )

        return InputParams(parametros_fotovoltaico, dia_ano_geracao_grafico=properties["DiaAnoGeracaoGrafico"])

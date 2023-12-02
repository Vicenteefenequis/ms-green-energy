class ParametrosFotovoltaico:
    def __init__(self, orien_azimutal, inclinacao, lat_local, long_local, long_padrao, alt_local, const_solar, albedo, parametros_arranjo_fotovoltaico):
        self.orien_azimutal = orien_azimutal
        self.inclinacao = inclinacao
        self.lat_local = lat_local
        self.long_local = long_local
        self.long_padrao = long_padrao
        self.alt_local = alt_local
        self.const_solar = const_solar
        self.albedo = albedo
        self.parametros_arranjo_fotovoltaico = parametros_arranjo_fotovoltaico

    def __str__(self):
        return f"ParametrosFotovoltaico{{orien_azimutal={self.orien_azimutal}, inclinacao={self.inclinacao}, lat_local={self.lat_local}, long_local={self.long_local}, long_padrao={self.long_padrao}, alt_local={self.alt_local}, const_solar={self.const_solar}, albedo={self.albedo}, parametros_arranjo_fotovoltaico={self.parametros_arranjo_fotovoltaico}}}"

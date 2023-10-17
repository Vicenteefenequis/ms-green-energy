class ParametrosArranjoFotovoltaico:
    def __init__(self, tempNominalCelula, potenNominalArranjo, potenNominalInversor,
                 potenMaximaInversor, inrradianciaEnsaioPadrao, coeficienteTempMaximaPotencia,
                 tempEnsaioPadrao, eficienInsersor100PorCento, eficienInsersor50PorCento,
                 eficienInsersor10PorCento, areaM2):
        self.tempNominalCelula = tempNominalCelula
        self.potenNominalArranjo = potenNominalArranjo
        self.potenNominalInversor = potenNominalInversor
        self.potenMaximaInversor = potenMaximaInversor
        self.inrradianciaEnsaioPadrao = inrradianciaEnsaioPadrao
        self.coeficienteTempMaximaPotencia = coeficienteTempMaximaPotencia
        self.tempEnsaioPadrao = tempEnsaioPadrao
        self.eficienInsersor100PorCento = eficienInsersor100PorCento
        self.eficienInsersor50PorCento = eficienInsersor50PorCento
        self.eficienInsersor10PorCento = eficienInsersor10PorCento
        self.areaM2 = areaM2

    def __str__(self):
        return (f"ParametrosArranjoFotovoltaico{{"
                f"tempNominalCelula={self.tempNominalCelula}, "
                f"potenNominalArranjo={self.potenNominalArranjo}, "
                f"potenNominalInversor={self.potenNominalInversor}, "
                f"potenMaximaInversor={self.potenMaximaInversor}, "
                f"inrradianciaEnsaioPadrao={self.inrradianciaEnsaioPadrao}, "
                f"coeficienteTempMaximaPotencia={self.coeficienteTempMaximaPotencia}, "
                f"tempEnsaioPadrao={self.tempEnsaioPadrao}, "
                f"eficienInsersor100PorCento={self.eficienInsersor100PorCento}, "
                f"eficienInsersor50PorCento={self.eficienInsersor50PorCento}, "
                f"eficienInsersor10PorCento={self.eficienInsersor10PorCento}")

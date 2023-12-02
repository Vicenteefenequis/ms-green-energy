def calculate_indicators(locations, average_photovoltaic=0):
    calculator = IndicatorCalculator(locations, average_photovoltaic)
    return Indicator.to_response(calculator)


class IndicatorCalculator:

    def __init__(self, projects, average_photovoltaic=0):
        self.projects = projects
        self.average_photovoltaic = average_photovoltaic

    def calculate_average(self, data):
        return sum(item['value'] for item in data) / len(data)

    def residential_electricity_per_capita(self):
        return [{
            "location_name": project.location.name,
            "is_certified": project.is_certified,
            "value": (project.data_energetic.total_residential_electricity_use + (0 if project.is_certified else self.average_photovoltaic)) / project.location.population
        } for project in self.projects]

    def percentage_habitants_with_regular_connection(self):
        return [{
            "location_name": project.location.name,
            "is_certified": project.is_certified,
            "value": (project.data_energetic.number_of_people_with_regular_connection / project.location.population) * 100
        } for project in self.projects]

    def electricity_consumption_in_public_buildings(self):
        return [{
            "location_name": project.location.name,
            "is_certified": project.is_certified,
            "value": (project.data_energetic.total_electricity_consumption_in_public_buildings + (0 if project.is_certified else self.average_photovoltaic)) / project.data_energetic.total_area_of_these_buildings
        } for project in self.projects]

    def percentage_of_renewable_energy(self):
        return [{
            "location_name": project.location.name,
            "is_certified": project.is_certified,
            "value": (
                (project.data_energetic.total_electricity_consumption_produced_from_renewable + (0 if project.is_certified else self.average_photovoltaic)) / project.data_energetic.total_energy_consumption) * 100
        } for project in self.projects]

    def total_electricity_per_capita(self):
        return [{
            "location_name": project.location.name,
            "is_certified": project.is_certified,
            "value": (project.data_energetic.total_electricity_use + (0 if project.is_certified else self.average_photovoltaic)) / project.location.population
        } for project in self.projects]

    def average_interruptions_energy_consumer(self):
        return [{
            "location_name": project.location.name,
            "is_certified": project.is_certified,
            "value": project.data_energetic.total_number_of_interruptions / project.data_energetic.total_number_of_consumers_served
        } for project in self.projects]

    def duration_average_interruptions_energy(self):
        return [{
            "location_name": project.location.name,
            "is_certified": project.is_certified,
            "value": project.data_energetic.sum_of_the_duration_of_all_interruptions / project.data_energetic.total_number_of_interruptions
        } for project in self.projects]


class Indicator:
    @staticmethod
    def to_response(calculator):
        return [
            {
                "name": "Uso de energia elétrica residencial per capita",
                "unit": "kWh/ano",
                "data": calculator.residential_electricity_per_capita(),
                "average": calculator.calculate_average(calculator.residential_electricity_per_capita())
            },
            {
                "name": "Porcentagem de habitantes da cidade com fornecimento regular de energia elétrica",
                "unit": "%",
                "data": calculator.percentage_habitants_with_regular_connection(),
                "average": calculator.calculate_average(calculator.percentage_habitants_with_regular_connection())
            },
            {
                "name": "Consumo de energia de edificios publicos por ano(kWh/m2)",
                "unit": "kWh/m2",
                "data": calculator.electricity_consumption_in_public_buildings(),
                "average": calculator.calculate_average(calculator.electricity_consumption_in_public_buildings())
            },
            {
                "name": "Porcentagem de energia total proveniente de fontes renováveis, como parte do consumo total da energia da cidade",
                "unit": "%",
                "data": calculator.percentage_of_renewable_energy(),
                "average": calculator.calculate_average(calculator.percentage_of_renewable_energy())
            },
            {
                "name": "Uso total de energia elétrica per capita(kWh/ano)",
                "unit": "kWh/ano",
                "data": calculator.total_electricity_per_capita(),
                "average": calculator.calculate_average(calculator.total_electricity_per_capita())
            },
            {
                "name": "Número médio de interrupções de energia elétrica por consumidor por ano",
                "unit": "número",
                "data": calculator.average_interruptions_energy_consumer(),
                "average": calculator.calculate_average(calculator.average_interruptions_energy_consumer())
            },
            {
                "name": "Duração média das interrupções de energia elétrica (em horas)",
                "unit": "número",
                "data": calculator.duration_average_interruptions_energy(),
                "average": calculator.calculate_average(calculator.duration_average_interruptions_energy())
            },
        ]

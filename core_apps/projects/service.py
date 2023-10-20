
class IndicatorCalculator:

    def __init__(self, projects):
        self.projects = projects

    def calculate_average(self, data):
        return sum(item['value'] for item in data) / len(data)

    def residential_electricity_per_capita(self):
        return [{
            "id": project.id,
            "city": project.location.name,
            "value": project.data_energetic.total_residential_electricity_use / project.location.population
        } for project in self.projects]

    def percentage_habitants_with_regular_connection(self):
        return [{
            "id": project.id,
            "city": project.location.name,
            "value": (project.data_energetic.number_of_people_with_regular_connection / project.location.population) * 100
        } for project in self.projects]

    def electricity_consumption_in_public_buildings(self):
        return [{
            "id": project.id,
            "city": project.location.name,
            "value": project.data_energetic.total_electricity_consumption_in_public_buildings / project.data_energetic.total_area_of_these_buildings
        } for project in self.projects]

    def percentage_of_renewable_energy(self):
        return [{
            "id": project.id,
            "city": project.location.name,
            "value": (project.data_energetic.total_electricity_consumption_produced_from_renewable / project.data_energetic.total_energy_consumption) * 100
        } for project in self.projects]

    def total_electricity_per_capita(self):
        return [{
            "id": project.id,
            "city": project.location.name,
            "value": project.data_energetic.total_electricity_use / project.location.population
        } for project in self.projects]

    def average_interruptions_energy_consumer(self):
        return [{
            "id": project.id,
            "city": project.location.name,
            "value": project.data_energetic.total_number_of_interruptions / project.data_energetic.total_number_of_consumers_served
        } for project in self.projects]

    def duration_average_interruptions_energy(self):
        return [{
            "id": project.id,
            "city": project.location.name,
            "value": project.data_energetic.sum_of_the_duration_of_all_interruptions / project.data_energetic.total_number_of_interruptions
        } for project in self.projects]

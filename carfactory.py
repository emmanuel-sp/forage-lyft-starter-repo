from car import Car
from engine import *
from battery import *


class CarFactory:
    def __init__(self):
        pass
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))
    def create_glissade(self ,current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))
    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
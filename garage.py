from vehicle import Vehicle


class Garage:
    def __init__(self):
        self._vehicles: list[Vehicle] = []

    @property
    def vehicles(self) -> list[Vehicle]:
        return list(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def empty_garage(self) -> None:
        self._vehicles.clear()

    def sort_by_release_year(self) -> None:
        self._vehicles.sort()
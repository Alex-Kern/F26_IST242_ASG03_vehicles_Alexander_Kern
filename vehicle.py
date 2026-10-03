from abc import ABC, abstractmethod
from manufacturer import Manufacturer
from auto_model import AutoModel


class Vehicle(ABC):
    def __init__(self, manufacturer: Manufacturer, model: AutoModel, mpg: float):
        self._manufacturer = manufacturer
        self._model = model
        self._mpg = float(mpg)

    @property
    def manufacturer(self) -> Manufacturer:
        return self._manufacturer

    @property
    def model(self) -> AutoModel:
        return self._model

    @property
    def mpg(self) -> float:
        return self._mpg

    @property
    def release_year(self) -> int:
        return self._model.years[0]

    @abstractmethod
    def number_of_wheels(self) -> int:
        pass

    def how_far_with(self, num_of_gallons: int) -> float:
        return float(self._mpg * num_of_gallons)
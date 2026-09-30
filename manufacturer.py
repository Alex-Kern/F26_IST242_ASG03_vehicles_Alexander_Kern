class Manufacturer:
    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country

    @property
    def name(self) -> str:
        return self._name

    @property
    def country(self) -> str:
        return self._country
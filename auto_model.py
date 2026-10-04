class AutoModel:
    def __init__(self, name: str, in_production: bool, years: list[int]):
        if not years:
            raise ValueError("The years list cannot be empty.")
        self._name = name
        self._in_production = in_production
        self._years = list(years)

    @property
    def name(self) -> str:
        return self._name

    @property
    def in_production(self) -> bool:
        return self._in_production

    @property
    def years(self) -> list[int]:
        return self._years.copy()  

    @property
    def first_year(self) -> int:
        return self._years[0]  

    def __str__(self) -> str:
        return f"{self._name} in production = {self._in_production}, release year: {self._years[0]}"
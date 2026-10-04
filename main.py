from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
from truck import Truck
from garage import Garage


def main():
    # 1. Instantiate the 4 vehicles
    ford = Manufacturer("Ford", "USA")
    f150_model = AutoModel("F150", True, [2020, 2021, 2022])
    f150 = Truck(ford, f150_model, 20.0, is_dually=False)

    honda = Manufacturer("Honda", "Japan")
    civic_model = AutoModel("Civic", False, [1996, 1997, 1998])
    civic = Sedan(honda, civic_model, 28.0)

    bmw = Manufacturer("BMW", "Germany")
    m3_model = AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018])
    m3 = Sedan(bmw, m3_model, 30.0)

    toyota = Manufacturer("Toyota", "Japan")
    tundra_model = AutoModel("Tundra", False, [1987, 1988])
    tundra = Truck(toyota, tundra_model, 30.0, is_dually=True)

    # 2. Add vehicles to the garage
    g = Garage()
    g.add_vehicle(f150)
    g.add_vehicle(civic)
    g.add_vehicle(m3)
    g.add_vehicle(tundra)

    # 3. Print before sorting
    print("Before sorting:")
    print(g)
    print()

    # 4. Sort and print after sorting
    g.sort_by_release_year()
    print("After sorting:")
    print(g)


if __name__ == "__main__":
    main()
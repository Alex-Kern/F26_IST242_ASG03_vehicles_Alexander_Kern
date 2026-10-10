import pytest
from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
from truck import Truck
from garage import Garage


def test_vehicle_range_and_wheels():
    """Verify fuel travel calculation and wheel configuration between types."""
    mfg_subaru = Manufacturer("Subaru", "Japan")
    outback_model = AutoModel("Outback", True, [2018, 2019, 2020])
    sedan = Sedan(mfg_subaru, outback_model, 26.5)

    mfg_ram = Manufacturer("RAM", "USA")
    ram_model = AutoModel("3500", True, [2021, 2022])
    dually_truck = Truck(mfg_ram, ram_model, 14.0, is_dually=True)

    # Validate range calculation (mpg * gallons)
    assert sedan.how_far_with(10) == pytest.approx(265.0)
    assert dually_truck.how_far_with(20) == pytest.approx(280.0)

    # Validate wheel counts
    assert sedan.number_of_wheels() == 4
    assert dually_truck.number_of_wheels() == 6


def test_garage_encapsulation_and_sorting():
    """Verify that garage list cannot be mutated externally and sorts properly."""
    mfg = Manufacturer("Chevrolet", "USA")
    older_model = AutoModel("Impala", False, [1967, 1968])
    newer_model = AutoModel("Silverado", True, [2022, 2023])

    older_sedan = Sedan(mfg, older_model, 15.0)
    newer_truck = Truck(mfg, newer_model, 18.0)

    garage = Garage()
    garage.add_vehicle(newer_truck)
    garage.add_vehicle(older_sedan)

    # Check encapsulation: mutating the returned copy should not modify the garage
    external_list = garage.vehicles
    external_list.clear()
    assert len(garage.vehicles) == 2

    # Check sort order by release year (1967 before 2022)
    garage.sort_by_release_year()
    sorted_vehicles = garage.vehicles
    assert sorted_vehicles[0].release_year == 1967 
    assert sorted_vehicles[1].release_year == 2022
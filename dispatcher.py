"""Dispatcher for the simulation"""

from typing import Optional, List
from driver import Driver
from rider import Rider


def _fastest_driver(drivers: List[Driver], rider: Rider) -> Optional[Driver]:
    """Returns the driver who can reach rider's destination the fastest."""

    fastest_time = 100 * 100
    best_driver = None

    for dr in drivers:
        curr_time = dr.get_travel_time(rider.origin)
        if curr_time < fastest_time:
            fastest_time = curr_time
            best_driver = dr
    return best_driver


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """
    _driving_fleet: List[Driver]  # registry of all drivers
    _available_drivers: List[Driver]
    _rider_wait_list: List[Rider]

    def __init__(self) -> None:
        """Initialize a Dispatcher."""
        self._driving_fleet = []
        self._available_drivers = []
        self._rider_wait_list = []

    def __str__(self) -> str:
        """Return a string representation."""
        return "=== 148 DISPATCHER SERVICE ==="

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        assigned_driver = _fastest_driver(self._available_drivers, rider)

        if assigned_driver is not None:
            self._available_drivers.remove(assigned_driver)
            return assigned_driver
        self._rider_wait_list.append(rider)
        return None

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver.requests == 0:  # new driver
            self._driving_fleet.append(driver)
        driver.requests += 1
        self._available_drivers.append(driver)  # available once requests

        if self._rider_wait_list:  # if not empty
            # longest waiting
            self._rider_wait_list.sort(key=lambda x: x.timestamp)
            assigned_rider = self._rider_wait_list.pop(0)
            self._available_drivers.remove(driver)
            return assigned_rider
        return None

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider."""
        if rider in self._rider_wait_list:
            self._rider_wait_list.remove(rider)
        rider.set_status('c')

    # # added
    # def add_driver(self, driver: Driver) -> None:
    #     """Add new driver to driving fleet."""
    #     self._driving_fleet.append(driver)
    #
    # def load_available_drivers(self) -> None:
    #     """Load available drivers."""
    #     for d in filter(lambda x: x.is_idle is True, self._driving_fleet):
    #         self._available_drivers.append(d)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})

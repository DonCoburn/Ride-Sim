"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""

from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    """A rider for a ride-sharing service.

    """
    identifier: str
    patience: int
    origin: Location
    destination: Location

    status: str
    timestamp: int

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.identifier = identifier
        self.patience = patience
        self.origin = origin
        self.destination = destination

        self.status = WAITING
        self.timestamp = 0

    def __str__(self) -> str:
        """Return a string representation of the rider."""
        return "Rider: {}".format(self.identifier)

    # added
    def set_status(self, option: str) -> None:
        """Set the status of the rider."""

        if option == 'c':
            self.status = CANCELLED
        elif option == 's':
            self.status = SATISFIED

    def set_time_stamp(self, time: int) -> None:
        """Records the time at which the rider starts waiting."""
        self.timestamp = time


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['location']})

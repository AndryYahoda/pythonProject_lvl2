from datetime import datetime


class Train:
    def __init__(self, destination: str, train_number: str, departure_time: str):
        """
        Initializes a Train object.
        :param destination: The destination of the train.
        :param train_number: The train number.
        :param departure_time: The departure time in 'YYYY-MM-DD HH:MM' format.
        """
        self._destination = destination
        self._train_number = train_number
        self._departure_time = departure_time
        self._validate_departure_time()

    def _validate_departure_time(self) -> None:
        """
        Validates that the departure time is not in the past.
        :raises ValueError: If the departure time is less than the current time.
        """
        current_time = datetime.now()
        departure_time_converted = datetime.strptime(self._departure_time, "%Y-%m-%d %H:%M")
        if departure_time_converted < current_time:
            raise ValueError("Час відправлення не може бути меншим за поточний.")

    @property
    def destination(self) -> str:
        """Gets the destination of the train."""
        return self._destination

    @property
    def train_number(self) -> str:
        """Gets the train number."""
        return self._train_number

    @property
    def departure_time(self) -> str:
        """Gets the departure time of the train."""
        return self._departure_time

    def __str__(self) -> str:
        """
        Formats the string to display train information.
        :return: A description of the train.
        """
        return (f"Потяг №{self.train_number} рухається до міста {self.destination}, "
                f"відправлення: {self.departure_time}")


train = Train("Dnipro-Lviv", "123", "2024-11-11 13:00")
print(train)

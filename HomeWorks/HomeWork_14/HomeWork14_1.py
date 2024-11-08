from datetime import datetime
import re


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
        self._validate_train_number()
        self._validate_destination()

    def _validate_departure_time(self) -> None:
        """
        Validates that the departure time is not in the past.
        :raises ValueError: If the departure time is less than the current time.
        """
        current_time = datetime.now()
        departure_time_converted = datetime.strptime(self._departure_time, "%Y-%m-%d %H:%M")
        if departure_time_converted < current_time:
            raise ValueError("Час відправлення не може бути меншим за поточний.")

    def _validate_train_number(self):
        """
        Validates the train number.
        :param self._train_number: The train number to be validated.
        :raises ValueError: If the train number is not in the correct format or out of the range.
        """
        if not re.fullmatch(r'\d{1,3}', self._train_number) or not (1 <= int(self._train_number) <= 999):
            raise ValueError("Номер поїзда має бути числом від 001 до 999.")
        if len(self._train_number) != 3:
            raise ValueError("Номер поїзда має бути у форматі трьох цифр, наприклад 001, 099 або 345.")

    def _validate_destination(self):
        """
        Validates the destination of the train.
        :param self._destination: The destination of the train.
        :raises ValueError: If the destination is empty, contains invalid characters, or exceeds 30 characters.
        """
        if not self._destination.strip():
            raise ValueError("Destination cannot be empty.")
        if len(self._destination) > 30 or not all(char.isalpha() or char == '-' for char in self._destination):
            raise ValueError("Destination can only contain letters and hyphens, up to 30 characters.")



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


train = Train("Dnipro-Lviv", "001", "2024-11-11 13:00")
print(train)

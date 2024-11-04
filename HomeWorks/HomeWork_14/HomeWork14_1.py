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
        self._destination = None
        self._train_number = None
        self._departure_time = None
        self.set_destination(destination)
        self.set_train_number(train_number)
        self.set_departure_time(departure_time)
        self._validate_departure_time()

    def _validate_departure_time(self) -> None:
        """
        Validates that the departure time is not in the past.
        :raises ValueError: If the departure time is less than the current time.
        """
        current_time = datetime.now()
        departure_time_converted = datetime.strptime(self.get_departure_time(), "%Y-%m-%d %H:%M")
        if departure_time_converted < current_time:
            raise ValueError("Час відправлення не може бути меншим за поточний.")

    def get_destination(self) -> str:
        """
        Gets the destination of the train.
        :return: The destination of the train.
        """
        return self._destination

    def get_train_number(self) -> str:
        """
        Gets the train number.
        :return: The train number.
        """
        return self._train_number

    def get_departure_time(self) -> str:
        """
        Gets the departure time of the train.
        :return: The departure time of the train.
        """
        return self._departure_time

    def set_destination(self, destination: str) -> None:
        """
        Sets the destination of the train.
        :param destination: The destination to set (string).
        """
        self._destination = destination

    def set_train_number(self, train_number: str) -> None:
        """
        Sets the train number.
        :param train_number: The train number to set (string).
        """
        self._train_number = train_number

    def set_departure_time(self, departure_time: str) -> None:
        """
        Sets the departure time of the train.
        :param departure_time: The departure time to set in 'YYYY-MM-DD HH:MM' format (string).
        :raises ValueError: If the format of departure time is incorrect.
        """
        datetime_regex = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$"
        if re.match(datetime_regex, departure_time):
            self._departure_time = departure_time
        else:
            raise ValueError("Incorrect format")

    def __str__(self) -> str:
        """
        Formats the string to display train information.
        :return: A description of the train.
        """
        return (f"Потяг №{self.get_train_number()} рухається до міста {self.get_destination()}, "
                f"відправлення: {self.get_departure_time()}")


train = Train("Dnipro-Lviv", "123", "2024-11-11 13:00")
print(train)

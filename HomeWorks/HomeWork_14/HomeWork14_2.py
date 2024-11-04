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
        departure_time_converted = datetime.strptime(self.departure_time, "%Y-%m-%d %H:%M")
        if departure_time_converted < current_time:
            raise ValueError("Час відправлення не може бути меншим за поточний.")

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def train_number(self) -> str:
        return self._train_number

    @property
    def departure_time(self) -> str:
        return self._departure_time

    def set_destination(self, destination: str) -> None:
        self._destination = destination

    def set_train_number(self, train_number: str) -> None:
        self._train_number = train_number

    def set_departure_time(self, departure_time: str) -> None:
        datetime_regex = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$"
        if re.match(datetime_regex, departure_time):
            self._departure_time = departure_time
        else:
            raise ValueError("Incorrect format")

    def __str__(self) -> str:
        return f"Потяг №{self.train_number} рухається до міста {self.destination}, відправлення: {self.departure_time}"


def sort_trains_by_number(trains: list) -> list:
    return sorted(trains, key=lambda train: train.train_number)


def find_train_by_number(trains: list, number: str) -> list:
    result = [train for train in trains if train.train_number == number]
    return result if result else "Потяг із таким номером не знайдено."


trains = [
    Train("Львів", "123", "2024-11-10 13:00"),
    Train("Київ", "456", "2024-11-10 11:05"),
    Train("Одеса", "789", "2024-11-11 15:30"),
    Train("Харків", "234", "2024-11-09 21:45"),
    Train("Дніпро", "567", "2024-11-10 23:30"),
]

sorted_trains = sort_trains_by_number(trains)
print("Список потягів за номером:")
for train in sorted_trains:
    print(train)

search_number = input("Введіть номер потяга для пошуку (без №, лише цифри): ")
found_trains = find_train_by_number(trains, search_number)
if isinstance(found_trains, list):
    for train in found_trains:
        print(train)
else:
    print(found_trains)


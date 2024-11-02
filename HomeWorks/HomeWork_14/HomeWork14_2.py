from datetime import datetime, timedelta


class Train:
    def __init__(self, destination: str, train_number: str, departure_time: str):
        """
        Initializes a Train object.
        :param destination: The destination of the train.
        :param train_number: The train number.
        :param departure_time: The departure time in 'YYYY-MM-DD HH:MM' format.
        """
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time
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

    def __str__(self) -> str:
        """
        Formats the string to display train information.
        :return: A description of the train.
        """
        return f"Потяг №{self.train_number} рухається до міста {self.destination}, відправлення: {self.departure_time}"


def sort_trains_by_number(trains: list) -> list:
    """
    Sorts a list of Train objects by their train number.
    :param trains: A list of Train objects.
    :return: A sorted list of Train objects by train number.
    """
    return sorted(trains, key=lambda train: train.train_number)


def find_train_by_number(trains: list, number: str) -> list:
    """
    Finds a train by its number.
    :param trains: A list of Train objects.
    :param number: The train number to search for.
    :return: A list of Train objects matching the train number, or a message if not found.
    """
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

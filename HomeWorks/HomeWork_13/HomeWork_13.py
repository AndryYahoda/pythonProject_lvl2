class MobPhone:
    """Class to represent a mobile phone with brand, size, and price."""
    def __init__(self, brand: str, size_h: float, size_w: float, price: float):
        """
        Initialize the MobPhone instance.
        :param brand: The brand of the mobile phone.
        :param size_h: The height of the phone in centimeters.
        :param size_w: The width of the phone in centimeters.
        :param price: The price of the phone.
        """
        self.brand = brand
        self._size_h = None
        self._size_w = None
        self._price = None
        self.set_size_h(size_h)
        self.set_size_w(size_w)
        self.set_price(price)

    def get_size_h(self) -> float:
        """
        Get the height of the phone.
        :return: The height of the phone in centimeters.
        """
        return self._size_h

    def get_size_w(self) -> float:
        """
        Get the width of the phone.
        :return: The width of the phone in centimeters.
        """
        return self._size_w

    def get_price(self) -> float:
        """
        Get the price of the phone.
        :return: The price of the phone.
        """
        return self._price

    def set_size_h(self, size_h: float) -> None:
        """
        Set the height of the phone.
        :param size_h: The height to set in centimeters.
        :return: ValueError if the height is not in the range [6, 21].
        """

        if 6 <= size_h <= 21:
            self._size_h = size_h
        else:
            raise ValueError("Висота повинна бути в межах від 6 до 21 см")

    def set_size_w(self, size_w: float) -> None:
        """
        Set the width of the phone.
        :param size_w: The width to set in centimeters.
        :return: ValueError if the width is not in the range [4, 10].
        """

        if 4 <= size_w <= 10:
            self._size_w = size_w
        else:
            raise ValueError("Ширина повинна бути в межах від 4 до 10 см")

    def set_price(self, price: float) -> None:
        """
        Set the price of the phone.
        :param price: The price to set.
        :return: ValueError if the price is not greater than 0.
        """

        if price > 0:
            self._price = price
        else:
            raise ValueError("Ціна повинна бути більше 0")

    def getData(self) -> str:
        """
        Get a string representation of the phone's data.
        :return: A formatted string with the phone's brand, height, width, and price.
        """
        return (
            f"Бренд: {self.brand}, "
            f"Висота: {self.get_size_h()} см, "
            f"Ширина: {self.get_size_w()} см, "
            f"Ціна: ${self.get_price()}"
        )


phone1 = MobPhone("Samsung", 16, 8, 1000)
phone2 = MobPhone("Apple", 15, 7, 1200)

print(phone1.getData())
print(phone2.getData())


class MobPhone:
    def __init__(self, brand: str, size_h: float, size_w: float, price: float):
        self.brand = brand
        self._size_h = None
        self._size_w = None
        self._price = None
        self.set_size_h(size_h)
        self.set_size_w(size_w)
        self.set_price(price)

    def get_size_h(self) -> float:
        return self._size_h

    def get_size_w(self) -> float:
        return self._size_w

    def get_price(self) -> float:
        return self._price

    def set_size_h(self, size_h: float) -> None:
        if 6 <= size_h <= 21:
            self._size_h = size_h
        else:
            raise ValueError("Висота повинна бути в межах від 6 до 21 см")

    def set_size_w(self, size_w: float) -> None:
        if 4 <= size_w <= 10:
            self._size_w = size_w
        else:
            raise ValueError("Ширина повинна бути в межах від 4 до 10 см")

    def set_price(self, price: float) -> None:
        if price > 0:
            self._price = price
        else:
            raise ValueError("Ціна повинна бути більше 0")

    def getData(self) -> str:
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

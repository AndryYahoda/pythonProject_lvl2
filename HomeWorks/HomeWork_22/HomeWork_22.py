class Potion:
    def __init__(self, color: list[int], volume: int) -> None:
        """
        Initializes the Potion object.
        :param color: A list of three integers representing RGB intensity in the range [0, 255].
        :param volume: A non-negative integer indicating the volume of the potion.
        :raises ValueError: If the color or volume are incorrectly formatted.
        """
        if len(color) != 3 or not all(0 <= c <= 255 for c in color):
            raise ValueError("Color must be a list of three integers in the range [0, 255].")
        if not isinstance(volume, int) or volume < 0:
            raise ValueError("Volume must be a non-negative integer.")
        self.color = color
        self.volume = volume

    def mix(self, other):
        """
        Mixes the current potion with another potion and returns the resulting potion.
        :param other: Another potion object to mix with.
        :return: A new Potion object representing the mixed potion.
        :raises TypeError: If the other object is not a Potion.
        """
        if not isinstance(other, Potion):
            raise TypeError("Can only mix with another Potion.")

        new_volume = self.volume + other.volume

        if new_volume == 0:
            new_color = [0, 0, 0]
        else:
            new_color = [
                round((self.color[i] * self.volume + other.color[i] * other.volume) / new_volume)
                for i in range(3)
            ]

        return Potion(new_color, new_volume)


potio_piperis = Potion([255, 255, 255], 7)
potio_developing = Potion([51, 102, 51], 12)
new_potion = potio_piperis.mix(potio_developing)

print("New potion color:", new_potion.color)
print("New potion volume:", new_potion.volume)

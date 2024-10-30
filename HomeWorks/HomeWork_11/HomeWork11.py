class StudentRating:
    """Class to manage and analyze student ratings."""

    def __init__(self, ratings: list[int] = []):
        """Initialize the StudentRating instance with an optional list of ratings.

        Args:
            ratings (list[int], optional): A list of integer ratings. Defaults to an empty list.
        """
        self.ratings = ratings

    def get_ratings(self) -> list[int]:
        """Return the list of ratings.

        Returns:
            list[int]: The list of ratings.
        """
        return self.ratings

    def set_ratings(self, new_ratings: list[int]) -> None:
        """Set a new list of ratings.

        Args:
            new_ratings (list[int]): A new list of integer ratings.
        """
        self.ratings = new_ratings

    def add_rating(self, rating: int) -> None:
        """Add a single rating to the list of ratings.

        Args:
            rating (int): An integer rating to add.
        """
        self.ratings.append(rating)

    def max_rating(self) -> int:
        """Return the maximum rating, or None if no ratings are available.

        Returns:
            int: The maximum rating or None if no ratings exist.
        """
        return max(self.ratings, default=None)

    def min_rating(self) -> int:
        """Return the minimum rating, or None if no ratings are available.

        Returns:
            int: The minimum rating or None if no ratings exist.
        """
        return min(self.ratings, default=None)

    def average_rating(self) -> float:
        """Calculate and return the average rating, or None if no ratings are available.

        Returns:
            float: The average rating or None if no ratings exist.
        """
        return sum(self.ratings) / len(self.ratings) if self.ratings else None

    def count_above_average(self) -> int:
        """Count and return the number of ratings above the average rating.

        Returns:
            int: The count of ratings above the average.
        """
        avg = self.average_rating()
        return sum(1 for rating in self.ratings if rating > avg) if avg is not None else 0

    def count_below_average(self) -> int:
        """Count and return the number of ratings below the average rating.

        Returns:
            int: The count of ratings below the average.
        """
        avg = self.average_rating()
        return sum(1 for rating in self.ratings if rating < avg) if avg is not None else 0

    def count_excellent(self) -> int:
        """Count and return the number of ratings in the 'excellent' category (91-100).

        Returns:
            int: The count of 'excellent' ratings.
        """
        return sum(1 for rating in self.ratings if 91 <= rating <= 100)

    def count_very_good(self) -> int:
        """Count and return the number of ratings in the 'very good' category (71-90).

        Returns:
            int: The count of 'very good' ratings.
        """
        return sum(1 for rating in self.ratings if 71 <= rating <= 90)

    def count_good(self) -> int:
        """Count and return the number of ratings in the 'good' category (60-70).

        Returns:
            int: The count of 'good' ratings.
        """
        return sum(1 for rating in self.ratings if 60 <= rating <= 70)

    def count_satisfactory(self) -> int:
        """Count and return the number of ratings in the 'satisfactory' category (0-59).

        Returns:
            int: The count of 'satisfactory' ratings.
        """
        return sum(1 for rating in self.ratings if 0 <= rating <= 59)

    def __str__(self) -> str:
        """Return a string representation of the ratings.

        Returns:
            str: A string of the ratings.
        """
        return f"Рейтинги: {', '.join(map(str, self.ratings))}"


student_ratings = StudentRating([55, 65, 85, 95, 100, 45, 75, 70, 90, 80])

print("Максимальний рейтинг:", student_ratings.max_rating())
print("Мінімальний рейтинг:", student_ratings.min_rating())
print("Середній рейтинг:", student_ratings.average_rating())
print("----------------------------------------------------")
print("Кількість студентів з рейтингом вище середнього:", student_ratings.count_above_average())
print("Кількість студентів з рейтингом нижче середнього:", student_ratings.count_below_average())
print("Кількість студентів з рейтингом 'excellent':", student_ratings.count_excellent())
print("----------------------------------------------------")
print("Кількість студентів з рейтингом 'very good':", student_ratings.count_very_good())
print("Кількість студентів з рейтингом 'good':", student_ratings.count_good())
print("Кількість студентів з рейтингом 'satisfactory':", student_ratings.count_satisfactory())
print("----------------------------------------------------")
print(student_ratings)


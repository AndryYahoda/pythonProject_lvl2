class StudentRating:
    """Class to manage and analyze student ratings."""

    def __init__(self, ratings=None):
        """Initialize the StudentRating instance with an optional list of ratings."""
        self.ratings = ratings or []

    def get_ratings(self):
        """Return the list of ratings."""
        return self.ratings

    def set_ratings(self, new_ratings):
        """Set a new list of ratings."""
        self.ratings = new_ratings

    def add_rating(self, rating):
        """Add a single rating to the list of ratings."""
        self.ratings.append(rating)

    def max_rating(self):
        """Return the maximum rating, or None if no ratings are available."""
        return max(self.ratings, default=None)

    def min_rating(self):
        """Return the minimum rating, or None if no ratings are available."""
        return min(self.ratings, default=None)

    def average_rating(self):
        """Calculate and return the average rating, or None if no ratings are available."""
        return sum(self.ratings) / len(self.ratings) if self.ratings else None

    def count_above_average(self):
        """Count and return the number of ratings above the average rating."""
        avg = self.average_rating()
        return sum(1 for rating in self.ratings if rating > avg) if avg is not None else 0

    def count_below_average(self):
        """Count and return the number of ratings below the average rating."""
        avg = self.average_rating()
        return sum(1 for rating in self.ratings if rating < avg) if avg is not None else 0

    def count_excellent(self):
        """Count and return the number of ratings in the 'excellent' category (91-100)."""
        return sum(1 for rating in self.ratings if 91 <= rating <= 100)

    def count_very_good(self):
        """Count and return the number of ratings in the 'very good' category (71-90)."""
        return sum(1 for rating in self.ratings if 71 <= rating <= 90)

    def count_good(self):
        """Count and return the number of ratings in the 'good' category (60-70)."""
        return sum(1 for rating in self.ratings if 60 <= rating <= 70)

    def count_satisfactory(self):
        """Count and return the number of ratings in the 'satisfactory' category (0-59)."""
        return sum(1 for rating in self.ratings if 0 <= rating <= 59)

    def __str__(self):
        """Return a string representation of the ratings."""
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

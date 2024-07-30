class Movie:
    def __init__(self, title, runtime, year_released, genre):
        self.title = title
        self.runtime = runtime
        self.year_released = year_released
        self.genre = genre

    def print_details(self):
        print(f"Title: {self.title}, Runtime: {self.runtime} minutes, Year Released: {self.year_released}, Genre: {self.genre}")


godfather = Movie("The Godfather", 175, 1972, "Crime, Drama")
shawshank = Movie("The Shawshank Redemption", 142, 1994, "Crime, Drama")
godfather.print_details()
shawshank.print_details()

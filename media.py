class Movie(object):
    """
    Movie Class holds all the necessary
    pieces of data for a movie
    """
    # Poster base url to pull image from
    POSTER_URL = "https://image.tmdb.org/t/p/original/"

    # Initialize new movie object with data
    def __init__(self, title, storyline, year, poster_id, trailer_id):
        self.title = title
        self.storyline = storyline
        self.poster_id = poster_id
        self.trailer_id = trailer_id
        self.year = year

    # Function used in testing prints details of object
    def print_details(self):
        print("Title: " + self.title)
        print("Storyline: " + self.storyline)
        print("Poster URL: " + self.POSTER_URL + self.poster_id)
        print("Trailer ID: " + self.trailer_id)
        print("Year: " + str(self.year))

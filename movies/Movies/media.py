class Movie():
    """This class provides a way to store movie related info """
    def __init__(self, Movie_title, Movie_storyline, poster_image, trailer_youtube):  # noqa
        self.title = Movie_title
        self.storyline = Movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

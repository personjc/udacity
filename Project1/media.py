import webbrowser


class Movie():
    """ Movie object for the entertainment center

    Attributes:
        movie_title: title of the selected movie
        movie_storyline: short synopsis of movie plot
        poster_image: picture of the official movie poster
        trailer_youtube: url of the movie trailer
        year: release year for the movie
    """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube,
                 year):
        """initialize movie object taking in all required attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year

    def show_trailer(self):
        """Opens movie trailer in video viewer"""
        webbrowser.open(self.trailer_youtube_url)

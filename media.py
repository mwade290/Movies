class Movie():

    """
    Attributes:
        title (str): Movie Title
        storyline (str): Movie Storyline
        poster_image_url (str): Movie Poster
        trailer_youtube_url (str): Movie Trailer - Must be from Youtube
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

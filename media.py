import webbrowser

# The Movie class:
#
# properties:
#   title - the title of the movie
#   storyline - a brief description of the movie
#   poster_image_url - a link to an image of the movie poster
#   trailer_youtube_url - a link to the trailer for the movie
#
# methods:
#   show_trailer - open the trailer_youtube_url link in the browswer
####################################################################
class Movie():
    """ This class provides a way to store movie related information and functions """

    # all properties set in the constructor
    #######################################   
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # open the trailer_youtube_url link in the browser
    ##################################################
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
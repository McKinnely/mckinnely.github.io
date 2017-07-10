
#********Project: Movie Trailer Website**************
#                                                   *                                             
#   Software Engineer: McKinnely Bentley            *
#   Project: Movie Trailer                          *
#   Inputs:  The input are hard coded in.           *
#   Outputs: Outputs data based on specs given      *
#   in the Udacity specification doc.               *
#                                                   *
#****************************************************



# Imports the "webbrowser" file in order to use the in order to logially open the web browser.  
import webbrowser
class Movie():
    """This is the movie class, which allows for other classes to build objects from it."""

# Creates a constructor to accept data from the classes that uses it.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''' Send the data here and then view the trailer
        in the web browser.'''
        self.title     = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Creates a method "show_trailer" method that allows for other classes to send the
# data here and then view the trailer in the web browser.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

print "Testing"





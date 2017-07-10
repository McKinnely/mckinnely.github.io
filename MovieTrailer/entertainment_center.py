
#********Project: Movie Trailer Website**************
#                                                   *                                             
#   Software Engineer: McKinnely Bentley            *
#   Project: Movie Trailer                          *
#   Inputs:  The input are hard coded in.           *
#   Outputs: Outputs data based on specs given      *
#   in the Udacity specification doc.               *
#                                                   *
#****************************************************


# Imports the "media" file in order to use the Movie class.
# Imports the "fresh_tomatoes" file in order to pass the in 
# logic to open the associated trailers and photos.
import media
import fresh_tomatoes
 
print "working"

# The below variables allows for the data to be sent to the 
# media file and then to be parsed by the Movie class constructor.
toy_story = media.Movie("Toy Story", 
    "Toy Story is an awseome movie!", 
    "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg", 
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", 
    "A marine on an alien planet.", 
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

the_internship = media.Movie("The Internship", 
    "A movie about two regular guys getting hired at Google.", 
    "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg", 
    "https://www.youtube.com/watch?v=cdnoqCViqUo")

ratatouille = media.Movie("Ratatouille", 
    "A movie about a cooking mouse.", 
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", 
    "https://www.youtube.com/watch?v=ALUmKa_mpik")

midnight_in_paris = media.Movie("Midnight In Paris", 
    "A movie about vacationing in Paris.", 
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", 
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", 
    "A movie about survival.", 
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg", 
    "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# The below array list "movies" collects all the movie objects and 
# saves them inside of the "movies" array list to be parsed by the 
# below fresh_tomatoes.open_movies_page
# method. 
movies = [toy_story, avatar, the_internship, ratatouille, midnight_in_paris, hunger_games]

# The fresh_tomatoes.open_movies_page is used to open the movies web
# page in a logical and structured manor. 
fresh_tomatoes.open_movies_page(movies)

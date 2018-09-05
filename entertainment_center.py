import media
import fresh_tomatoes

# Create various Movies for display
###################################
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
            "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
            "https://www.youtube.com/watch?v=6ziBFh3V1aM")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
            "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
            "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
            "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
            "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
            "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
            "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
            "https://www.youtube.com/watch?v=mfmrPu43DF8")

# Put the Movies into a list and send it to the website rendering code
######################################################################
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

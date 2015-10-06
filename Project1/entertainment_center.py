import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "poster",
                        "trailer")

good_men = media.Movie( "A Few Good Men",
                        "Two soldiers are put on trial over the death of a fellow solider",
                        "https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
                        "https://www.youtube.com/watch?v=ePo91pMcu94")

movies= [toy_story, good_men]

fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)

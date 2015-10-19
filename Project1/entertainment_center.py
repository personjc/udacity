import media
import fresh_tomatoes

"""
Displays the given movies. Runs fresh_tomatoes.  
"""

days_of_summer = media.Movie("500 Days of Summer",
                        "This is a story of boy meets girl, but this is not a love story.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",
                        "https://www.youtube.com/watch?v=PsD0NpFSADM",
                        "2009")

good_men = media.Movie( "A Few Good Men",
                        "Two soldiers are put on trial over the death of a fellow solider",
                        "https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
                        "https://www.youtube.com/watch?v=ePo91pMcu94",
                        "1992")

gladiator = media.Movie( "Gladiator",
                        "Roman General seeks to exact revenge on his family's murderer",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=IvTT29cavKo",
                         "2000")

movies= [days_of_summer, good_men, gladiator]

fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)

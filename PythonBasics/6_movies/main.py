"""
'Movie website' project from lesson 6
Imports Movie class from media.py to create instances of that class.
Uses fresh_tomatoes to generate a web page
"""

from media import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story",
                  "A story about toys",
                  "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY606_.jpg",
                  "https://www.youtube.com/watch?v=Ny_hRfvsmU8")

alien3 = Movie("Alien 3",
               "A story about space and space creatures",
               "http://www.impawards.com/1992/posters/alien_three_ver1_xlg.jpg",
               "https://www.youtube.com/watch?v=Ipv1y-Phi7A")

thematrix = Movie("The Matrix",
                  "A story about people in a dream world",
                  "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
                  "https://www.youtube.com/watch?v=m8e-FF8MsqU")

fightclub = Movie("Fight Club",
                  "A story about life",
                  "http://www.impawards.com/1999/posters/fight_club_ver1.jpg",
                  "https://www.youtube.com/watch?v=SUXWAEX2jlg")

movies = [toy_story, alien3, thematrix, fightclub]
fresh_tomatoes.open_movies_page(movies)

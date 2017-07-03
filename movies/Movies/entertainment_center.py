import fresh_tomatoes
import media
Flipped = media.Movie("Flipped",
                      "love story",
                      "https://upload.wikimedia.org/wikipedia/en/3/3a/Flipped_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=92SgWpDYjlo")
The_Lion_king = media.Movie("The Lion King",
                            "Simba",
                            "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=s2p1NNsXg7s")
Front_of_the_Class = media.Movie("Front of the Class",
                                 "to be number one",
                                 "https://upload.wikimedia.org/wikipedia/en/a/aa/Front_of_the_Class_poster.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=R9rLslyqsBM")
Source_code = media.Movie("Source Code",
                          "life is in your hand",
                          "https://upload.wikimedia.org/wikipedia/en/e/e5/Source_Code_Poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=NkTrG-gpIzE")
Trainspotting = media.Movie("Trainspotting",
                            "Teenager",
                            "https://upload.wikimedia.org/wikipedia/en/7/71/Trainspotting_ver2.jpg",  # noqa
                            "https://www.youtube.com/watch?v=6ZU6sMlqHEI")
Schindler = media.Movie("Schindler",
                        "a 1993 American epic historical period drama film",
                        "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",  # noqa
                        "https://www.youtube.com/watch?v=Tnj6COmS4ow")

#Add each movie to the list
movies = [Flipped, The_Lion_king, Front_of_the_Class, Source_code,
          Trainspotting, Schindler]
# Take a list of movies and create a website to show these movies
fresh_tomatoes.open_movies_page(movies)



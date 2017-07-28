import fresh_tomatoes
import media

#below are 6 movie instances that use the Movie class from media.py
rookie_of_the_year = media.Movie('Rookie of the Year',
                                 'When an accident miraculously gives a boy an incredibly powerful pitching arm, he becomes a major league pitcher for the Chicago Cubs.',
                                 'https://images-na.ssl-images-amazon.com/images/M/MV5BZGJhODAwNDQtNGY0My00ZDA4LTgwOTMtMTA5NzdhZTQ0YmIwXkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_UX182_CR0,0,182,268_AL_.jpg',
                                 'https://www.youtube.com/watch?v=Heoa-AI42bA')

evolution = media.Movie('Evolution',
                        'College professor Ira Kane (David Duchovny) and geologist Harry Block (Orlando Jones), investigate a meteor crash in Arizona.',
                        'https://upload.wikimedia.org/wikipedia/en/2/2f/Evolution_movie.jpg',
                        'https://www.youtube.com/watch?v=PM0HXsH28To')


the_matrix = media.Movie('The Matrix',
                         'A dystopian future in which reality as perceived by most humans is actually a simulated reality called "The Matrix"',
                         'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
                         'https://www.youtube.com/watch?v=vKQi3bBA1y8')

a_knights_tale = media.Movie("A Knight's Tale",
                             "William Thatcher's (Ledger) quest to change his stars, win the heart of an exceedingly fair maiden (Sossamon) and rock his medieval world.",
                             "https://upload.wikimedia.org/wikipedia/en/a/a6/AKnightsTale.jpg",
                             "https://www.youtube.com/watch?v=3C_7qoPII4I")

the_fifth_element = media.Movie("The Fifth Element",
                                "New York cab driver Korben Dallas didn't mean to be a hero, but he just picked up the kind of fare that only comes along every five thousand years: A perfect beauty, a perfect being, a perfect weapon. Together, they must save the world.",
                                'https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg',
                                'https://www.youtube.com/watch?v=fQ9RqgcR24g')

harry_potter_1 = media.Movie("Harry Potter and the Sorcerer's Stone",
                             "The story of a boy who learns on his 11th birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. Invited to attend Hogwarts School of Witchcraft and Wizardry, Harry embarks on the adventure of a lifetime.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                             "https://www.youtube.com/watch?v=RzCjI3Jy7E8")

movies = [rookie_of_the_year,
          evolution,
          the_matrix,
          a_knights_tale,
          the_fifth_element,
          harry_potter_1]

fresh_tomatoes.open_movies_page(movies)

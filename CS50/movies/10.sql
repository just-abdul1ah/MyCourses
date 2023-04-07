SELECT DISTINCT(name) FROM people, movies, ratings, directors
WHERE rating >= 9
AND ratings.movie_id = movies.id
AND movies.id = directors.movie_id
AND directors.person_id = people.id;
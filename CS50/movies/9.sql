SELECT DISTINCT(name) FROM people, movies, stars
WHERE year = 2004
AND movies.id = stars.movie_id
AND stars.person_id = people.id
ORDER BY birth ASC;
SELECT DISTINCT(name) FROM people, movies, stars
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND title IN (
SELECT title FROM movies, people, stars
WHERE name = 'Kevin Bacon' AND birth = 1958
AND people.id = stars.person_id
AND stars.movie_id = movies.id
)
AND name != 'Kevin Bacon';
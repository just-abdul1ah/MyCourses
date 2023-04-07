SELECT name FROM movies, stars, people
WHERE title = 'Toy Story'
AND movies.id = stars.movie_id
AND stars.person_id = people.id;
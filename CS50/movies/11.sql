SELECT title FROM movies, stars, people, ratings
WHERE name = 'Chadwick Boseman'
AND people.id = stars.person_id
AND stars.movie_id = movies.id
AND movies.id = ratings.movie_id ORDER BY rating DESC LIMIT 5;
SELECT title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE name = 'Helena Bonham Carter'
AND title IN (
SELECT title FROM movies, stars, people
WHERE name = 'Johnny Depp'
AND stars.person_id = people.id
AND stars.movie_id = movies.id
);
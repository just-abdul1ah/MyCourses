SELECT title, rating FROM movies, ratings
WHERE year = 2010
AND movie_id = id ORDER BY rating DESC, title ASC;
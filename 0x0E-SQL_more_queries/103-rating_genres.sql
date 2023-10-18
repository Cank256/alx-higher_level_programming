-- List genres by their rating sum
SELECT tv_genres.name, SUM(tv_shows_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
INNER JOIN tv_shows_ratings ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;

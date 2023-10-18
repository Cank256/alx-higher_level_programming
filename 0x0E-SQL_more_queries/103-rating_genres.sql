-- List genres by their rating sum
SELECT tv_genres.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_genres
INNER JOIN hbtn_0d_tvshows ON tv_genres.id = hbtn_0d_tvshows.genre_id
INNER JOIN hbtn_0d_tvshows_rate ON hbtn_0d_tvshows.id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

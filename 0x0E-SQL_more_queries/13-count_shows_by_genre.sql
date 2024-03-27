-- script that lists all genres from hbtn_0d_tvshows
SELECT t1.name AS genre,
    count(t1.name) AS number_of_shows
FROM tv_genres t1
    RIGHT JOIN tv_show_genres t2 ON t1.id = t2.genre_id
GROUP BY(genre)
ORDER BY number_of_shows DESC;

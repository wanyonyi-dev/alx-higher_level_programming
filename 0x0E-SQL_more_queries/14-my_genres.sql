-- script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter
SELECT t1.name
FROM tv_genres t1
    INNER JOIN tv_show_genres t2 ON t1.id = t2.genre_id
    INNER JOIN tv_shows t3 ON t2.show_id = t3.id
WHERE t3.title = "Dexter"
ORDER BY t1.name;

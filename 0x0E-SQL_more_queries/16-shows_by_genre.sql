-- script that lists all shows, and all genres linked to that show,
--  from the database hbtn_0d_tvshows
SELECT t1.title, t3.name
FROM tv_shows t1
    LEFT JOIN tv_show_genres t2 ON t2.show_id = t1.id
    LEFT JOIN tv_genres t3 ON t3.id = t2.genre_id
ORDER BY t1.title, t3.name;

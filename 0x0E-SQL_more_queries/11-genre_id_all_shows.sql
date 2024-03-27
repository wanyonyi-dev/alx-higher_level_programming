-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT
    t1.title,
    t2.genre_id
FROM
    tv_shows t1
    LEFT JOIN tv_show_genres t2 ON t1.id = t2.show_id
ORDER BY
    t1.title,
    t2.genre_id

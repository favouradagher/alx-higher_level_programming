-- Select all shows and their rating sum
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC, tv_shows.title ASC;

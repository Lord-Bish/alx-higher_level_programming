-- Show genre and number of shows attached

SELECT gen.`name` AS `genre`,
	COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS gen
	INNER JOIN `tv_show_genres` AS sh
	ON gen.`id`=sh.`genre_id`
GROUP BY gen.`name`
ORDER BY `number_of_shows` DESC;

-- sql script to groups records with same score

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;

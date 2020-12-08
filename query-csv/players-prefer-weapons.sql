WITH weapon as (
    SELECT player_name,
           tournament_id,
           created_at,
           weapon_name,
           SUM(attack_count) sum_attack_count,
           RANK() OVER (PARTITION BY tournament_id, player_name ORDER BY SUM(attack_count) DESC) use_rank
    FROM `kr_weapons`
    GROUP BY tournament_id, player_name, weapon_name
    ORDER BY player_name, created_at
    ),
    tournament as (
    SELECT player_name, tournament_id,
            SUM(attack_count) sum_attack_count
    FROM `kr_weapons`
    GROUP BY tournament_id, player_name
    ),
     times as
         (SELECT tournament_id,
                 DATE(MIN(created_at)) first,
                 DATE(MAX(created_at)) last
         FROM matches_summary
         GROUP BY tournament_id)

SELECT weapon.player_name 선수이름,
       weapon.tournament_id 토너먼트,
       weapon.weapon_name 무기이름,
       ROUND((weapon.sum_attack_count / tournament.sum_attack_count) * 100, 1) 사용량비율
FROM weapon
INNER JOIN tournament
ON weapon.player_name = tournament.player_name AND weapon.tournament_id = tournament.tournament_id
INNER JOIN times
ON weapon.tournament_id = times.tournament_id
WHERE weapon.use_rank < 4
AND weapon.player_name
ORDER BY weapon.player_name, times.first, 사용량비율 DESC

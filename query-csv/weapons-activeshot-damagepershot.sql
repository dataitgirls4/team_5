WITH weapon as (
    SELECT player_name,
           weapon_name,
           SUM(attack_count) sum_attack_count,
           RANK() OVER (PARTITION BY player_name ORDER BY SUM(attack_count) DESC) use_rank,
           RANK() OVER (PARTITION BY player_name ORDER BY COUNT(weapon_name) DESC) get_rank
    FROM `kr_weapons`
    GROUP BY player_name, weapon_name
    ORDER BY player_name
    )

SELECT weapon.player_name 선수이름,
       weapon.weapon_name 무기이름,
       sixman_shots_damages.boowi 부위,
       sixman_shots_damages.shots 유효사용비율,
       sixman_shots_damages.damages 데미지비율
FROM weapon INNER JOIN sixman_shots_damages
ON weapon.player_name = sixman_shots_damages.player_name AND weapon.weapon_name = sixman_shots_damages.weapon_name
WHERE weapon.use_rank < 4 OR weapon.get_rank < 4
AND weapon.player_name IN ('2HEART', 'UNDER', 'EJ', 'PIO', 'HIKARI', 'DUMBO')
ORDER BY weapon.player_name, use_rank

SELECT player_name, AVG(avg.activeshot)
FROM
(SELECT player_name, weapon_name, (real_attack_count/attack_count)*100 activeshot
FROM kr_weapons
WHERE player_name = 'HIKARI'
GROUP BY weapon_name)avg

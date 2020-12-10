SELECT player_name, ROUND(AVG(avg.damage_per_shot),2) avg_damage_per_shot
FROM
    (SELECT player_name, weapon_name, (damage/real_attack_count)*100 damage_per_shot
     FROM kr_weapons
     WHERE player_name = 'DUMBO'
     GROUP BY weapon_name
    )avg

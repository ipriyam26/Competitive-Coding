t = int(input())
for _ in range(t):
    l,damage = [int(k) for k in input().split(" ")]
    health =  [int(k) for k in input().split(" ")]
    power =  [int(k) for k in input().split(" ")]

    monster_army = list(zip(health,power))
    monster_army.sort(key=lambda x: (-x[1], x[0]),reverse=True)

    total_damage_dealt = 0
    lost = False

    while monster_army:

        monster0_HEALTH,monster0_POWER = monster_army[0]
        monster0_HEALTH-=total_damage_dealt
        if monster0_HEALTH<=0:
            #dead already
            monster_army.pop(0)
            continue
        if damage<=0:
            lost = not lost
            print("NO")
            break
        while monster0_HEALTH > damage > 0:
            monster0_HEALTH-=damage
            total_damage_dealt +=damage
            damage-=monster0_POWER
        monster_army.pop(0)
        total_damage_dealt +=damage
        damage-=monster_army[0][1]
    
    if not lost:
        print("YES")


        
        
        


    

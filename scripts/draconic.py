!serveralias rollarray embed
<drac2>
abilities = [
    "STR",
    "DEX",
    "CON",
    "WIS",
    "INT",
    "CHA",
]
ability_min = 7
ability_max = 16
total_min = 74
total_max = 74
array = {}
while True:
    for a in abilities:
        # roll 4d6kh3
        rolls = [
            randint(1, 7) for _ in range(4)
        ]
        rolls.sort()
        score = sum(rolls[1:])

        array[a] = min(ability_max, max(ability_min, score))

    total = sum(array.values())
    if total_min <= total <= total_max:
        break

T = f"Generate ability scores in [{ability_min}, {ability_max}], total [{total_min}, {total_max}]"
D = f"{array}, total: {total}"
</drac2>
-title "{{T}}"
-desc "{{D}}"

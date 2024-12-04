PlayerList = []

def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name="", damage=0, defensePower=0):
    return {
        "name": name,
        "score": 0,
        "damage": damage,
        "health": 100,
        "defensePower": defensePower,
        "defense": False
    }

def addPlayer(player):
    PlayerList.append(player)

def removePlayer(name):
    for player in PlayerList:
        if player['name'] == name:
            PlayerList.remove(player)
            return
    print("There is no player with that name!")

def setPlayer(player, key, value):
    player[key] = value

def attackPlayer(attacker, target):
    if target['defense']:
        damage_diterima = max(0, attacker['damage'] - target['defensePower'],2)
        setPlayer(attacker, 'score', round(attacker["score"] + 1 - 1 / target["defensePower"], 2))
    else:
        damage_diterima = attacker['damage']
        setPlayer(attacker, 'score', attacker['score'] + 1)
    
    setPlayer(target, 'health', target['health'] - damage_diterima)
    setPlayer(target, 'defense', False)

def displayMatchResult():
    peringkat = sorted(
        PlayerList, 
        key=lambda x: (-x['score'], -x['health'])
    )
    
    for i, player in enumerate(peringkat, 1):
        print(f"Rank {i}: {player['name']} | Score: {player['score']} | Health: {player['health']}")

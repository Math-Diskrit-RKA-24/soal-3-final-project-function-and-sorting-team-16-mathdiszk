# Inisialisasi daftar pemain
initPlayers()

# Membuat beberapa pemain baru
player1 = createNewPlayer(name="Alice", damage=20, defensePower=5)
player2 = createNewPlayer(name="Bob", damage=15, defensePower=3)
player3 = createNewPlayer(name="Charlie", damage=25, defensePower=2)

# Menambahkan pemain ke daftar pemain
addPlayer(player1)
addPlayer(player2)
addPlayer(player3)

# Menyerang pemain Bob dengan pemain Alice
print("Sebelum serangan:")
print(f"{player1['name']} - Health: {player1['health']}, Score: {player1['score']}")
print(f"{player2['name']} - Health: {player2['health']}, Score: {player2['score']}")
print(f"{player3['name']} - Health: {player3['health']}, Score: {player3['score']}")
attackPlayer(player1, player2)

# Menyerang pemain Charlie dengan pemain Bob
attackPlayer(player2, player3)

# Bob bertahan saat diserang oleh Alice
setPlayer(player2, 'defense', True)
attackPlayer(player1, player2)

# Menampilkan hasil pertandingan
print("\nHasil Pertandingan:")
displayMatchResult()
songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0:2])
print(songs[1:4])

songs[0] = "Possession"
print(songs[0])

songs.extend(["fever dream", "Little Garcon", "Kiss from a Rose"])
print(songs)

del songs[1]
print(songs)

for song in songs:
    print(song)

for i in range(len(songs)):
    print(songs[i])



animals = ["cat", "fox", "kiwi"]

animals.append("meerkat")
print(animals[2])

del animals[0]

for i in range(len(animals)):
    print(animals[i])
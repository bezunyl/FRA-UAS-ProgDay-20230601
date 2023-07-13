t, n = tuple(map(int, input().split()))
songs = list(map(int, input().split()))

songs_s = sorted(songs)

time = 0
t = t * 60

for s in songs_s:
    time += s

    if time > t:
        time -= s
        break

print(time)



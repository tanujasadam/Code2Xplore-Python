n=int(input("Enter number of songs:"))
playlist=[0] * n
for i in range(n):
    playlist[i]= int(input("Enter duration of song:"))

invalid = False
for i in range(n):
    if playlist[i] <= 0:
        invalid=True

if invalid==True:
    print("Invalid Playlist:Contains non-positive durations.")
else:
    total_duration=0
    for i in range(n):
        total_duration= total_duration + playlist[i]

    print("Total Duration:",total_duration, "seconds")
    print("Songs:", n)

    repetitive = False
    for i in range(n):
        count=0
        for j in range(n):
            if playlist[i] == playlist[j]:
                count=count+1
        if count>1:
            repetitive = True
    minimum = playlist[0]
    maximum = playlist[0]
    for i in range(n):
        if playlist[i] < minimum:
            minimum = playlist[i]
        if playlist[i] > maximum:
            maximum = playlist[i]
    difference = maximum - minimum

    if total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Increase playlist length for better experience"
    elif total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Trim down some tracks for balanced listening"
    elif repetitive==True:
        category = "Repetitive Playlist"
        recommendation = "Include songs of different durations for variety"
    elif difference <= 300:
        category = "Balanced Playlist"
        recommendation = "Playlist is well structured and enjoyable"
    else:
        category = "Irregular Playlist"
        recommendation = "Adjust song duration for smoother flow"
    print("Category:",category)
    print("Recommendation:",recommendation)
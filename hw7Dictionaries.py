#hw 7 dict and sets pirple

favSong = {
    "Artist":"Marshmello",   
    "Song":"Blocks",
    "DurationInMinutes":3.483,
    "Producer":"Wild Bill",
    "Label":"House label",
    "NumOfSpotifyListens":1400000,
    "YearRecorded":2016,
    "AlbumName":"Joytime",
    "AlbumArtwork":"Some Lady",
    "SalesinUSDollars":4350000.27
    }

key = input("What item do you want to guess?")
value = input("what is your guess?")


for song in favSong:
    if key in favSong:
        match = favSong[key]
        print(match)
    else:
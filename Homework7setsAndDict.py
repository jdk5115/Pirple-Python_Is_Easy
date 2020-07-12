'''
Homework #7 copied from Homework #1 pirple
Sets and dictionaries
'''

#Artist and Genre info
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

while(True):
    key = input("What item do you want to guess?")
    value = input("what is your guess?")

    def guessFunc(key,value):
        if key in favSong:
            if value in favSong:
                print("hey now")
            else:
                print("nah")

    guessFunc(key,value)

# print(Artist)
# print(Song)
# print(DurationInMinutes)
# print(Producer)
# print(Label)
# print(NumOfSpotifyListens)
# print(YearRecorded)
# print(AlbumName)
# print(AlbumArtwork)
# print(SalesinUSDollars)
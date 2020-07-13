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

key = input("What item do you want to guess?")
value = input("what is your guess?")


for song in favSong:
    if key in favSong:
        match = favSong[key]
        print(match)
    else:


    # for x in favSong:
    #     if key in favSong:
    #         if value in favSong: 
    #             if favSong[key] == value:
    #                 print(value)
    #                 break
    #         else:
    #             print("Please pick another item.  Your item was not found in the dictionary.")
    #             break

    # def guessFunc(key,value):
    #     if key in favSong:
    #         if value in favSong.items():
    #             print(key, value)

    # guessFunc(key,value)

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
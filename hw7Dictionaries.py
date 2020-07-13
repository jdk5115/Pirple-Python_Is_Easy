#hw 7 dict and sets pirple

favSong = {
    "Artist":"Marshmello",   
    "Song":"Blocks",
    "DurationInMinutes":"3.483",
    "Producer":"Wild Bill",
    "Label":"House label",
    "NumOfSpotifyListens":"1400000",
    "YearRecorded":"2016",
    "AlbumName":"Joytime",
    "AlbumArtwork":"Some Lady",
    "SalesinUSDollars":"4350000.27"
    }

while(True):
    key = input("What item do you want to guess?")
    value = input("what is your guess?")

    if key in favSong:
        match = favSong[key]
        if match == value:
            again = input("Nice, you got it! The answer was " + match + ". Want to try again? Answer Yes or No only.")
            if again == "Yes":
                continue 
            else:
                print("see ya")
                break
        else:
            print("Nope.  Better luck next time.")
            break
    else:
         print("Nope. You blew it.")
         break

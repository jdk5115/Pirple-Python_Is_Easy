# input output homework pirple
import os

''' 
Details:
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
    A) Read the file
    B) Delete the file and start over
    C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 

Extra Credit:
Allow the user to select a 4th option:
    D) Replace a single line

If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:
    1) The line number they want to update.
    2) The text that should replace that line. 
'''

fileName = input("What do you want the filename to be?") + ".txt"


if os.path.isfile(fileName):
    choice = input("Do you want to: \n A) Read the File \n B) Delete the file and start over \n C) Append the file \n ")

    if choice == "A":
        File = open(fileName, 'r') 
        lines = File.readlines() 
        print(lines)
        File.close()

    elif choice == "B":
        os.remove(fileName)
        File = open(fileName,"w")
        File.close()
        print("The old file has been deleted and a new file has been created.")

    elif choice == "C":
        File = open(fileName,"a")
        Filez = [File]
        fileAppend = input("What would you like to add to the file?")
        Filez.append(fileAppend)
        File.write(str(Filez))
        print("Your file has been appended.")
    else:
        print("Please only choose either A, B, or C.")

else:
    data = input("What do you want to input into file?")
    File = open(fileName, "w")
    File.write(data)
    File.close()
    print("Your file has been created!")

File.close()


#!/usr/bin/python3
# Currently unfinshed! Archived for now.

def main():
    quat = {"00":"0", "01":"1", "10":"2", "11":"3"}

    print(":: Enter 'q' to exit ::")

    usrinput = str(input("Binary to Quaternary:: "))

    while usrinput != 'q':
        print("Your Entry: " + usrinput)

        # make the binary string even by adding a leading zero
        if len(usrinput) % 2 != 0:
            usrinput = "0" + usrinput
            # print(usrinput)

        # convert another or exit
        usrinput = str(input("Binary to Quaternary:: "))

main()

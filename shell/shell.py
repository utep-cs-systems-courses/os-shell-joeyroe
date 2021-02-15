import os, sys, re

prompt = '$ '

def main():

    while True:
        if 'PS1' in os.environ:
            os.write(1, (os.environ['PS1']).encode())
        else:
            os.write(1, ("$ ").encode()) #writes the prompt
            userInput = input() #get user input

            if(userInput == 'exit'): #quit if exit is typed
                sys.exit(1)

            splitUserInput = userInput.split(" ")

            if(splitUserInput[0] == 'cd' and len(splitUserInput) == 2): #makes sure only two things were entered for cd

                try:
                    os.chdir(splitUserInput[1])

                except:  #directory does not exist
                    os.write(1, ("%s was not found\n" % splitUserInput[1]).encode())



if __name__ == '__main__':
    main()

from os import read

next = 0
limit = 0

# my_getChar calls read to fill a buffer. It gets one character at a time.
def getChar():
    global next
    global limit

    if(next == limit): #buffer is empty
        next = 0 #resetting the buffer
        limit = read(0, 1000) #read into the buffer

        if(limit == 0): #it's reached the end of the file
            return "EOF"

    if(next < len(limit) - 1): #checks if its in bounds
        c = chr(limit[next])
        next += 1
        return c

    else:
        return "EOF"


# getLine gets the next line from file descriptor 0 as a String
def getLine():
    global next
    global limit
    line = ""
    char = getChar()
    while(char != '' and char != "EOF"):  # Check to see if we have a character to append.
        line += char
        char = getChar()
    next = 0  # reset next and limit after we have have finished a line.
    limit = 0
    return line #returns empty if EOF
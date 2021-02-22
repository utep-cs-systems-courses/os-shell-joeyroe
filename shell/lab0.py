from os import read

buffer = None

#readString reads a string to a buffer
def readString():

    global buffer
    buffer = read(0, 1000) #reads to the buffer

    if(buffer == 0): #Buffer has reached the end of the file
        return "EOF"

    return buffer


def readLine():

    global buffer
    line = ""
    i = 0

    if(buffer == None): #if the buffer is empty
        buffer = readString()

    while len(buffer) > 0:

        line += chr(buffer[i]) #add to the line
        if ("\n" in line): #encounters a new line
            buffer = buffer[i + 1:]
            return line
        i += 1

    if(i == len(buffer)): #resets the buffer
        i = 0
        buffer = readString()
    return line

#def main():


 #   b = readLine()
  #  print(b)

#   main()
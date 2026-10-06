
def readFile(fileName):
    with open(fileName,'r') as file:
        content = file.read()
        return content

import calculateHash
import readFile
import compareHash
import json

def main():
    filename = 'file.txt' # -> sollte später variabel sein

    with open("hashes.json", "r") as file:
        print(file.read())

    with open("hashes.json", "r") as file:
        hashes = json.load(file)

        if filename in hashes:
            oldHash = hashes[filename]
            text = readFile.readFile('file.txt')
            calculatedHash = calculateHash.calculateHash(text)
            print(compareHash.compare(calculatedHash, oldHash))
            print(calculatedHash)
            exit(0)

        print("Couldn't find the file, saving...")
        text = readFile.readFile('file.txt')
        calculatedHash = calculateHash.calculateHash(text)
        hashes[filename] = calculatedHash
        with open("hashes.json", "w") as file:
            json.dump(hashes, file)
        print("Saved file")

if __name__ == "__main__":
    main()

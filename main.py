import calculate_hash
import read_file
import compare_hash
import json

def main():
    filename = 'file.txt' # -> sollte später variabel sein

    text = read_file.read_file('file.txt')
    calculatedHash = calculate_hash.calculate_hash(text)

    with open("hashes.json", "r") as file:
        hashes = json.load(file)

        if filename not in hashes:
            print("Couldn't find file name, saving...")
            hashes[filename] = calculatedHash
            with open("hashes.json", "w") as file:
                json.dump(hashes, file)
            print("Saved file")

        else:
            print("File name found, checking hash...")
            oldHash = hashes[filename]
            print(compare_hash.compare(calculatedHash, oldHash))
            print(calculatedHash)

if __name__ == "__main__":
    main()

import hashlib


def main():
    print("Calculating hash...")
    m = hashlib.sha256()
    m.update(b"Hallo was geht")
    calculatedHash = m.hexdigest()
    print(compare(calculatedHash))
    print(calculatedHash)

def compare(calculatedHash):
    correctHash = "5376988ea08c2dec574d91f7e5f073093c07ab1644de38c6f616abab2cb84be5"
    if calculatedHash == correctHash:
        return "Correct"
    else:
        return "Incorrect"

if __name__ == "__main__":
    main()
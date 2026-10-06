def compare(calculatedHash, oldHash):
    if calculatedHash == oldHash:
        return "No Change"
    else:
        return "File modified"

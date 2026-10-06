# File-Integrity-Checker (fic)
Fic is a program that checks, if a file was changed since the last scan. It does this by calculating the SHA-256 hash of the given file and saving it to a JSON-file, if it isn't already in the JSON.

If the given file name already exists in the JSON, fic will compare the old saved hash with the new hash of the now given file. It then returns, wether the file was changed in the meantime.

Librarys used: hashlib, json

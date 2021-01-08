# QuickHash
Uses the hashtoolkit.com hash database to convert md5, sha1, sha256, sha384 and sha512 to passwords or text

Usage:

Requires python3. Have not tested on python2

-hl - hash location, to use this just type "-hl /Example_hash_file.txt"
-hv - hash value, to use this just type "-hl somerandomhash"
-w - Writes found hashes to a file, Name the file whatever you want  so for example "-w Name_Of_file"

Examples:

python3 quickhash.py -hl /Example_hash_file.txt -w hashes.txt

python3 quickhash.py -hl /Example_hash_file.txt

python3 quickhash.py -hv 7B502C3A1F48C8609AE212CDFB639DEE39673F5E -w Hashes.txt

python3 quickhash.py -hv 7B502C3A1F48C8609AE212CDFB639DEE39673F5E

import sys, os, hashlib
from collections import OrderedDict as od

def getHashSums(file_path):
    hashSums = od()
    hashSums['md5sum'] = hashlib.md5()
    hashSums['sha1sum'] = hashlib.sha1()
    hashSums['sha224sum'] = hashlib.sha224()
    hashSums['sha256sum'] = hashlib.sha256()
    hashSums['sha384sum'] = hashlib.sha384()
    hashSums['sha512sum'] = hashlib.sha512()

    with open(file_path, 'rb') as fd:
        dataChunk = fd.read(1024) #Reading only 1mb at a time 
        while dataChunk:
            for hashsum in hashSums.keys():
                hashSums[hashsum].update(dataChunk)
            dataChunk = fd.read(1024)

    results = od()
    for key,value in hashSums.items():
        results[key] = value.hexdigest()         
    return results

def main():
    for path in sys.argv[1:]:
        for key,value in getHashSums(path).items():
            print(key,value)

if __name__ == '__main__': 
    main()

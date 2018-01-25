# pyCheckSum Calculator
Get the md5, sha1, sha224, sha256, sha384, and sha512 hash sum of a file using a python script.

```
$ python pyCheckSum.py testFile.txt
```
## Output:
```
md5sum 70ab0fecde91d64788a7092caa4e58b5
sha1sum dc1507883fd97251c76dfae3b227a8c41a2aa9ab
sha224sum a1d7f13c76cf0ce79f6f7fd68c633782754e756292ba3063c24d3c34
sha256sum 68ebf5ebd8af52c2e710a6f545ed81c644c75a46270e9f2a59bf41d3c77b319e
sha384sum 63e164badf5f35e429b4efee47704d649cc17a9ebf7b451ba7278ac70357d1f06e9563326c6499747e349fcbcd6d2786
sha512sum 763a880599c117060ae859b2ae0b447efe81d7cad802d16d8217ce83bae461ddf0ccd1424909495764c9d52fc0e5ca55755dd2ab95431a77a457eec5be255f07
```

## To DO:
Maybe instead of calculating all the check sum of a file using all these algorithm, I might wanna allow the user to choose which one to use.

from zipfile import ZipFile
import py7zr
path = "C:\\Users\\tawfik.khaled\\tracking\\a50219\\a50219-2\\a50219\\test\\"
import gzip

f = py7zr.SevenZipFile(path+"file2.7z", blocksize=16)
strs = f.read()
zip = gzip.open(path +"file3.gz", mode="wb")
#zip.write()
inp = list(strs.values())[0]
while(True):
    line = inp.readline()
    if(not line):
        break
    print(line)
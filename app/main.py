import sys
import os
import zlib
from hashlib import new

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    #Uncomment this block to pass the first stage
    
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    elif command == 'cat-file' and sys.argv[2] == '-p':
        hashed_val = sys.argv[3]
        with open('.git/objects/'+str(hashed_val[:2])+'/'+str(hashed_val[2:]), 'rb') as f:
            raw = zlib.decompress(f.read())
            header, content = raw.split(sep=b'\0', maxsplit=1)
            print(content.decode(encoding='utf-8'), end='')
    elif command == 'hash-object' and sys.argv[2] == '-w':
        with open(sys.argv[3], 'rb') as f:
            content = f.read()
        header = f"blob {len(content)}\x00"
        headed_content = header.encode('ascii') + content
        hashed_sha = new(name='sha1', data = headed_content).hexdigest()
        print(hashed_sha)

        os.mkdir(os.getcwd()+'.git/objects/'+hashed_sha[:2]+'/'+hashed_sha[2:])
        with open(os.getcwd()+'.git/objects/'+hashed_sha[:2]+'/'+hashed_sha[2:], 'wb') as f2:
            f2.write(zlib.compress(content))
                
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()

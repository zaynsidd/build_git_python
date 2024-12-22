import sys
import os
import zlib


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
            header, content = raw.split(sep='\0')
            #blob, size = header.split(sep=' ')
            #size = int(size)
            print(content)
        pass
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()

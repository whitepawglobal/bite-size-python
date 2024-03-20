def readline(filename):
    
    with open(filename, "r") as f:
        
        while True:
    
            line = f.readline()
        
            if not line:
                break
                
            else:
                yield line
        
#readline("sample.txt")


if __name__ == "__main__":
    for line in readline("sample.txt"):

        print("line:" + line)
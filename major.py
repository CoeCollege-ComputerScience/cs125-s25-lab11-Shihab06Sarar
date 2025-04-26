def major():
    math=set()
    cs=set()
    infile= open("math.txt", "r")
    infile2= open("cs.txt", "r")
    infile.readline()
    infile2.readline()
    for line in infile:
        line= line.strip()
        math.add(line)
    for line in infile2:
        line= line.strip()
        cs.add(line)
    
    infile2.close()
    for name in sorted(math.union(cs)):
        print(name)
    
    for name in sorted(math.union(cs)):
        print(name)

    for name in sorted(cs.difference(math)):
        print(name)
      
    infile.close()
major()
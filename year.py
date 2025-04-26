def student():
    math = set()
    cs = set()
    year1 = set()
    year2 = set()
    year3 = set()
    year4 = set()

    infile = open("math.txt", "r")
    infile2 = open("cs.txt", "r")
    infile3 = open("studentYear.txt", "r")

    infile.readline()
    infile2.readline()

    for line in infile:
        line = line.strip()
        math.add(line)

    for line in infile2:
        line = line.strip()
        cs.add(line)

    for line in infile3:
        line = line.strip()
        if len(line.split()) == 2:
            year, name = line.split()
            if year == "1":
                year1.add(name)
            elif year == "2":
                year2.add(name)
            elif year == "3":
                year3.add(name)
            elif year == "4":
                year4.add(name)

    infile.close()
    infile2.close()
    infile3.close()

    for name in sorted(year2.intersection(cs)):
        print(name)

    for name in sorted(year1.difference(math.union(cs))):
        print(name)

    for name in sorted(year4.intersection(math.union(cs))):
        print(name)

student()


 

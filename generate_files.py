
# function to create n amount of m-byte files in directory d
def create_files(d, n, m):
    # find number of leading 0s necessary for file naming
    digits = len(str(n-1))

    # create n empty m-byte files
    for i in range(n):
        with open(d + "/test" + str(i).zfill(digits), "w+b") as out:
            # traverse to the last byte and write zero-byte
            out.seek(m-1)
            out.write('\0')

# DS01: (10,000) 10KB files
def create_ds01():
    create_files("DS01", 10000, 10*1024)

# DS02: (10,000) 100KB files
def create_ds02():
    create_files("DS02", 10000, 100*1024)

# DS03: (10,000) 1MB files
def create_ds03():
    create_files("DS03", 10000, 1024*1024)

# DS04: (100,000) 1MB files
def create_ds04():
    create_files("DS04", 100000, 1024*1024)

# DS05: (1,000) 1GB files
def create_ds05():
    create_files("DS05", 1000, 1024*1024*1024)

# DS06: (500) 2GB files
def create_ds06():
    create_files("DS06", 500, 2*1024*1024*1024)

# DS07: (100) 10GB files
def create_ds07():
    create_files("DS07", 100, 10*1024*1024*1024)

# DS08: (200) 10GB files
def create_ds08():
    create_files("DS08", 200, 10*1024*1024*1024)

# DS09: (100) 20GB files
def create_ds09():
    create_files("DS09", 100, 20*1024*1024*1024)

# DS10: (1) 100GB file
def create_ds10():
    create_files("DS10", 1, 100*1024*1024*1024)

# DS11: (10) 100GB files
def create_ds11():
    create_files("DS11", 10, 100*1024*1024*1024)

# DS12: (20) 100GB files
def create_ds12():
    create_files("DS12", 20, 100*1024*1024*1024)

# DS13: (50) 100GB files
def create_ds13():
    create_files("DS13", 50, 100*1024*1024*1024)

# DS14: (1) 250GB file
def create_ds14():
    create_files("DS14", 1, 250*1024*1024*1024)

# DS15: (4) 250GB files
def create_ds15():
    create_files("DS15", 4, 250*1024*1024*1024)

# DS16: (10) 250GB files
def create_ds16():
    create_files("DS16", 10, 250*1024*1024*1024)

# DS17: (20) 250GB files
def create_ds17():
    create_files("DS17", 20, 250*1024*1024*1024)

create_ds05()

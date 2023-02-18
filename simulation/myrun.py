import os, sys

with open(sys.argv[1], "r") as f:
    for cmdline in f.readlines():
        cmdline = cmdline.strip("\n")
        if cmdline[0] == "#":
            continue
        os.system(cmdline)
        os.system("sleep " + str(10))
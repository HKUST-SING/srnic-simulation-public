# fat2 = ""
# fat1 = ""

# -------- 1 & 2 layers Fat Tree, 16 & 64 servers -------

# fat2_file_name = "fat2.txt"
# fat1_file_name = "fat1.txt"

# fat2 += "72 8 80\n"
# for i in range(64,72):
#     fat2 += str(i)
#     if i != 71:
#         fat2 += " "
# fat2 += "\n"

# for i in range(64):
#     if i<16:
#         line = str(i) + " " + str(64) + " 100Gbps 1000ns 0.000000\n"
#     elif i<32:
#         line = str(i) + " " + str(65) + " 100Gbps 1000ns 0.000000\n"
#     elif i < 48:
#         line = str(i) + " " + str(66) + " 100Gbps 1000ns 0.000000\n"
#     else:
#         line = str(i) + " " + str(67) + " 100Gbps 1000ns 0.000000\n"
#     fat2 += line
# for i in range(64,68):
#     for j in range(68, 72):
#         line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
#         fat2 += line
# print(fat2)

# with open(fat2_file_name, "w") as file:
#     file.write(fat2)
# file.close()

# fat1 += "17 1 16\n"
# fat1 += "16\n"
# for i in range(16):
#     line = str(i) + " 16 100Gbps 1000ns 0.000000\n"
#     fat1 += line
# print(fat1)
# with open(fat1_file_name, "w") as file1:
#     file1.write(fat1)
# file1.close()

# -------- 1 layers Fat Tree, 16 servers, 1:1 over-subscription --------
# 1 tor S
fatTree_1_16_file_name = "fatTree_1_16.txt"
fatTree_1_16 = ""
fatTree_1_16 += "17 1 16\n"
for i in range(16, 17):
    fatTree_1_16 += str(i)
    if i != 16:
        fatTree_1_16 += " "
fatTree_1_16 += "\n"

torStart = 16
for i in range(16):
    tor = int(i//16) + torStart
    line = str(i) + " " + str(tor) + " 100Gbps 1000ns 0.000000\n"
    fatTree_1_16 += line

with open(fatTree_1_16_file_name, "w") as fd_fatTree_1_16:
    fd_fatTree_1_16.write(fatTree_1_16)
fd_fatTree_1_16.close

# -------- 2 layers Fat Tree, 64 servers, 1:1 over-subscription --------
# 4 tor S, 4 agg S, 16 servers/tor
fatTree_2_64_file_name = "fatTree_2_64.txt"
fatTree_2_64 = ""
fatTree_2_64 += "72 8 80\n"
for i in range(64, 72):
    fatTree_2_64 += str(i)
    if i != 71:
        fatTree_2_64 += " "
fatTree_2_64 += "\n"

torStart = 64
for i in range(64):
    tor = int(i//16) + torStart
    line = str(i) + " " + str(tor) + " 100Gbps 1000ns 0.000000\n"
    fatTree_2_64 += line

aggStart = 68 # 64+4
for i in range(64,68):
    agg = int((i-64)//4) * 4 + aggStart
    for j in range(agg, agg+4):
        line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
        fatTree_2_64 += line

with open(fatTree_2_64_file_name, "w") as file_2_64:
    file_2_64.write(fatTree_2_64)
file_2_64.close

# -------- 2 layers Fat Tree, 256 servers, 1:1 over-subscription --------
# 8 tor S, 8 agg S, 32 servers/tor

# fatTree_2_256_file_name = "fatTree_2_256.txt"
# fatTree_2_256 = ""
# fatTree_2_256 += "272 16 320\n"
# for i in range(256, 272):
#     fatTree_2_256 += str(i)
#     if i != 271:
#         fatTree_2_256 += " "
# fatTree_2_256 += "\n"

# torStart = 256
# for i in range(256):
#     tor = int(i//32) + torStart
#     line = str(i) + " " + str(tor) + " 100Gbps 1000ns 0.000000\n"
#     fatTree_2_256 += line

# aggStart = 264 # 256+8
# for i in range(256,264):
#     agg = int((i-256)//8) * 8 + aggStart
#     for j in range(agg, agg+8):
#         line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
#         fatTree_2_256 += line

# with open(fatTree_2_256_file_name, "w") as file_2_256:
#     file_2_256.write(fatTree_2_256)
# file_2_256.close


# -------- 3 layers Fat Tree, 4096 servers, 1:1 over-subscription --------
# Pod: 8 tor S, 8 agg S, 32 servers/tor; 16 pods
fatTree_3_4096 = ""
fatTree_3_4096_file_name = "fatTree_3_4096.txt"
fatTree_3_4096 += "4416 320 6144\n"
for i in range(4096, 4416):
    fatTree_3_4096 += str(i)
    if i != 4415:
        fatTree_3_4096 += " "
fatTree_3_4096 += "\n"

torStart = 4096
for i in range(4096):
    tor = int(i//32) + torStart
    line = str(i) + " " + str(tor) + " 100Gbps 1000ns 0.000000\n"
    fatTree_3_4096 += line

aggStart = 4224 # 4096+8*16 = 4096+128
for i in range(4096,4224):
    agg = int((i-4096)//8) * 8 + aggStart
    for j in range(agg, agg+8):
        line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
        fatTree_3_4096 += line

coreStart = 4352 # 4224+8*16 = 4224+128 
for i in range(4224, 4352):
    core = int((i - 4224)%8) * 8 + coreStart
    for j in range(core, core+8):
        line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
        fatTree_3_4096 += line

with open(fatTree_3_4096_file_name, "w") as file_3_4096:
    file_3_4096.write(fatTree_3_4096)
file_3_4096.close()


# -------- 3 layers Fat Tree, 1024 servers, 1:1 over-subscription --------
# Pod: 4 tor S, 4 agg S, 16 servers/tor; 16 pods

# fatTree_3_1024 = ""
# fatTree_3_1024_file_name = "fatTree_3_1024.txt"
# fatTree_3_1024 += "1168 144 1536\n"
# for i in range(1024, 1168):
#     fatTree_3_1024 += str(i)
#     if i != 1167:
#         fatTree_3_1024 += " "
# fatTree_3_1024 += "\n"

# torStart = 1024
# for i in range(1024):
#     tor = int(i//16) + torStart
#     line = str(i) + " " + str(tor) + " 100Gbps 1000ns 0.000000\n"
#     fatTree_3_1024 += line

# aggStart = 1088 # 1024+4*16 = 1024+64
# for i in range(1024,1088):
#     agg = int((i-1024)//4) * 4 + aggStart
#     for j in range(agg, agg+4):
#         line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
#         fatTree_3_1024 += line

# coreStart = 1152 # 1088+64
# for i in range(1088, 1152):
#     core = int((i - 1088)%4) * 4 + coreStart
#     for j in range(core, core+4):
#         line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
#         fatTree_3_1024 += line

# with open(fatTree_3_1024_file_name, "w") as file_3_1024:
#     file_3_1024.write(fatTree_3_1024)
# file_3_1024.close()


# -------- 3 layers Fat Tree, 4096 servers, 4:1 over-subscription-------

# fatTree4096 = ""
# fatTree4096_file_name = 'fatTree4096.txt'
# fatTree4096 += "4400 304 5248\n"
# for i in range(4096,4400):
#     fatTree4096 += str(i)
#     if i != 4399:
#         fatTree4096 += " "
# fatTree4096 += "\n"

# torStart = 4096
# for i in range(4096):
#     tor = int(i//16) + torStart
#     line = str(i) + " " + str(tor) + " 40Gbps 1000ns 0.000000\n"
#     fatTree4096 += line

# aggStart = 4352 # 4096 + 256
# for i in range(4096,4352):
#     agg = int((i-4096)//32) * 4 + aggStart
#     for j in range(agg, agg+4):
#         line = str(i) + " " + str(j) + " 40Gbps 1000ns 0.000000\n"
#         fatTree4096 += line

# coreStart = 4384 # 4052 + 32
# for i in range(4352,4384):
#     core = int((i-4352)%4) * 4 + coreStart
#     for j in range(core, core+4):
#         line = str(i) + " " + str(j) + " 400Gbps 1000ns 0.000000\n"
#         fatTree4096 += line

# with open(fatTree4096_file_name, "w") as file:
#     file.write(fatTree4096)
# file.close


# -------- 3 layers Fat Tree, 512 servers, 4:1 over-subscription -------

# fatTree512 = ""
# fatTree512_file_name = "fatTree512.txt"
# fatTree512 += "548 36 640\n"
# for i in range(512, 548):
#     fatTree512 += str(i)
#     if i != 547:
#         fatTree512 += " "
# fatTree512 += "\n"

# torStart = 512
# for i in range(512):
#     tor = int(i//16) + torStart
#     line = str(i) + " " + str(tor) + " 40Gbps 1000ns 0.000000\n"
#     fatTree512 += line

# for i in range(512, 544):
#     for j in range(544, 548):
#         line = str(i) + " " + str(j) + " 40Gbps 1000ns 0.000000\n"
#         fatTree512 += line

# with open(fatTree512_file_name, 'w') as file:
#     file.write(fatTree512)
# file.close()


# -------- 3 layers Fat Tree with different propagation delay, 320 servers, 1:1 over-subscription -------

# fatTreeHpcc_delayDff = ""
# fatTreeHpcc_delayDff_file_name = "fatTreeHpcc_delayDff_extreme.txt"
# fatTreeHpcc_delayDff += "376 56 480\n"
# for i in range(320, 376):
#     fatTreeHpcc_delayDff += str(i)
#     if i != 376:
#         fatTreeHpcc_delayDff += " "
# fatTreeHpcc_delayDff += "\n"

# torStart = 320
# for i in range(320):
#     tor = int(i//16) + torStart
#     line = str(i) + " " + str(tor) + " 100Gbps 5000ns 0.000000\n"
#     fatTreeHpcc_delayDff += line

# aggStart = 340 # 320 + 20
# for i in range(320,340):
#     agg = int((i-320)//4) * 4 + aggStart
#     for j in range(agg, agg+4):
#         line = str(i) + " " + str(j) + " 400Gbps 5000ns 0.000000\n"
#         fatTreeHpcc_delayDff += line

# coreStart = 360 # 340 + 20
# for i in range(340, 360):
#     core = int((i - 340)%4) * 4 + coreStart
#     for j in range(core, core+4):
#         line = str(i) + " " + str(j) + " 400Gbps 40000ns 0.000000\n"
#         fatTreeHpcc_delayDff += line

# with open(fatTreeHpcc_delayDff_file_name, "w") as file:
#     file.write(fatTreeHpcc_delayDff)
# file.close()
def initial_permute(bit64):
    ini_permute = [[58,50,42,34,26,18,10,2],
                [60,52,44,36,28,20,12,4],
                [62,54,46,38,30,22,14,6],
                [64,56,48,40,32,24,16,8],
                [57,49,41,33,25,17,9,1],
                [59,51,43,35,27,19,11,3],
                [61,53,45,37,29,21,13,5],
                [63,55,47,39,31,23,15,7]]
    temp = ''
    for i in range(64):
        temp += bit64[ini_permute[i//8][i%8]-1]
    return temp


def expansion_permute(bit32):
    exp_permute = [[32,1,2,3,4,5],
                [4,5,6,7,8,9],
                [8,9,10,11,12,13],
                [12,13,14,15,16,17],
                [16,17,18,19,20,21],
                [20,21,22,23,24,25],
                [24,25,26,27,28,29],
                [28,29,30,31,32,1]]
    temp = ''
    for i in range(48):
        temp += bit32[exp_permute[i//6][i%6]-1]
    return temp


def permute_func_p(bit32):
    p = [[16,7,20,21,29,12,28,17],
        [1,15,23,26,5,18,31,10],
        [2,8,24,14,32,27,3,9],
        [19,13,30,6,22,11,4,25]]
    temp = ''
    for i in range(32):
        temp += bit32[p[i//8][i%8]-1]
    return temp


def inverse_initial_permute(bit64):
    inv = [[40,8,48,16,56,24,64,32],
        [39,7,47,15,55,23,63,31],
        [38,6,46,14,54,22,62,30],
        [37,5,45,13,53,21,61,29],
        [36,4,44,12,52,20,60,28],
        [35,3,43,11,51,19,59,27],
        [34,2,42,10,50,18,58,26],
        [33,1,41,9,49,17,57,25]]
    temp = ''
    for i in range(64):
        temp += bit64[inv[i//8][i%8]-1]
    return temp


def left_circular_shift(bit, shift):
    return bit[shift:] + bit[:shift]


def permute_choice_1(bit):
    pc = [[57,49,41,33,25,17,9],
        [1,58,50,42,34,26,18],
        [10,2,59,51,43,35,27],
        [19,11,3,60,52,44,36],
        [63,55,47,39,31,23,15],
        [7,62,54,46,38,30,22],
        [14,6,61,53,45,37,29],
        [21,13,5,28,20,12,4]]
    temp = ''
    for i in range(56):
        temp += bit[pc[i//7][i%7]-1]
    return temp


def permute_choice_2(bit):
    pc = [[14,17,11,24,1,5,3,28],
        [15,6,21,10,23,19,12,4],
        [26,8,16,7,27,20,13,2],
        [41,52,31,37,47,55,30,40],
        [51,45,33,48,44,49,39,56],
        [34,53,46,42,50,36,29,32]]
    temp = ''
    for i in range(48):
        temp += bit[pc[i//8][i%8]-1]
    return temp


def substitution_box(bit):
    s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    s = [s1, s2, s3, s4, s5, s6, s7, s8]
    result = ''
    for i in range(8):
        temp = bit[i*6: (i+1)*6]
        row = int(temp[0]+temp[5], 2)
        col = int(temp[1:5], 2)
        result += format(s[i][row][col], "04b")
    return result


def xor(a, b):
    temp = ''
    for i in range(len(a)):
        temp += str((int(a[i]) ^ int(b[i])))
    return temp


def schedule_left_shift(round):
    sls = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    return sls[round]



plain = input("Enter plain text: ")
print("The key must be 8 letters/digits long")
ikey = input("Enter key: ")  # The key must be 8 letters/digits long
cipher = []



hexcipher = ''
for i in plain:
    hexcipher += hex(ord(i))[2:] + " "
print("The plain text in hexadecimal:", hexcipher)
print()




# turn plain text into block of 64 bits
p = ""
for i in plain:
    p += format(ord(i), "08b")
plain = p

while len(plain) % 64 != 0:
    plain += "10"

p_block = []
for i in range(len(plain) // 64):
    p_block.append(plain[i*64:(i+1)*64])
print("The 64 bits blocks of plain text are :")
print(p_block)
print()

###############################################################

# turn key into 64bits binary format
k = ''
for i in ikey:
    k += format(ord(i), "08b")
ikey = k

# permute key using permute choice 1 which produce 56bits key
key = permute_choice_1(ikey)
print("\nKey before and after permute choice 1 ###########")
print(ikey)
print(key)
print()

# covert 56 bits key into two 28 bits blocks before the left shift
lkey = key[:28]
rkey = key[28:]
print("Key before and after the partition into left and right block")
print(key)
print(lkey)
print(rkey)
print()

##############################################################################

i_lkey = lkey
i_rkey = rkey
# loop through each of 64bits block
for index in range(len(p_block)):
    i = p_block[index]
    lkey = i_lkey
    rkey = i_rkey

    # initial permutation of 64bits block of plain text
    block = initial_permute(i)
    print("Block No.", index + 1, "of plain text before and after initial permutation ")
    print(i)
    print(block)
    print()

    # convert 64 bits block of plain text into two 32 bits blocks
    lblock = block[:32]
    rblock = block[32:]
    print("\nBlock of plain text before and after partition into left and right block")
    print(block)
    print(lblock)
    print(rblock)
    print()

    # start the 16 rounds of DSE
    for roundNum in range(16):

        print("\n%%%%%%  Round", roundNum + 1, "%%%%%%%%%")
        print()

        # apply circular left shift to each 28 bits block of
        print("Apply circular left shift to each 28 bits blocks of key")
        print("Left key before and after left circular shift")
        print(lkey)
        lkey = left_circular_shift(lkey, schedule_left_shift(roundNum))
        print(lkey)
        print()

        print("Right key before and after left circular shift")
        print(rkey)
        rkey = left_circular_shift(rkey, schedule_left_shift(roundNum))
        print(rkey)
        print()


        # permute the key with permute choice 2
        print("Whole key before before and after permute choice 2")
        print(lkey+rkey)
        key = permute_choice_2(lkey + rkey)
        print(key)
        print()

        ################################################################################

        # temporary holding the right block of plain text before it get manipulated
        temp_rblock = rblock

        # expand the 32 bits block of plain text into 48 bits with expansion box
        print("rblock before and after expansion")
        print(rblock)
        rblock = expansion_permute(rblock)
        print(rblock)
        print()

        # xor the right block of plain text with the key
        print("rblock before and after xor with key")
        print(rblock)
        rblock = xor(rblock, key)
        print(rblock)
        print()

        # continue pushing the right block into substitution box
        print("rblock before and after the substitution box")
        print(rblock)
        rblock = substitution_box(rblock)
        print(rblock)
        print()

        # permute the right block with permute function p
        print("rblock before and after permute p")
        print(rblock)
        rblock = permute_func_p(rblock)
        print(rblock)
        print()

        # xor the right block with the left block
        print("\nrblock before and after xor with lblock")
        print(rblock)
        rblock = xor(rblock, lblock)
        print(rblock)
        print()

        # turn the original right block into the left block
        lblock = temp_rblock
        print("left block and right block after the round")
        print("left", lblock)
        print("right", rblock)
        print()

    # swap the left block with the right block
    lblock, rblock = rblock, lblock
    print("left block and right block after swapping")
    print("left", lblock)
    print("right", rblock)
    print()

    # inverse initial permutation on the combine left and right block
    print("The 64 bits block before and after inverse initial permute")
    print(lblock + rblock)
    block = inverse_initial_permute(lblock + rblock)
    print(block)

    cipher.append(block)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("\n\n")
wcipher = ''
hexcipher = ''
for i in cipher:
    wcipher += i
for i in range(len(wcipher)//8):
    deccipher = int(wcipher[i*8: (i+1)*8], 2)
    hexcipher += hex(deccipher)[2:] + " "
print("The cipher text in hexadecimal:", hexcipher)
print()

ciphertext = ''
for i in range(len(wcipher)//8):
    deccipher = int(wcipher[i*8: (i+1)*8], 2)
    ciphertext += chr(deccipher)
print("The cipher text is :", ciphertext)



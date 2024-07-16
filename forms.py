def pyramids(nb_block, block_shape="#"):
    block_shape = " " + block_shape
    used_blocks = 0
    nb_blockr = nb_block
    nb_et = 0
    l_pr = []
    while nb_block > 0:
        used_blocks += 1
        nb_block -= used_blocks
        nb_et += 1
    if nb_block < 0:
        nb_et -= 1
        base = nb_et + 1
    else:
        base = nb_et
    for i in range(0, nb_et):
        nb_blockr2 = nb_blockr
        nb_blockr -= base
        if nb_blockr >= 0:
            chr_ = " "*(base - (base - i))
            chr_ += block_shape*base
        else:
            chr_ = " "*(base - (base - i))
            chr_ += block_shape*nb_blockr2
        l_pr.append(chr_)
        base -= 1
    for i in range (1, (len(l_pr) + 1)):
        print(l_pr[-i])
    print("level number: ", nb_et)

pyramids(36, "3")



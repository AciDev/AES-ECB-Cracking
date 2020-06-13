def getBlocks(blocks, block_size):
    new = list()
    for i in range(0, len(blocks), block_size):
        new.append(blocks[i:i+block_size])
    return new

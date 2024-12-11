# day09.py
import numpy as np
from itertools import compress

def parse(infile):
    with open(infile, 'r') as f:
        return f.read()

def main():
    infile = 'input.txt'
    
    data = parse(infile)
    # data = '2333133121414131402' # Test data
    # print(data)
    
    data = np.array([int(n) for n in data])
    files = data[::2]
    space = data[1::2]
    offset = files[0]+space[0]
    segments = np.cumsum(data)
    spacepos = segments[1::2]
    filespos = segments[::2]
    filespos2 = filespos.copy()
    checksum = 0
    backID = len(files)-1 # pointer to file
    length = files[backID] 
    part2 = True
    has_moved = [False]*len(files)
    if part2:
        # Consider files from back to front.
        for fid,fsize in enumerate(files[::-1]):
            fid = backID - fid
            # Find most suitable free location
            fits_file_idx = np.where(space>=fsize)[0]
            if len(fits_file_idx) != 0:
                left_loc = fits_file_idx[0]
                # print(f'Moving file {fid}')
                if spacepos[fid-1] > filespos[left_loc]:
                    blocks = filespos[left_loc]+np.arange(fsize)
                    checksum += sum(fid*blocks)
                    space[left_loc] -= fsize
                    has_moved[fid] = True
                    filespos[left_loc] += fsize
    
    for fid,fsize in enumerate(files):
        if not has_moved[fid]:
            blocks = np.arange(-fsize,0)+filespos2[fid]
            # print(f'File {fid} of size {fsize} at {blocks=}')
            checksum += sum(fid*blocks)

        # print(fid, fsize)
    print(checksum) # 8515929533392 too high
                   #  8515929533392
                   # 8451961488305 too high
    exit()
            
        
        
    
    # print(sum(range(0,2)))
    # print(files,space)
    # print(filespos)

    block = 0
    disk_map = ''
    
        
    # Loop over all segments with
    # Get the next file block/space block
    for fid,(fb,sb) in enumerate(zip(filespos,spacepos)):
        # Start with the file at its original location; compute checksum
        while block < fb:
            checksum += block*fid
            block += 1
            disk_map += str(fid)
        # We come in the next free space segment. 
        # Get the file that is up next for displacement
        # Move file at pointer to start
        while block < sb:
            if (length := length - 1) == -1:
                # Moving the file at end is completed, we take the subsequent file
                length = files[backID := backID -1] - 1
            disk_map += str(backID)
            checksum += backID*block
            block += 1
        # Check if the current block is past the previous file block
        if backID <= fid+1:
            # Finalize current file (leave in place, but use remaining length for checksum)
            for l in range(length):
                disk_map += str(backID)
                checksum += backID*block
                block += 1
            break
    
    print(disk_map)
    print(f'Part 1: {checksum}')


if __name__ == "__main__":
    main()
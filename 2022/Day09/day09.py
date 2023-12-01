import numpy as np
import matplotlib.pyplot as plt

def write_positions(posH, posT,N):
    """Write an array with the Head and Tails characters"""
    A = [ ['.' for _ in range(N)] for _ in range(N)]
    A = np.array(A)
    A[posT[0],posT[1]] = 'T'
    A[posH[0],posH[1]] = 'H' 

    print(np.flip(A,axis=1).T, '\n')

def interpret_move(line):
    """Read a line [{U,L,D,R}, number] to determine the move vector and number of steps"""
    move = line.split()[0]
    steps = line.split()[1]
    # Select appropriate move
    if move == 'R': move = np.array([1,0])
    elif move == 'L': move = np.array([-1,0])
    elif move == 'U': move = np.array([0, 1])
    elif move == 'D': move = np.array([0,-1])
    else: 
        print('No such move defined\n\n')
        exit()

    return move,steps

def part1(lines):
    """Compute motion of a snake with Head and Tail"""
    posH,posT = [np.array([0,0]) for _ in range(2)]

    tail_locations = np.array([posT])
    for line in lines:
        move,steps = interpret_move(line)    
        
        # Take step, and check if tail needs to follow
        for n_moves in range(int(steps)):
            posH_old = posH.copy()
            posH += move
            if np.linalg.norm(posH-posT) >= 1.5:
                posT = posH_old
            tail_locations = np.append(tail_locations,[posT],axis = 0)

    return tail_locations

def store_tail_locations(tail_locations, tail):
    """Add tail locations to a set"""
    for n,tailpos in enumerate(tail):
        tail_locations[n].add(tuple(tailpos))
    return tail_locations

def part2(lines,snake_size):
    """Simulate a snake with given size"""
    posT = np.array([0,0])
    snake = np.array([posT]*snake_size)

    # Create storage locations for the tail-visited locations
    tail_locations = [set() for _ in range(snake_size)]
    tail_locations = store_tail_locations(tail_locations,snake)

    for line in lines:
        move,steps = interpret_move(line)    
        # Iterate through the steps and store the snake each time
        for _ in range(int(steps)):
            snake = move_snake(snake,move)
            tail_locations = store_tail_locations(tail_locations,snake)

    return tail_locations

def move_snake(snake, move):
    snake_old = snake.copy()
    # Let the head move first
    snake[0] += move

    # Now let the tail follow
    for lead, posT in enumerate(snake[1:]):
        tail = lead+1

        dist = snake[lead] - snake[tail]
        # Test if lead + tail are not adjacent to each other
        # (diagonally adjacent pieces are ||dist||_2 = sqrt(2) \approx 1.42 < 1.5)
        if np.linalg.norm(dist) >= 1.5:
            # If the pieces are not adjacent, move the tail piece towards the leading piece
            # Either [+-1,0] or [0,+-1] for axis aligned moves, or [+-1,+-1] for diagonal 
            # moves. For the latter case, the dist will give [+-2,+-1], so we have to replace
            # the value of +-2 by +-1, which can be done by vector operation.
            move = dist.copy()
            move[dist==2]=1
            move[dist==-2]=-1
            snake[tail] += move
            
    return snake


if __name__ == "__main__":
    myfile = 'input.txt'

    with open(myfile, 'r') as file:
        lines = file.readlines()

    tail_locations_p1 = part1(lines)
    tail_locations_p2 = part2(lines,10)

    print('Part 1: Total steps: ',len(tail_locations_p1), 'Unique tail positions: ', len(np.unique(tail_locations_p1,axis=0)))
    print('Part 2: Unique tail positions of tail part 9: ',len(tail_locations_p2[9]))
    plt.plot(tail_locations_p1[:,0],tail_locations_p1[:,1],marker='o')
    plt.ylabel('some numbers')
    plt.show()
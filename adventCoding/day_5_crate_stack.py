
stacks = {
    1: ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
    2: ['D', 'W', 'B'],
    3:['T', 'S', 'Q', 'W', 'J', 'C'],
    4:['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
    5:['G', 'P', 'V', 'J', 'M', 'S', 'T'],
    6:['B', 'W', 'F', 'T', 'N'],
    7:['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
    8:['H', 'P', 'F', 'R'],
    9:['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H'],
}

mov_instructions ="""move 2 from 8 to 1
move 4 from 9 to 8
move 2 from 1 to 6
move 7 from 4 to 2
move 10 from 2 to 7
move 2 from 1 to 6
move 1 from 9 to 4
move 1 from 4 to 1
move 8 from 6 to 4
move 7 from 1 to 8
move 6 from 8 to 1
move 1 from 4 to 1
move 8 from 7 to 3
move 2 from 5 to 2
move 5 from 3 to 2
move 5 from 2 to 1
move 1 from 6 to 5
move 2 from 2 to 6
move 5 from 8 to 7
move 12 from 7 to 4
move 3 from 5 to 4
move 2 from 6 to 4
move 9 from 1 to 7
move 4 from 3 to 7
move 4 from 3 to 4
move 3 from 1 to 7
move 1 from 9 to 1
move 1 from 1 to 4
move 2 from 5 to 2
move 1 from 3 to 7
move 15 from 7 to 2
move 4 from 7 to 9
move 6 from 9 to 2
move 2 from 8 to 3
move 3 from 2 to 8
move 1 from 7 to 6
move 8 from 2 to 5
move 2 from 8 to 4
move 2 from 3 to 8
move 9 from 5 to 9
move 7 from 4 to 2
move 1 from 8 to 6
move 6 from 9 to 2
move 3 from 9 to 7
move 2 from 8 to 4
move 7 from 2 to 6
move 7 from 4 to 1
move 3 from 1 to 8
move 2 from 1 to 8
move 4 from 8 to 2
move 2 from 1 to 5
move 19 from 2 to 7
move 8 from 4 to 7
move 18 from 7 to 1
move 11 from 7 to 4
move 15 from 1 to 7
move 9 from 4 to 3
move 2 from 3 to 1
move 9 from 4 to 5
move 1 from 8 to 1
move 8 from 6 to 5
move 3 from 2 to 5
move 1 from 6 to 7
move 4 from 4 to 3
move 8 from 5 to 1
move 13 from 1 to 6
move 12 from 7 to 1
move 12 from 6 to 3
move 1 from 7 to 6
move 1 from 7 to 5
move 1 from 1 to 9
move 1 from 3 to 1
move 3 from 1 to 9
move 12 from 3 to 8
move 1 from 9 to 3
move 1 from 6 to 8
move 5 from 5 to 1
move 1 from 6 to 2
move 10 from 8 to 9
move 13 from 9 to 2
move 10 from 3 to 4
move 1 from 8 to 9
move 2 from 8 to 7
move 1 from 3 to 1
move 1 from 5 to 6
move 13 from 2 to 5
move 1 from 9 to 2
move 7 from 1 to 4
move 2 from 2 to 5
move 2 from 7 to 8
move 1 from 6 to 8
move 10 from 5 to 8
move 3 from 7 to 2
move 4 from 1 to 4
move 12 from 4 to 2
move 10 from 5 to 3
move 6 from 2 to 1
move 2 from 4 to 8
move 3 from 4 to 8
move 6 from 1 to 7
move 1 from 7 to 5
move 12 from 8 to 2
move 3 from 4 to 9
move 1 from 4 to 3
move 2 from 9 to 6
move 2 from 6 to 8
move 1 from 1 to 3
move 8 from 2 to 6
move 4 from 1 to 8
move 12 from 2 to 3
move 4 from 6 to 8
move 10 from 8 to 3
move 14 from 3 to 8
move 5 from 5 to 8
move 1 from 7 to 8
move 5 from 3 to 5
move 4 from 7 to 2
move 2 from 6 to 1
move 4 from 3 to 7
move 4 from 5 to 1
move 21 from 8 to 6
move 7 from 3 to 2
move 1 from 5 to 1
move 4 from 8 to 9
move 16 from 6 to 1
move 1 from 8 to 4
move 5 from 9 to 2
move 7 from 1 to 7
move 10 from 1 to 3
move 1 from 4 to 2
move 6 from 6 to 5
move 6 from 1 to 4
move 4 from 7 to 9
move 1 from 6 to 5
move 5 from 7 to 6
move 3 from 6 to 8
move 1 from 7 to 6
move 6 from 4 to 8
move 4 from 8 to 3
move 4 from 8 to 4
move 17 from 2 to 1
move 8 from 3 to 4
move 5 from 4 to 3
move 10 from 1 to 5
move 11 from 3 to 5
move 1 from 7 to 9
move 3 from 6 to 4
move 9 from 4 to 9
move 7 from 1 to 3
move 1 from 4 to 8
move 7 from 5 to 4
move 18 from 5 to 1
move 13 from 1 to 6
move 1 from 1 to 5
move 1 from 1 to 6
move 2 from 3 to 1
move 1 from 3 to 1
move 5 from 1 to 6
move 4 from 5 to 8
move 2 from 4 to 9
move 1 from 1 to 9
move 6 from 3 to 8
move 1 from 4 to 5
move 10 from 8 to 7
move 16 from 6 to 7
move 1 from 5 to 4
move 1 from 7 to 2
move 2 from 2 to 6
move 2 from 8 to 5
move 5 from 4 to 9
move 2 from 5 to 9
move 7 from 9 to 8
move 2 from 6 to 9
move 4 from 8 to 9
move 7 from 9 to 7
move 13 from 9 to 5
move 10 from 5 to 1
move 3 from 8 to 4
move 5 from 1 to 3
move 3 from 5 to 6
move 3 from 9 to 7
move 1 from 1 to 7
move 2 from 1 to 3
move 1 from 6 to 1
move 4 from 3 to 8
move 1 from 8 to 9
move 1 from 8 to 7
move 1 from 8 to 4
move 1 from 9 to 7
move 1 from 8 to 5
move 2 from 4 to 3
move 4 from 6 to 3
move 1 from 5 to 1
move 1 from 6 to 4
move 2 from 4 to 5
move 1 from 4 to 6
move 1 from 6 to 4
move 30 from 7 to 3
move 1 from 5 to 1
move 6 from 7 to 3
move 2 from 1 to 7
move 2 from 1 to 2
move 2 from 2 to 1
move 1 from 4 to 9
move 3 from 1 to 2
move 1 from 9 to 5
move 2 from 7 to 1
move 1 from 7 to 3
move 1 from 1 to 9
move 1 from 5 to 8
move 1 from 1 to 2
move 1 from 7 to 3
move 1 from 9 to 4
move 18 from 3 to 4
move 1 from 5 to 9
move 1 from 9 to 6
move 1 from 2 to 7
move 1 from 8 to 7
move 1 from 6 to 3
move 1 from 7 to 2
move 14 from 4 to 6
move 1 from 7 to 6
move 15 from 6 to 4
move 20 from 3 to 1
move 5 from 4 to 9
move 5 from 4 to 2
move 15 from 1 to 7
move 11 from 7 to 9
move 2 from 7 to 6
move 1 from 6 to 4
move 1 from 6 to 3
move 2 from 7 to 8
move 10 from 4 to 3
move 15 from 9 to 3
move 1 from 9 to 7
move 29 from 3 to 6
move 3 from 1 to 6
move 1 from 8 to 4
move 2 from 4 to 3
move 1 from 8 to 9
move 4 from 6 to 1
move 20 from 6 to 2
move 5 from 1 to 9
move 3 from 6 to 2
move 4 from 6 to 3
move 4 from 3 to 1
move 4 from 1 to 4
move 3 from 4 to 8
move 6 from 3 to 4
move 6 from 2 to 6
move 1 from 7 to 1
move 3 from 6 to 8
move 6 from 9 to 3
move 1 from 1 to 4
move 1 from 1 to 7
move 3 from 4 to 5
move 2 from 6 to 4
move 2 from 5 to 6
move 4 from 8 to 7
move 1 from 5 to 6
move 1 from 8 to 4
move 1 from 8 to 4
move 2 from 4 to 9
move 4 from 7 to 8
move 4 from 4 to 3
move 1 from 7 to 9
move 4 from 8 to 6
move 1 from 3 to 4
move 1 from 3 to 5
move 2 from 4 to 7
move 4 from 6 to 3
move 2 from 9 to 1
move 2 from 7 to 4
move 1 from 5 to 1
move 1 from 3 to 4
move 1 from 9 to 3
move 4 from 4 to 5
move 2 from 5 to 3
move 1 from 5 to 7
move 1 from 5 to 8
move 2 from 6 to 4
move 3 from 1 to 3
move 21 from 3 to 5
move 3 from 6 to 1
move 1 from 7 to 1
move 4 from 2 to 6
move 1 from 8 to 2
move 10 from 2 to 4
move 4 from 1 to 2
move 1 from 6 to 5
move 2 from 6 to 9
move 7 from 4 to 9
move 1 from 6 to 5
move 3 from 9 to 4
move 6 from 2 to 8
move 3 from 9 to 1
move 8 from 4 to 3
move 1 from 9 to 4
move 21 from 5 to 7
move 1 from 1 to 3
move 2 from 9 to 6
move 14 from 7 to 1
move 2 from 4 to 1
move 2 from 8 to 7
move 1 from 8 to 2
move 11 from 2 to 9
move 8 from 9 to 6
move 4 from 7 to 1
move 1 from 7 to 4
move 2 from 3 to 5
move 1 from 1 to 6
move 1 from 8 to 2
move 3 from 7 to 5
move 6 from 1 to 7
move 1 from 8 to 7
move 1 from 4 to 5
move 4 from 6 to 5
move 6 from 7 to 6
move 3 from 9 to 1
move 1 from 7 to 3
move 11 from 5 to 1
move 1 from 5 to 2
move 9 from 6 to 4
move 1 from 7 to 3
move 2 from 6 to 1
move 1 from 2 to 1
move 1 from 2 to 6
move 14 from 1 to 5
move 1 from 8 to 4
move 10 from 1 to 5
move 3 from 5 to 1
move 8 from 3 to 8
move 16 from 5 to 7
move 2 from 1 to 9
move 3 from 8 to 1
move 1 from 2 to 4
move 6 from 7 to 4
move 3 from 5 to 8
move 2 from 3 to 6
move 7 from 1 to 7
move 14 from 4 to 3
move 9 from 7 to 8
move 2 from 4 to 1
move 9 from 8 to 4
move 7 from 8 to 2
move 6 from 1 to 8
move 1 from 9 to 7
move 1 from 1 to 6
move 1 from 9 to 6
move 1 from 5 to 9
move 1 from 5 to 3
move 9 from 4 to 9
move 3 from 3 to 6
move 8 from 6 to 3
move 1 from 2 to 9
move 8 from 9 to 8
move 6 from 2 to 9
move 2 from 6 to 1
move 7 from 8 to 6
move 2 from 9 to 6
move 8 from 7 to 8
move 1 from 4 to 5
move 9 from 3 to 5
move 2 from 1 to 4
move 1 from 7 to 4
move 2 from 4 to 3
move 11 from 8 to 1
move 1 from 4 to 7
move 1 from 7 to 8
move 5 from 1 to 3
move 4 from 6 to 4
move 2 from 4 to 8
move 1 from 4 to 8
move 7 from 8 to 9
move 1 from 8 to 9
move 1 from 8 to 5
move 18 from 3 to 2
move 17 from 2 to 7
move 6 from 5 to 4
move 1 from 2 to 5
move 4 from 4 to 6
move 4 from 6 to 9
move 15 from 7 to 9
move 2 from 1 to 6
move 2 from 7 to 9
move 28 from 9 to 2
move 1 from 6 to 7
move 4 from 6 to 9
move 3 from 1 to 7
move 2 from 6 to 3
move 1 from 4 to 7
move 8 from 9 to 5
move 13 from 5 to 3
move 1 from 5 to 7
move 3 from 9 to 4
move 8 from 3 to 7
move 28 from 2 to 5
move 1 from 9 to 8
move 4 from 3 to 4
move 4 from 7 to 5
move 2 from 3 to 9
move 21 from 5 to 4
move 1 from 5 to 7
move 1 from 3 to 5
move 3 from 5 to 7
move 1 from 1 to 3
move 3 from 7 to 3
move 5 from 7 to 6
move 10 from 4 to 8
move 6 from 5 to 4
move 1 from 9 to 3
move 15 from 4 to 5
move 10 from 4 to 7
move 3 from 3 to 7
move 1 from 3 to 4
move 1 from 3 to 4
move 7 from 5 to 1
move 2 from 4 to 7
move 1 from 9 to 2
move 2 from 6 to 9
move 1 from 5 to 3
move 1 from 3 to 8
move 10 from 7 to 9
move 2 from 8 to 1
move 9 from 9 to 2
move 1 from 4 to 3
move 9 from 8 to 7
move 1 from 2 to 8
move 5 from 5 to 4
move 1 from 3 to 2
move 5 from 4 to 3
move 3 from 5 to 9
move 6 from 7 to 3
move 1 from 6 to 5
move 5 from 9 to 7
move 2 from 5 to 6
move 3 from 6 to 7
move 4 from 1 to 4
move 6 from 2 to 7
move 17 from 7 to 5
move 1 from 6 to 1
move 5 from 3 to 6
move 10 from 7 to 2
move 1 from 8 to 4
move 1 from 9 to 8
move 3 from 4 to 1
move 1 from 7 to 4
move 5 from 5 to 9
move 2 from 8 to 7
move 3 from 3 to 7
move 4 from 2 to 3
move 3 from 4 to 6
move 7 from 5 to 8
move 7 from 2 to 8
move 4 from 9 to 8
move 12 from 8 to 3
move 17 from 3 to 2
move 1 from 7 to 9
move 1 from 3 to 9
move 3 from 9 to 1
move 2 from 5 to 1
move 1 from 3 to 5
move 4 from 5 to 8
move 6 from 8 to 1
move 17 from 2 to 3
move 13 from 3 to 2
move 1 from 3 to 9
move 1 from 8 to 4
move 1 from 4 to 8
move 1 from 9 to 1
move 2 from 7 to 2
move 8 from 6 to 2
move 2 from 7 to 5
move 9 from 1 to 3
move 13 from 2 to 9
move 6 from 1 to 4
move 6 from 4 to 5
move 3 from 8 to 1
move 2 from 1 to 8
move 8 from 5 to 7
move 2 from 3 to 1
move 9 from 3 to 1
move 3 from 8 to 2
move 1 from 1 to 9
move 1 from 3 to 9
move 6 from 7 to 3
move 4 from 2 to 7
move 14 from 1 to 6
move 2 from 3 to 9
move 3 from 3 to 7
move 6 from 2 to 1
move 2 from 1 to 2
move 9 from 6 to 3
move 11 from 9 to 5
move 9 from 7 to 6
move 6 from 6 to 2
move 1 from 1 to 8
move 5 from 9 to 4
move 1 from 8 to 5
move 9 from 2 to 7
move 10 from 5 to 8"""

mov_list = mov_instructions.splitlines()

for move in mov_list:

    amount = 0
    move_from=0
    move_to=0
    if len(move)>18:
        amount = int(move[5]+move[6])
        move_from = int(move[13])
        move_to = int(move[18])
    else:
        amount = int(move[5])
        move_from = int(move[12])
        move_to = int(move[17])

    # amount = amount if amount>0 else 10
    temp_stack = []
    for i in range(amount):
        popped = stacks[move_from].pop()
        # stacks[move_to].append(popped)
        temp_stack.append(popped)
    
    for i in range(len(temp_stack)):
        stacks[move_to].append(temp_stack.pop())

top_crates = ""

for crates in stacks.items():
    top_crate = crates[1].pop()
    top_crates = top_crates + top_crate

print(top_crates)


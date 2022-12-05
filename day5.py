
def parse_stacks(txt_stacks: str) -> list:
    # Create list of lists from stacks text input
    txt_stacks = txt_stacks.splitlines()
    stacks = [[] for _ in range((len(txt_stacks[0]) // 4) + 1)]
    for line in txt_stacks:
        i_col = 0
        i = 1
        while i < len(line):
            if line[i] != ' ':
                stacks[i_col].insert(0, line[i])
            i += 4
            i_col += 1
    return stacks

def parse_instructions(txt_instructions: str) -> list:
    # Create list of instructions from text input in format:
    # [number_of_moves, from_stack, to_stack]
    # Also sack off the 1 indexing and convert to 0 indexing.
    output_instructions = []
    for line in txt_instructions.splitlines():
        line = line.replace("move ", "")
        line = line.replace(" from ", ",")
        line = line.replace(" to ", ",")
        output_instructions.append([int(x) for x in line.split(",")])
        output_instructions[-1][1] = output_instructions[-1][1] - 1
        output_instructions[-1][2] = output_instructions[-1][2] - 1

    return output_instructions

def top_crates_poppush(txt_stacks: str, txt_instructions: str) -> str:
    # Move stuff between stacks by popping and pushing (appending) between stacks.
    stacks = parse_stacks(txt_stacks)
    instructions = parse_instructions(txt_instructions)
    print_stacks(stacks)
    for inst in instructions:
        move_count = inst[0]
        from_stack = inst[1]
        to_stack = inst[2]
        while move_count > 0:
            m = stacks[from_stack].pop()
            stacks[to_stack].append(m)
            move_count -= 1
    output_string = ""
    for stack in stacks:
        output_string = output_string + stack[-1]
    print_stacks(stacks)
    return output_string

def top_crates_inchunks(txt_stacks: str, txt_instructions: str) -> str:
    # Move stuff between stacks by gathering the stuff from the source list to 
    # be moved into a helper list and sticking that on the end of the destination list.
    stacks = parse_stacks(txt_stacks)
    instructions = parse_instructions(txt_instructions)
    print("")
    for inst in instructions:
        move_count = inst[0]
        from_stack = inst[1]
        to_stack = inst[2]
        m = []
        while move_count > 0:
            m.insert(0, stacks[from_stack].pop())
            move_count -= 1
        stacks[to_stack] = stacks[to_stack] + m
       
    output_string = ""
    for stack in stacks:
        output_string = output_string + stack[-1]
    
    print_stacks(stacks)
    return output_string



def print_stacks(stacks):
    # function to print the stacks for debugging.
    tallest = 0
    num_stacks = len(stacks)

    for s in stacks:
        if len(s) > tallest:
            tallest = len(s)

    for i in range(tallest, -1, -1):
        line = ""
        for s in stacks:
            if i < len(s):
                line = line + f"[{s[i]}] "
            else:
                line = line + "    "
        print(line)

    numbers_row = ""
    for i in range(num_stacks):
        numbers_row = numbers_row + f" {i}  "
    print(numbers_row)


        

def main():
    print(top_crates_poppush(STACKS, INSTRUCTIONS))
    print(top_crates_inchunks(STACKS, INSTRUCTIONS))

STACKS = """[T]             [P]     [J]        
[F]     [S]     [T]     [R]     [B]
[V]     [M] [H] [S]     [F]     [R]
[Z]     [P] [Q] [B]     [S] [W] [P]
[C]     [Q] [R] [D] [Z] [N] [H] [Q]
[W] [B] [T] [F] [L] [T] [M] [F] [T]
[S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
[Q] [Q] [B] [D] [J] [W] [H] [R] [J]"""

INSTRUCTIONS = """move 3 from 8 to 2
move 3 from 1 to 5
move 3 from 1 to 4
move 2 from 7 to 4
move 3 from 7 to 4
move 8 from 5 to 7
move 2 from 1 to 8
move 7 from 3 to 2
move 1 from 5 to 2
move 1 from 6 to 7
move 2 from 5 to 9
move 1 from 9 to 1
move 3 from 9 to 6
move 5 from 6 to 2
move 10 from 7 to 2
move 3 from 8 to 9
move 7 from 9 to 2
move 1 from 1 to 2
move 1 from 9 to 6
move 1 from 4 to 1
move 1 from 8 to 2
move 11 from 4 to 2
move 1 from 7 to 9
move 1 from 4 to 6
move 1 from 9 to 7
move 1 from 1 to 3
move 1 from 7 to 5
move 1 from 4 to 9
move 1 from 5 to 2
move 1 from 3 to 8
move 1 from 6 to 9
move 1 from 8 to 6
move 11 from 2 to 1
move 1 from 6 to 8
move 7 from 2 to 1
move 14 from 2 to 7
move 1 from 6 to 3
move 1 from 8 to 2
move 1 from 3 to 9
move 7 from 7 to 1
move 1 from 6 to 5
move 5 from 7 to 6
move 4 from 2 to 8
move 3 from 6 to 7
move 3 from 7 to 8
move 9 from 1 to 3
move 8 from 3 to 7
move 1 from 3 to 1
move 2 from 2 to 3
move 1 from 6 to 7
move 2 from 1 to 7
move 7 from 1 to 6
move 1 from 3 to 5
move 2 from 5 to 3
move 7 from 6 to 3
move 9 from 7 to 5
move 1 from 9 to 1
move 4 from 8 to 5
move 7 from 1 to 5
move 4 from 7 to 2
move 1 from 7 to 8
move 1 from 6 to 4
move 10 from 5 to 3
move 8 from 5 to 1
move 2 from 8 to 3
move 2 from 8 to 9
move 8 from 2 to 7
move 4 from 9 to 8
move 13 from 3 to 7
move 1 from 5 to 3
move 6 from 3 to 9
move 10 from 1 to 9
move 1 from 3 to 4
move 6 from 9 to 7
move 1 from 5 to 8
move 14 from 7 to 6
move 14 from 6 to 1
move 13 from 1 to 8
move 1 from 1 to 2
move 9 from 8 to 9
move 6 from 8 to 5
move 2 from 4 to 6
move 1 from 8 to 1
move 2 from 2 to 1
move 2 from 8 to 6
move 3 from 1 to 2
move 3 from 3 to 9
move 16 from 9 to 1
move 3 from 2 to 4
move 3 from 7 to 2
move 6 from 5 to 4
move 5 from 7 to 3
move 4 from 6 to 1
move 10 from 2 to 9
move 13 from 9 to 1
move 5 from 7 to 2
move 2 from 4 to 6
move 1 from 9 to 1
move 2 from 9 to 5
move 2 from 6 to 8
move 2 from 5 to 3
move 1 from 8 to 3
move 31 from 1 to 7
move 2 from 1 to 5
move 12 from 7 to 3
move 11 from 3 to 2
move 1 from 8 to 4
move 6 from 4 to 5
move 1 from 3 to 4
move 8 from 3 to 2
move 5 from 5 to 6
move 2 from 6 to 7
move 4 from 7 to 3
move 1 from 6 to 9
move 13 from 7 to 6
move 13 from 2 to 3
move 1 from 4 to 8
move 10 from 2 to 3
move 3 from 7 to 3
move 2 from 2 to 1
move 1 from 8 to 2
move 2 from 4 to 7
move 1 from 9 to 2
move 3 from 7 to 3
move 1 from 5 to 1
move 2 from 5 to 2
move 15 from 6 to 7
move 4 from 1 to 9
move 22 from 3 to 9
move 7 from 3 to 9
move 4 from 3 to 8
move 4 from 9 to 4
move 3 from 2 to 4
move 5 from 7 to 1
move 7 from 4 to 7
move 2 from 8 to 4
move 1 from 4 to 8
move 3 from 1 to 5
move 2 from 1 to 4
move 1 from 2 to 9
move 2 from 5 to 7
move 1 from 5 to 9
move 3 from 8 to 6
move 8 from 7 to 1
move 6 from 7 to 1
move 10 from 1 to 9
move 3 from 6 to 2
move 2 from 1 to 3
move 2 from 3 to 6
move 3 from 7 to 4
move 2 from 7 to 1
move 1 from 2 to 5
move 13 from 9 to 5
move 12 from 9 to 3
move 6 from 5 to 3
move 2 from 9 to 1
move 11 from 9 to 3
move 1 from 4 to 6
move 2 from 5 to 3
move 1 from 1 to 8
move 24 from 3 to 5
move 2 from 9 to 3
move 2 from 2 to 4
move 1 from 9 to 2
move 2 from 6 to 8
move 5 from 3 to 5
move 2 from 8 to 9
move 1 from 9 to 8
move 4 from 1 to 4
move 1 from 9 to 4
move 1 from 8 to 4
move 1 from 8 to 4
move 7 from 4 to 5
move 1 from 1 to 8
move 1 from 6 to 5
move 35 from 5 to 4
move 18 from 4 to 3
move 6 from 4 to 3
move 8 from 5 to 8
move 8 from 8 to 1
move 2 from 4 to 9
move 23 from 3 to 1
move 1 from 8 to 5
move 1 from 9 to 1
move 1 from 5 to 1
move 1 from 9 to 4
move 11 from 1 to 2
move 16 from 4 to 5
move 3 from 3 to 5
move 9 from 2 to 5
move 1 from 4 to 1
move 2 from 2 to 6
move 1 from 2 to 9
move 1 from 6 to 2
move 1 from 3 to 5
move 1 from 3 to 9
move 1 from 2 to 9
move 23 from 1 to 5
move 1 from 6 to 9
move 1 from 9 to 8
move 27 from 5 to 1
move 1 from 9 to 3
move 18 from 5 to 8
move 6 from 5 to 7
move 1 from 5 to 6
move 1 from 9 to 8
move 12 from 8 to 3
move 1 from 1 to 4
move 6 from 7 to 8
move 1 from 6 to 3
move 1 from 4 to 2
move 2 from 1 to 8
move 1 from 2 to 9
move 8 from 3 to 2
move 2 from 9 to 7
move 5 from 2 to 7
move 7 from 7 to 2
move 2 from 8 to 2
move 3 from 1 to 9
move 5 from 1 to 2
move 3 from 9 to 8
move 3 from 8 to 7
move 5 from 2 to 5
move 2 from 7 to 6
move 12 from 8 to 9
move 12 from 1 to 4
move 9 from 9 to 3
move 4 from 5 to 8
move 12 from 3 to 8
move 1 from 7 to 9
move 3 from 9 to 2
move 1 from 4 to 7
move 3 from 1 to 7
move 7 from 4 to 6
move 3 from 6 to 2
move 2 from 7 to 9
move 18 from 8 to 1
move 2 from 4 to 7
move 1 from 2 to 8
move 1 from 8 to 2
move 10 from 2 to 3
move 3 from 9 to 8
move 2 from 6 to 7
move 13 from 3 to 1
move 2 from 8 to 9
move 28 from 1 to 8
move 1 from 5 to 2
move 1 from 4 to 3
move 4 from 7 to 6
move 5 from 6 to 7
move 7 from 2 to 6
move 1 from 9 to 6
move 2 from 2 to 4
move 1 from 9 to 1
move 4 from 1 to 2
move 3 from 2 to 5
move 3 from 4 to 9
move 3 from 5 to 7
move 1 from 1 to 4
move 6 from 7 to 6
move 1 from 2 to 6
move 1 from 4 to 1
move 1 from 1 to 8
move 3 from 9 to 4
move 18 from 6 to 3
move 4 from 3 to 6
move 1 from 7 to 9
move 1 from 6 to 9
move 2 from 3 to 6
move 1 from 9 to 6
move 1 from 9 to 2
move 6 from 6 to 8
move 3 from 4 to 7
move 2 from 7 to 2
move 35 from 8 to 7
move 3 from 3 to 1
move 26 from 7 to 2
move 10 from 3 to 9
move 6 from 9 to 4
move 3 from 1 to 2
move 1 from 4 to 3
move 4 from 4 to 1
move 1 from 3 to 6
move 1 from 8 to 3
move 1 from 6 to 2
move 1 from 3 to 2
move 13 from 7 to 3
move 3 from 1 to 4
move 4 from 3 to 1
move 3 from 1 to 9
move 2 from 1 to 9
move 10 from 2 to 9
move 19 from 2 to 9
move 6 from 3 to 9
move 2 from 3 to 4
move 2 from 2 to 6
move 17 from 9 to 8
move 1 from 2 to 8
move 2 from 9 to 3
move 2 from 6 to 7
move 8 from 9 to 3
move 5 from 4 to 5
move 14 from 9 to 4
move 1 from 2 to 3
move 1 from 7 to 2
move 2 from 9 to 3
move 1 from 2 to 7
move 5 from 5 to 1
move 1 from 2 to 1
move 1 from 3 to 1
move 1 from 9 to 7
move 3 from 7 to 2
move 3 from 3 to 7
move 1 from 2 to 4
move 1 from 3 to 8
move 1 from 2 to 4
move 4 from 3 to 4
move 16 from 8 to 9
move 3 from 1 to 4
move 21 from 4 to 6
move 1 from 7 to 2
move 1 from 8 to 2
move 1 from 1 to 3
move 6 from 6 to 7
move 3 from 1 to 9
move 3 from 7 to 3
move 1 from 4 to 6
move 1 from 4 to 7
move 2 from 2 to 6
move 1 from 8 to 6
move 13 from 6 to 7
move 1 from 2 to 3
move 15 from 9 to 8
move 6 from 6 to 3
move 13 from 8 to 3
move 4 from 9 to 4
move 5 from 4 to 8
move 19 from 3 to 9
move 3 from 3 to 1
move 5 from 8 to 9
move 17 from 9 to 7
move 1 from 1 to 8
move 4 from 9 to 6
move 3 from 3 to 8
move 1 from 1 to 2
move 3 from 3 to 1
move 36 from 7 to 6
move 1 from 1 to 2
move 7 from 8 to 2
move 24 from 6 to 5
move 2 from 6 to 7
move 1 from 3 to 2
move 4 from 6 to 8
move 19 from 5 to 1
move 8 from 6 to 4
move 7 from 2 to 5
move 3 from 2 to 8
move 15 from 1 to 6
move 2 from 9 to 5
move 2 from 7 to 8
move 3 from 4 to 1
move 4 from 5 to 6
move 1 from 9 to 7
move 1 from 8 to 3
move 3 from 6 to 1
move 2 from 4 to 7
move 13 from 1 to 8
move 1 from 3 to 7
move 1 from 4 to 5
move 19 from 8 to 6
move 1 from 7 to 3
move 8 from 5 to 8
move 1 from 6 to 8
move 3 from 5 to 9
move 1 from 6 to 4
move 3 from 4 to 7
move 1 from 3 to 9
move 4 from 7 to 9
move 20 from 6 to 3
move 1 from 8 to 4
move 2 from 9 to 4
move 2 from 9 to 2
move 2 from 9 to 3
move 13 from 6 to 9
move 9 from 9 to 8
move 2 from 6 to 3
move 8 from 8 to 2
move 2 from 7 to 3
move 5 from 9 to 3
move 12 from 3 to 5
move 1 from 4 to 7
move 8 from 2 to 4
move 8 from 4 to 7
move 2 from 2 to 6
move 2 from 8 to 9
move 2 from 6 to 8
move 2 from 9 to 6
move 2 from 6 to 9
move 2 from 4 to 8
move 2 from 9 to 2
move 6 from 3 to 1
move 2 from 2 to 9
move 3 from 9 to 3
move 8 from 7 to 2
move 6 from 1 to 2
move 8 from 3 to 8
move 1 from 7 to 3
move 5 from 3 to 8
move 6 from 2 to 7
move 3 from 7 to 6
move 2 from 7 to 9
move 1 from 7 to 8
move 8 from 5 to 7
move 7 from 2 to 1
move 7 from 1 to 6
move 7 from 7 to 9
move 1 from 7 to 6
move 2 from 3 to 9
move 2 from 8 to 5
move 25 from 8 to 5
move 5 from 5 to 1
move 1 from 6 to 4
move 17 from 5 to 4
move 5 from 5 to 4
move 23 from 4 to 7
move 2 from 5 to 2
move 4 from 6 to 3
move 6 from 3 to 7
move 1 from 5 to 2
move 1 from 1 to 7
move 2 from 2 to 8
move 2 from 2 to 9
move 1 from 5 to 7
move 4 from 1 to 6
move 2 from 8 to 3
move 2 from 9 to 4
move 1 from 4 to 8
move 7 from 9 to 1
move 2 from 3 to 5
move 28 from 7 to 4
move 4 from 6 to 2
move 2 from 6 to 2
move 3 from 7 to 4
move 2 from 5 to 6
move 4 from 2 to 6
move 9 from 6 to 5
move 4 from 1 to 7
move 1 from 6 to 2
move 3 from 2 to 3
move 1 from 8 to 6
move 1 from 7 to 4
move 2 from 3 to 4
move 1 from 7 to 4
move 2 from 1 to 6
move 1 from 7 to 9
move 1 from 7 to 9
move 1 from 6 to 2
move 7 from 5 to 8
move 1 from 3 to 9
move 1 from 5 to 2
move 7 from 8 to 7
move 4 from 4 to 8
move 2 from 8 to 4
move 2 from 2 to 7
move 1 from 1 to 7
move 1 from 5 to 6
move 32 from 4 to 7
move 2 from 6 to 5
move 2 from 8 to 2
move 1 from 2 to 1
move 2 from 5 to 4
move 1 from 2 to 5
move 1 from 1 to 4
move 4 from 4 to 3
move 1 from 6 to 4
move 1 from 5 to 4
move 5 from 9 to 1
move 4 from 3 to 5
move 3 from 1 to 6
move 2 from 9 to 5
move 2 from 1 to 3
move 15 from 7 to 1
move 5 from 5 to 3
move 1 from 5 to 2
move 3 from 4 to 5
move 2 from 5 to 9
move 3 from 3 to 6
move 3 from 3 to 4
move 1 from 3 to 8
move 1 from 9 to 3
move 2 from 4 to 9
move 1 from 5 to 3
move 2 from 9 to 6
move 1 from 8 to 1
move 1 from 3 to 2
move 1 from 4 to 9
move 2 from 9 to 3
move 9 from 1 to 3
move 5 from 3 to 4
move 2 from 1 to 3
move 4 from 1 to 5
move 1 from 2 to 8
move 3 from 4 to 9"""


if __name__ == "__main__":
    main()



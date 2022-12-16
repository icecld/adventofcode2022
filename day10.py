
class CPU():
    def __init__(self) -> None:
        self.registers = {"X": 1}
        self.cycles = 0
        self.running_sum = 0

    def render_pixel(self):
        x_pos = self.cycles % 40
        if x_pos == 0:
            nl = "\n"
        else:
            nl = ""
        if x_pos-1 in [self.registers["X"]+1, self.registers["X"], self.registers["X"]-1]:
            print("██", end=nl)
        else:
            print("  ", end=nl)
    
    def cycle_interrupt(self) -> None:
        if (self.cycles - 20) % 40 == 0:
            self.running_sum += (self.cycles * self.registers["X"])
    
    def inc_cycle(self, count) -> None:
        for _ in range(count):
            self.cycles += 1
            self.cycle_interrupt()
            self.render_pixel()

    # CPU INSTRUCTIONS:
    def i_noop(self, operand) -> None:
        self.inc_cycle(1)
    
    def i_addx(self, operand) -> None:
        self.inc_cycle(2)
        self.registers["X"] += operand

    # DECODE & EXECUTE
    def decode_execute(self, instruction):
        instruction_set = {"noop": self.i_noop, "addx": self.i_addx}

        operation = instruction[0:4]
        if len(instruction) > 4:
            operand = int(instruction[5:])
        else:
            operand = None

        instruction_set[operation](operand)



def main() -> None:
    cpu = CPU()
    for line in INPUT.splitlines():
        cpu.decode_execute(line)
    print(cpu.running_sum)





INPUT = """noop
addx 26
addx -21
addx 2
addx 3
noop
noop
addx 23
addx -17
addx -1
noop
noop
addx 7
noop
addx 3
addx 1
noop
noop
addx 2
noop
addx 7
noop
addx -12
addx 13
addx -38
addx 5
addx 34
addx -2
addx -29
addx 2
addx 5
addx 2
addx 3
addx -2
addx -1
addx 8
addx 2
addx 6
addx -26
addx 23
addx -26
addx 33
addx 2
addx -37
addx -1
addx 1
noop
noop
noop
addx 5
addx 5
addx 3
addx -2
addx 2
addx 5
addx 5
noop
noop
addx -2
addx 4
noop
noop
noop
addx 3
noop
noop
addx 7
addx -1
addx -35
addx -1
addx 5
addx 3
noop
addx 4
noop
noop
noop
noop
noop
addx 5
addx 1
noop
noop
noop
addx -7
addx 12
addx 2
addx 7
noop
addx -2
noop
noop
addx 7
addx 2
addx -39
noop
noop
addx 5
addx 2
addx -4
addx 25
addx -18
addx 7
noop
addx -2
addx 5
addx 2
addx 6
addx -5
addx 2
addx -22
addx 29
addx -21
addx -7
addx 31
addx 2
noop
addx -36
addx 1
addx 5
noop
addx 1
addx 4
addx 5
noop
noop
noop
addx 3
noop
addx -13
addx 15
noop
addx 5
noop
addx 1
noop
addx 3
addx 2
addx 4
addx 3
noop
addx -3
noop"""

if __name__ == "__main__":
    main()
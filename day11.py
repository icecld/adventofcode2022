class monkey():
    def __init__(self, definition_txt: str) -> None:

        self.items_inspected = 0

        for line_num, line in enumerate(definition_txt.splitlines()):
            if line_num == 1:
                self._items = [int(x) for x in line[18:].split(", ")]
            elif line_num == 2:
                op = line[20:].split(" ")
                self.operation = self.generate_lambda(op[1], op[2])
            elif line_num == 3:
                self.test_mod = int(line[21:])
            elif line_num == 4:
                self.test_true = int(line[-1])
            elif line_num == 5:
                self.test_false = int(line[-1])

    def generate_lambda(self, op: str, operand: str):
        ops = {
            "*":       lambda a, b: a * b,
            "+":       lambda a, b: a + b
        }
        if operand != "old":
            return lambda x: ops[op](x, int(operand))
        else:
            return lambda x: ops[op](x, x)
    
    def pickup_and_inspect_item(self):
        self.items_inspected += 1
        item = self._items.pop(0)
        item = self.operation(item)
        #item = item // 3

        if item % self.test_mod == 0:
            return item, self.test_true
        else:
            return item, self.test_false
    
    def add_item(self, item: int) -> None:
        self._items.append(item)
    
    def items_exist(self) -> bool:
        if len(self._items) == 0:
            return False
        else:
            return True



def monkey_throws(input: str, rounds: int=20) -> int:
    monkey_txts = input.split("\n\n")
    monkeys = []
    for txt in monkey_txts:
        monkeys.append(monkey(txt))
    
    global_mod = 1
    for n in [m.test_mod for m in monkeys]:
        global_mod = global_mod * n
            # because fuck you, that's why.


    for round in range(rounds):
        for m in monkeys:
            while m.items_exist():
                item, throw_index = m.pickup_and_inspect_item()
                item = item % global_mod
                monkeys[throw_index].add_item(item)

        if round % 20 == 0:
            print(f"Round {round}")

    monkey_scores = []
    for m in monkeys:
        monkey_scores.append(m.items_inspected)

    monkey_business = [0, 0]
    for score in monkey_scores:
        for i, n in enumerate(monkey_business):
            if score > n:
                monkey_business.insert(i, score)
                del monkey_business[-1]
                break
    
    return monkey_business[0] * monkey_business[1]





def main():
    print(monkey_throws(INPUT, rounds=10000))





INPUT = """Monkey 0:
  Starting items: 65, 78
  Operation: new = old * 3
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 78, 86, 79, 73, 64, 85, 88
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 2:
  Starting items: 69, 97, 77, 88, 87
  Operation: new = old + 2
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 3:
  Starting items: 99
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 5

Monkey 4:
  Starting items: 60, 57, 52
  Operation: new = old * 19
  Test: divisible by 7
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 5:
  Starting items: 91, 82, 85, 73, 84, 53
  Operation: new = old + 5
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 6:
  Starting items: 88, 74, 68, 56
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 7:
  Starting items: 54, 82, 72, 71, 53, 99, 67
  Operation: new = old + 1
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0"""

if __name__ == "__main__":
    main()
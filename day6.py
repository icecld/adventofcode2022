
def find_first_n_distinct(input: str, n: int) -> int:
    buffer = [None] * n
    for i, char in enumerate(input):
        buffer.pop()
        buffer.insert(0,char)
        if len(buffer) == len(set(buffer)) and i > 3:
            return i + 1



def main():
    print(find_first_n_distinct(INPUT, 4))
    print(find_first_n_distinct(INPUT, 14))

def read_input(file):
    with open(file) as f:
        return f.read()


INPUT = read_input("day6_input.txt")

if __name__ == "__main__":
    main()
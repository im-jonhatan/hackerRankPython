if __name__ == '__main__':
    N = int(input())
    List = []
    for _ in range(N):
        Command = list(map(str, input().rstrip().split()))
        if Command[0] == "insert":
            List.insert(int(Command[1]), int(Command[2]))
        elif Command[0] == "print":
            print(List)
        elif Command[0] == "remove":
            List.remove(int(Command[1]))
        elif Command[0] == "append":
            List.append(int(Command[1]))
        elif Command[0] == "sort":
            List.sort()
        elif Command[0] == "pop":
            List.pop()
        elif Command[0] == "reverse":
            List.reverse()
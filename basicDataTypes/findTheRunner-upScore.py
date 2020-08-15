if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr= list(dict.fromkeys(arr))
    arr.sort()
    print(arr[-2])
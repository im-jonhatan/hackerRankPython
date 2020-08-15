if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)

    scores = list(dict.fromkeys(scores))
    scores.sort()
    low = scores[1]
    students.sort()
    for student in students:
        if student[1] == low:
            print(student[0])
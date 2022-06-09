if __name__ == "__main__":
    students = []
    totalScore = []
    names = []

    for _ in range(int(input())):
        stud = []
        name = input()
        stud.append(name)
        score = float(input())
        stud.append(score)
        totalScore.append(score)
        students.append(stud)

    ts = sorted(totalScore)

    for i in range(len(students)):
        if ts[i] < ts[i + 1]:
            secLowest = ts[i + 1]
            break

    for i in range(len(students)):
        if secLowest == students[i][1]:
            names.append(students[i][0])

    names.sort()
    for i in range(len(names)):
        print(names[i])

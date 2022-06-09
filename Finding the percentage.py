import math

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in range(n):
        if query_name == list(student_marks.keys())[i]:
            s = sum(list(student_marks.values())[i]) / len(
                list(student_marks.values())[i]
            )
    print("%.2f" % s)

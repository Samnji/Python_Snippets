#Students marks averaging showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    list_of_marks = student_marks[query_name]

    marks = 0

    for mark in list_of_marks:
        marks = marks + mark


    avg = marks / len(list_of_marks)
    
    print("%.2f" % avg)
    



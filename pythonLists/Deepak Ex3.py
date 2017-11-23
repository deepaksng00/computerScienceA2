# Deepak Singh
# Ex.3

students = []
markList = []
sortedMarks = []


def __init__():
    studentName = input('Please enter your name: ')
    students.append(studentName)
    for i in range(10):
        mark = int(input('Please enter your mark: '))
        markList.append(mark)
    sortedMarks = sorted(markList, reverse = True)
    return sortedMarks

sortedMarks = (__init__())

size = len(sortedMarks)
totMarks = 0

for i in sortedMarks:
    totMarks += i

avrMark = totMarks / size

print("Student name:" , students[0])
print("Student average mark:", avrMark)
print("Student top 3 marks:", sortedMarks[0:2])
print("Student bottom 3 marks:", sortedMarks[size-4:size-1])


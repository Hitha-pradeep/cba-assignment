# Store marks in a list (array in Python)
marks = [78, 45, 89, 32, 91, 67, 55]
print("All Marks:", marks)

highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark
print("Highest Mark:", highest)

lowest = marks[0]
for mark in marks:
    if mark < lowest:
        lowest = mark
print("Lowest Mark:", lowest)

sum_marks = 0
for mark in marks:
    sum_marks += mark
average = sum_marks / len(marks)
print("Average Marks:", round(average, 2))

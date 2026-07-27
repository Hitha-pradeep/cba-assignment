# Student Marks Dashboard
def analyze_marks(marks):
    print("Marks of all students:", marks)
    topper = max(marks)
    average = sum(marks) / len(marks)
    above_75 = sum(1 for m in marks if m > 75)
    print("===================================")
    print(f"Topper's Mark     : {topper}")
    print(f"Class Average     : {average:.2f}")
    print(f"Students > 75     : {above_75}")
    print("===================================")
def main():
    marks = []
    for i in range(10):
        mark = int(input(f"Enter marks for Student {i+1}: "))
        marks.append(mark)
    analyze_marks(marks)
if __name__ == "__main__":
    main()

import csv


def create_grades_csv():
    """Create grades.csv by collecting student names and exam scores."""

    num_students = int(input("How many students do you want to enter? "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        for _ in range(num_students):
            print("\nEnter student information:")
            first = input("First name: ")
            last = input("Last name: ")
            exam1 = int(input("Exam 1: "))
            exam2 = int(input("Exam 2: "))
            exam3 = int(input("Exam 3: "))

            writer.writerow([first, last, exam1, exam2, exam3])

    print("\ngrades.csv created successfully.")


create_grades_csv()

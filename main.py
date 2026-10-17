
import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    check_result,
    highest_average,
    lowest_average,
    class_average,
    find_top_students
)


def main():
    print("=" * 65)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)

    # Load student data from CSV
    data = pd.read_csv("students.csv")

    print("\n1. STUDENT DATASET")
    print("-" * 65)
    print(data.to_string(index=False))

    # Select subject columns
    subjects = ["Python", "Maths", "Computer"]

    # Calculate total, average, grade and result for every student
    totals = []
    averages = []
    grades = []
    results = []

    for index, row in data.iterrows():
        marks = [row[subject] for subject in subjects]

        total = calculate_total(marks)
        average = calculate_average(marks)
        grade = calculate_grade(average)
        result = check_result(marks)

        totals.append(total)
        averages.append(average)
        grades.append(grade)
        results.append(result)

    data["Total"] = totals
    data["Average"] = np.round(averages, 2)
    data["Grade"] = grades
    data["Result"] = results

    # Display student-wise analysis
    print("\n2. STUDENT PERFORMANCE REPORT")
    print("-" * 65)
    print(
        data[
            ["Student_ID", "Name", "Total",
             "Average", "Grade", "Result"]
        ].to_string(index=False)
    )

    # Overall class statistics
    print("\n3. CLASS PERFORMANCE")
    print("-" * 65)

    high = highest_average(data["Average"].to_numpy())
    low = lowest_average(data["Average"].to_numpy())
    overall = class_average(data["Average"].to_numpy())

    print(f"Total students: {len(data)}")
    print(f"Class average: {overall:.2f}")
    print(f"Highest student average: {high:.2f}")
    print(f"Lowest student average: {low:.2f}")

    # Pass and fail statistics
    passed = 0
    failed = 0

    for result in data["Result"]:
        if result == "Pass":
            passed += 1
        else:
            failed += 1

    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")

    # Subject-wise analysis
    print("\n4. SUBJECT-WISE PERFORMANCE")
    print("-" * 65)

    subject_averages = data[subjects].mean()

    for subject, average in subject_averages.items():
        print(f"{subject} average: {average:.2f}")

    best_subject = subject_averages.idxmax()
    print(f"Best-performing subject: {best_subject}")

    # Top-performing students
    print("\n5. TOP-PERFORMING STUDENT(S)")
    print("-" * 65)

    top_students = find_top_students(data)

    for _, student in top_students.iterrows():
        print(
            f"Name: {student['Name']} | "
            f"Average: {student['Average']:.2f} | "
            f"Grade: {student['Grade']}"
        )

    # Attendance analysis
    print("\n6. ATTENDANCE ANALYSIS")
    print("-" * 65)

    print(
        f"Class attendance average: "
        f"{np.mean(data['Attendance']):.2f}%"
    )

    low_attendance = data[data["Attendance"] < 75]

    print(
        f"Students with attendance below 75%: "
        f"{len(low_attendance)}"
    )

    print("\n" + "=" * 65)
    print("          ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 65)


if __name__ == "__main__":
    main()


import numpy as np

# Calculate total marks of a student
def calculate_total(marks):
    return sum(marks)


# Calculate average marks of a student
def calculate_average(marks):
    return np.mean(marks)


# Assign grade based on average marks
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Check whether a student passed or failed
# Passing marks: 40 in every subject
def check_result(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"
    return "Pass"


# Find the highest average
def highest_average(averages):
    return np.max(averages)


# Find the lowest average
def lowest_average(averages):
    return np.min(averages)


# Calculate overall class average
def class_average(averages):
    return np.mean(averages)


# Find top-performing students
def find_top_students(data):
    highest = data["Average"].max()
    return data[data["Average"] == highest]

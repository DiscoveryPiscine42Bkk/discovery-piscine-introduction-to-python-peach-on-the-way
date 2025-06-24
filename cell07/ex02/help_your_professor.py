#!/usr/bin/env python3

# • Create a script called help_your_professor.py.
# • It will contain a method called average.
# • This method will take a dictionary as a parameter, associating the students’ first
# names with their scores on an assignment, and calculate the class average for that
# assignment.
# • For example, the following script:
# # your method definition here
# class_3B = {
# "marine": 18,
# "jean": 15,
# "coline": 8,
# "luc": 9
# }
# class_3C = {
# "quentin": 17,
# "julie": 15,
# "marc": 8,
# "stephanie": 13
# }
# print(f"Average for class 3B: {average(class_3B)}.")
# print(f"Average for class 3C: {average(class_3C)}.")
# Will have the following output:
# ?> ./help_your_professor.py
# Average for class 3B: 12.5.
# Average for class 3C: 13.25.
# ?>

def average(student_scores):
    scores = student_scores.values()
    return sum(scores) / len(scores)

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")

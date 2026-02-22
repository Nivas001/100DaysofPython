#key:value --> dictionary

marks = {
    "Tamil": 89,
    "English": 97,
    "Maths": 95,
    "Science": 82,
    "Social": 78,
}



students_grade = {

}

def grades_convert(mark):
    if 90 <= mark <= 100:
        return "Outstanding"
    elif 80<= mark < 90:
        return "Exceeds Expectations"
    elif 70 <= mark < 80:
        return "Acceptable"
    else:
        return "Fail"

for subject, score in marks.items():
    students_grade[subject] = grades_convert(score)

print(students_grade)
# Student Grade Calculator

# Function to calculate grade and comment
def calculate_grade(marks):
    if marks >= 90:
        return "A+", "Excellent performance!"
    elif marks >= 80:
        return "A", "Very good!"
    elif marks >= 70:
        return "B", "Good work!"
    elif marks >= 60:
        return "C", "Average performance."
    elif marks >= 50:
        return "D", "Needs improvement."
    else:
        return "F", "Failed. Work harder next time."

# List to store all student results
students = []

while True:
    name = input("Enter student name: ")
    marks = float(input("Enter marks (out of 100): "))

    grade, comment = calculate_grade(marks)
    
    # Store result as a dictionary
    student_record = {
        "Name": name,
        "Marks": marks,
        "Grade": grade,
        "Comment": comment
    }
    students.append(student_record)

    # Ask if the user wants to add more students
    choice = input("Do you want to add another student? (yes/no): ").lower()
    if choice != 'yes':
        break

# Display all results
print("\n--- Student Grade Records ---")
for student in students:
    print(f"Name: {student['Name']}, Marks: {student['Marks']}, Grade: {student['Grade']}, Comment: {student['Comment']}")

print("\nAll records stored successfully!")

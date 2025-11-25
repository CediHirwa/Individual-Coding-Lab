import csv
import sys

class Assignment:
    def __init__(self, name, category, grade, weight):
        self.name = name
        self.category = category.upper()
        self.grade = float(grade)
        self.weight = float(weight)

    def calculate_weighted_grade(self):
        return (self.grade / 100) * self.weight

def get_valid_number(prompt, is_weight=False):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            
            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
                continue
            
            if not is_weight and value > 100:
                print("Error: Grade cannot exceed 100. Please try again.")
                continue
                
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def main():
    assignments = []
    
    print("------------------------------------------")
    print("   ALU GRADE GENERATOR - STUDENT TOOL     ")
    print("------------------------------------------")

    print("\n--- Student Details ---")
    
    while True:
        student_name = input("Enter Student Name: ").strip()
        if student_name:
            break
        print("Error: Name cannot be empty.")

    while True:
        student_id = input("Enter Student ID (3 digits, e.g., 123): ").strip()
        # Check if it is a number AND has exactly length of 3
        if student_id.isdigit() and len(student_id) == 3:
            break
        print("Error: Student ID must be exactly 3 numeric digits.")


    while True:
        print("\n--- New Assignment ---")
        name = input("Assignment Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            continue
            
        while True:
            category = input("Category (FA/SA): ").strip().upper()
            if category in ['FA', 'SA']:
                break
            print("Error: Invalid category. Please enter 'FA' or 'SA'.")

        grade = get_valid_number("Grade Obtained (0-100): ", is_weight=False)
        weight = get_valid_number("Weight (e.g., 30): ", is_weight=True)

        assignments.append(Assignment(name, category, grade, weight))

        cont = input("Add another assignment? (y/n): ").lower()
        if cont != 'y':
            break

    total_fa_score = 0
    total_sa_score = 0
    total_fa_weight = 0
    total_sa_weight = 0

    csv_data = [['Student Name', 'Student ID', 'Assignment', 'Category', 'Grade', 'Weight']]

    for task in assignments:
        weighted = task.calculate_weighted_grade()
        
        if task.category == 'FA':
            total_fa_score += weighted
            total_fa_weight += task.weight
        else:
            total_sa_score += weighted
            total_sa_weight += task.weight
            
        csv_data.append([student_name, student_id, task.name, task.category, task.grade, task.weight])

    final_grade = total_fa_score + total_sa_score
    gpa = (final_grade / 100) * 5.0
    
    fa_status = total_fa_score >= (total_fa_weight * 0.5)
    sa_status = total_sa_score >= (total_sa_weight * 0.5)
    
    if fa_status and sa_status:
        final_status = "PASSED"
    else:
        final_status = "FAILED"

    print("\n" + "="*50)
    print("{:^50}".format('ACADEMIC PERFORMANCE SUMMARY'))
    print("="*50)
    print("Student: {} (ID: {})".format(student_name, student_id))
    print("-" * 50)
    
    print("{:<20} | {:<20}".format('Category', 'Score / Weight'))
    print("-" * 50)
    print("{:<20} | {:.2f} / {:.2f}".format('Formative (FA)', total_fa_score, total_fa_weight))
    print("{:<20} | {:.2f} / {:.2f}".format('Summative (SA)', total_sa_score, total_sa_weight))
    print("-" * 50)
    print("{:<20} | {:.2f} %".format('FINAL GRADE', final_grade))
    print("{:<20} | {:.2f}".format('GPA', gpa))
    print("{:<20} | {}".format('STATUS', final_status))
    print("="*50)

    if not fa_status:
        print("ALERT: You failed the Formative Assessment requirement (<50%).")
    if not sa_status:
        print("ALERT: You failed the Summative Assessment requirement (<50%).")

    try:
        filename = 'grades.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)
        print("\n[SUCCESS] Data successfully exported to '{}'.".format(filename))
    except IOError as e:
        print("\n[ERROR] Could not save file. Permission denied or file open. {}".format(e))

if __name__ == "__main__":
    main()

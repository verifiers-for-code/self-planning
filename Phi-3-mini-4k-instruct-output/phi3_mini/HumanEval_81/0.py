def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    

    1. Create a function that takes a list of GPAs as input.
    2. Create a list of tuples with the GPA ranges and corresponding letter grades.
    3. Loop through the list of GPAs and for each GPA, find the corresponding letter grade using the list of tuples.
    4. Return the list of letter grades."""
    
    # Step 1: Create a function that takes a list of GPAs as input.
    def grade_equation(grades):
        # Step 2: Create a list of tuples with the GPA ranges and corresponding letter grades.
        grade_ranges = [
            (4.0, 'A+'),
            (3.7, 'A'),
            (3.3, 'A-'),
            (3.0, 'B+'),
            (2.7, 'B'),
            (2.3, 'B-'),
            (2.0, 'C+'),
            (1.7, 'C'),
            (1.3, 'C-'),
            (1.0, 'D+'),
            (0.7, 'D'),
            (0.0, 'D-'),
            (0.0, 'E')
        ]
        
        # Step 3: Loop through the list of GPAs and for each GPA, find the corresponding letter grade using the list of tuples.
        letter_grades = []
        for gpa in grades:
            for grade_range in grade_ranges:
                if gpa >= grade_range[0]:
                    letter_grades.append(grade_range[1])
                    break
        
        # Step 4: Return the list of letter grades.
        return letter_grades
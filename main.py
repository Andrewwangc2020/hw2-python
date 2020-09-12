#Author: Andrew Wang aqw5628@psu.edu

def getGradePoint(lettergrade):
  if lettergrade == "A":
    return 4.0;
  elif lettergrade == "A-":
    return 3.67;
  elif lettergrade == "B+":
    return 3.33;
  elif lettergrade == "B":
    return 3.0;
  elif lettergrade == "B-":
    return 2.67;
  elif lettergrade == "C+":
    return 2.33;
  elif lettergrade == "C":
    return 2.0;
  elif lettergrade == "D":
    return 1.0;
  else:
    return 0.0;

letter1 = input("Enter your course 1 letter grade: ");
gradepoint1 = getGradePoint(letter1);
c = input("Enter your course 1 credit: ");
credit1 = int(c);
print(f"Grade point for course 1 is: {gradepoint1}");

letter2 = input("Enter your course 2 letter grade: ");
gradepoint2 = getGradePoint(letter2);
c = input("Enter your course 2 credit: ");
credit2 = int(c);
print(f"Grade point for course 2 is: {gradepoint2}");

letter3 = input("Enter your course 3 letter grade: ");
gradepoint3 = getGradePoint(letter3);
c = input("Enter your course 3 credit: ");
credit3 = int(c);
print(f"Grade point for course 3 is: {gradepoint3}");

gpa = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3); 
print(f"Your GPA is: {gpa}");


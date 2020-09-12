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

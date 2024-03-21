# Your solution to Exercise 4
output=""
grade = int(input("Enter the school grade: "))
get_school_grade_level(grade):
  if grade == 1 or grade == 2 or grade == 3:
      output="Initial level"
  elif grade == 4 or grade == 5 or grade == 6:
      output="Average level"
  elif grade == 7 or grade == 8 or grade == 9:
      output="Sufficient level"
  elif grade == 10 or grade == 11 or grade == 12:
      output="High level"
  else:
      output="Level is absent"
print(output)

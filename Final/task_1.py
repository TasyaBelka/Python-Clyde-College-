# 14.03.2023 Final assessment
# Author Tetyana Kostyuk
# Final Assessment Part 1

# validation of input data
# function check validation of the coursework mark
def CourseworkValidation(value):
  if (value.isdigit() == False):
    return 'Invalid data'
  
  elif (int(value) < 0 or int(value) > 60):
    return 'Invalid data'

  elif (value == ''):
    return 'Invalid data'

  else: return True

# function check validation of prelim mark
def PrelimValidation(value):

  if (value.isdigit() == False):
    return 'Invalid data'
  
  elif (int(value) < 0 or int(value) > 90):
    return 'Invalid data'

  elif (value == ''):
    return 'Invalid data'

  else: return True


# work with data
# function define the grade mark by checking conditions 
def ShowGrade(grade):
  if(grade >= 70):
    mark = 'A'
    print(f'Your grade is {grade}. \nYour grade mark is A')
    
  elif(grade >= 60 and grade < 70):
    mark = 'B'
    print(f'Your grade is {grade}. \nYour grade mark is B')
    
  elif(grade >= 50 and grade < 60):
    mark = 'C'
    print(f'Your grade is {grade}. \nYour grade mark is C')
    
  elif(grade >= 45 and grade < 50): 
    mark = 'D'
    print(f'Your grade is {grade}. \nYour grade is D')
    
  else:
    mark = 'No grade'
    print(f'Your grade is {grade}. \nYou haven\'t passed')
    
  return mark

# function calculate the grade 
def GradeCalc(value1, value2):
  grade = ((int(value1) + int(value2)) * 100) / 150
  return round(grade)


# program code
  
# input data
# input the coursework mark
courseworkMark = input('Enter your coursework mark: ')

# validate the coursework mark 
if(CourseworkValidation(courseworkMark) == True): 
  
  # input the prelim mark
  prelimMark = input('Enter your prelim mark: ')

  # validate the prelim mark
  if(PrelimValidation(prelimMark) == True):

    # calculate the grade
    # show the results
    ShowGrade(GradeCalc(courseworkMark, prelimMark))
    
  else:
    print('Invalid data')
    
else:
  print('Invalid data')
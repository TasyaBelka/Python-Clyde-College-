# 14.03.2023
# Author Tetyana Kostyuk
# Final Assessment Part 2

# open the files with data
studentList = open('names.txt', 'r')
courseworkList = open('mark1.txt', 'r')
prelimList = open('mark2.txt', 'r')

# create functions for work with income data
# function create a list of data from the file
def CreateList(file):
  list = []
  for line in file:
    stripedLine = line.strip()
    list.append(stripedLine)

  return list

# function calculate the grade and return the list with grades
def CalcGrade(list1, list2):
  gradeList = []
  for x, y in zip(list1, list2):
    result = ((int(x) + int(y)) * 100) / 150
    gradeList.append(round(result))
  return gradeList

# function define the grade mark depends on the grade
def GetGradeMark(list):
  markList = []
  for grade in list:
    
    if(grade >= 70):
      markList.append('A')
     
    elif(grade >= 60 and grade < 70):
      markList.append('B')
    
    elif(grade >= 50 and grade < 60):
      markList.append('C')
    
    elif(grade >= 45 and grade < 50): 
      markList.append('D')
  
    else:
      markList.append('No Grade')
  return markList

# function count the number of 'A' grade marks
def FindTheA(list):
  result = 0
  for mark in list:
    if(mark == 'A'): result += 1
  return result

# function define max value in list
def GetMaxValue(list):
  max = 0 # set the first max number with the smallest value
  for item in list:
    # compare setted number with the our list's value. If the value bigger than setted number, then our value we set as a max number. Else - the max number doesn't change.
    if(item > max): max = item 

  return max

# work with data
# create lists of the data
students = CreateList(studentList)
courseworkMark = CreateList(courseworkList)
prelimMark = CreateList(prelimList)

# close the files
studentList.close()
courseworkList.close()
prelimList.close()

# create a list with all calculated student's grades
gradeList = CalcGrade(courseworkMark, prelimMark)

# create a list with all defined student's grade marks
gradeMarkList = GetGradeMark(CalcGrade(courseworkMark, prelimMark))

# define how many 'A' grade marks in the gradeMarkList 
print(f'The number of \'A\' grade is: {FindTheA(GetGradeMark(CalcGrade(courseworkMark, prelimMark)))}')

# define the max grade
maxGrade = GetMaxValue(CalcGrade(courseworkMark, prelimMark))

# define who has the best grade
print(f'The best grade {maxGrade} has student {students[gradeList.index(maxGrade)]}')
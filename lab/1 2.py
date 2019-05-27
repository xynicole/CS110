
SUFFICIENT = 5


def hasManyGrades(value_list):
  return len(value_list) > SUFFICIENT


def makeListOfStudents(student_dict):
    student_listt = []
    for name in student_dict.keys()
      if hasManyGrades (student_dict[name]):
          student_list.append(name)
    return student_list
    

def create_dict(data_list):
    new_dict = {}
    for line in data_list:
      item_list = line.split()
    
      if item_list[0] not in new_dict:
        new_dict[item_list[0]] = []
      new_dict [item_list[0] +=item_list[1:]
      
  return new_dict

                


def main():
  student_data = open('student_data.txt.py','r')
  student_grade_list = student_data.readlines()
  print(student_grade_list)

  student_grades = (create_dic(student_grade_list)
  
  
  line = student_data.readline()
  while line:
##    print(line)
    student_grade_list = line.split()
    if student_grade_list[0] in student_grades:
      student_grades[students_grade_liest[0]] += student_grade_list[1:]

      
    else:
      student_grades[student_grade_list[0]] = [] +student_grade_list[1:]



      
##   print(student_grade_list)

    line = student_data.readline()

  print(student_grade)
  print_list = makeListOfStuents(student_grades)





            close()





main()

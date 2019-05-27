



def tuple_list_to_dict(begin_tuple):
  my_dict = {}
  for key,value in begin_tuple:
      if key in my_dict:
        my_dict[key] += value
      else:
        my_dict[key] =value
 
  return my_dict



def get_sorted_key_list(begin_dict):
  dictKeys = list(begin_dict.keys())
  dictKeys.sort()
  return dictKeys

def compute_average(begin_list):
  if len(begin_list) == 0:
    average_grade = 0
  else:
    the_sum = 0
    for element in begin_list:
      the_sum += element
      average_grade = the_sum / len(begin_list)
  return average_grade

def sorted_list_of_tuples(given_dict):
  new_list  = list(given_dict.items())
  new_list.sort()
  return new_list




def main():
    
  grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]),
               ('Slartibartfast',[]), ('Trillian', [98, 88]),
               ('Trillian', [97, 77]), ('Slartibartfast', []),
               ('Marvin', [2000, 500]) , ('Arthur', [42, 20]),
               ('Arthur', [64]), ('Trillian', [99]),
               ('Marvin', [450]), ('Marvin', [550]),('Agrajag', []),
               ('Agrajag', []), ('Agrajag', [0]),
               ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]  
  
  convert_dict = tuple_list_to_dict(grade_list)
  sort_key = get_sorted_key_list(convert_dict)

  print("%25s" % "Grade")
  print("%16s\t%6s\t%6s" % ("Name", "Count", "Average"))
  print("-----" *10)

  

  for key in sort_key:
    first_name = key
    grade_count = len(convert_dict[key])
    grade_average = compute_average(convert_dict[key])
    print("%16s\t%6i\t%6.2f" % (first_name, grade_count, grade_average))

  print()


  new_list_sorted = sorted_list_of_tuples(convert_dict)
  print("%25s" % "Grade")
  print("%16s\t%6s\t%6s" % ("Name", "Count", "Average"))
  print("-----" *10)

  for k, v in new_list_sorted:
    second_name = k
    segrade_count = len(v)
    segrade_average = compute_average(v)
    print("%16s\t%6i\t%6.2f" % (second_name, segrade_count, segrade_average))


main()

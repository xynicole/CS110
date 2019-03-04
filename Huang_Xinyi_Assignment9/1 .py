
'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #9
'''
'''
ANALYSIS

RESTATEMENT:
  to count the times of students grades and the average of the grade

OUTPUT to monitor:
 name, grade count and average

'''

# CONSTANT
NUM = 36

# create a dictionary
def tuple_list_to_dict(grade_list): 
  my_dict={}
  for item in grade_list:
    if item[0] not in my_dict:
      my_dict[item[0]] = item[1]
    else:
      my_dict[item[0]] += item[1]
 
  return my_dict

# create a list of dictionary keys and sort them
def get_sorted_key_list(my_dict):
  keylist = list(my_dict.keys())
  keylist.sort()
  return keylist

# compute the average of the list of grades for each person
def compute_average(my_value): 
  if my_value == []:
    return 00.00
  else:
    average = float(sum(my_value) / len(my_value))
    return average

#Sort the list
def get_sorted_list_of_tuples(my_selist):
  return sorted(my_selist, key=lambda student: student[0])

def main():
    
  grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]),
               ('Slartibartfast',[]), ('Trillian', [98, 88]),
               ('Trillian', [97, 77]), ('Slartibartfast', []),
               ('Marvin', [2000, 500]) , ('Arthur', [42, 20]),
               ('Arthur', [64]), ('Trillian', [99]),
               ('Marvin', [450]), ('Marvin', [550]),('Agrajag', []),
               ('Agrajag', []), ('Agrajag', [0]),
               ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]  

  my_dict = {}
  my_dict = tuple_list_to_dict(grade_list)

 
# create a table
  print("{0:>26}".format("Grade"))
  print("{0:>16}{1:>10}{2:>10}".format("Name", "Count", "Average"))
  print("-" * NUM)

#first set of outputs
  for key in get_sorted_key_list(my_dict):
    average = compute_average(my_dict[key])
    print("{0:>16}{1:>10}{2:>10.2f}".format(key, len(my_dict[key]), average))


# table
  print("\n\n")
  print("{0:>26}".format("Grade"))
  print("{0:>16}{1:>10}{2:>10}".format("Name", "Count", "Average"))
  print("-" * NUM)

#second set of outputs
  my_selist = []
  my_selist = my_dict.items()
  my_selist = get_sorted_list_of_tuples(my_selist)
  for key in my_selist:
    average = compute_average(key[1])
    print("{0:>16}{1:>10}{2:>10.2f}".format(key[0], len(key[1]), average))


main()

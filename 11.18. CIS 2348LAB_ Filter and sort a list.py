#Tri Dao
#1954347
#11.18 CIS 2348LAB: Filter and sort a list

inp = input()
my_list = sorted([int(i) for i in inp.split() if int(i) >= 0])
for value in my_list:
  print(value, end = ' ')
  
  
  
  
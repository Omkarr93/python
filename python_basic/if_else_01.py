# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount


salary = int(input('Enter your salary\n'));
yos = int(input('Enter your year of service\n'));
bonus = salary*0.05 +salary;
txt =  'Your this years bonus  is {}'  
 
if yos >= 5:
   print(txt.format(bonus))
else:
    print("No  bonus")   

'''
print "Enter salary"
salary = input()
print "Enter year of service"
yos = input()
if yos>5:
  print "Bonus is",.05*salary
else:
  print "No bonus"    '''
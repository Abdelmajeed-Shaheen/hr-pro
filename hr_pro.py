import datetime
class Employee:
   #Employee class here
   def __init__ (self,name,age,salary,employment_year,**kwargs):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year
       for key , value in kwargs.items():
           setattr(self,key,value)

   def __str__(self):
      return ('Name: '+ self.name+', Age: '+str(self.age)+', Salary: '+str(self.salary)+', Working Years: '+str(self.get_working_years()))
   def get_working_years(self):
       return (datetime.date.today().year - self.employment_year)



class Manager(Employee):
    #Manager class here
    def __init__ (self,name,age,salary,employment_year,bonus_percentage,**kwargs):
        super().__init__ (name,age,salary,employment_year,**kwargs)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return (self.bonus_percentage  * self.salary)
    def __str__(self):
        return ('Name: '+ self.name+', Age: '+str(self.age)+', Salary: '+str(self.salary)+', Working Years: '+str(self.get_working_years())+', Bonus: '+str(self.get_bonus()))




def main():
	# main code here
    employees =[]
    managers =[]
    exit = True
    print("Welcome to HR Pro 2019")
    while exit:
        print("Options:")
        print("     1. Show Employees")
        print("     2. Show Managers")
        print("     3. Add An Employee")
        print("     4. Add A Manager")
        print("     5. Exit")
        print("     ")
        print("     ")
        userinput= int(input("What would you like to do?"))
        if userinput == 5:
            exit = False
            pass
        elif userinput == 1:
            print("-----------------")
            print("Employees")
            print("     ")
            print("     ")
            for emp in employees:
                print(emp.__str__())
            print("-----------------")
            pass
        elif userinput == 2:
            print("-----------------")
            print("Managers")
            print("     ")
            print("     ")
            for man in managers:
                print(man.__str__())
            print("-----------------")
            pass
        elif userinput == 3:
            print("-----------------")
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            year = input("Employement year: ")
            employee = Employee(name,int(age),int(salary),int(year))
            employees.append(employee)
            print("Employee added succesfully")

            pass
        elif userinput == 4:
            print("-----------------")
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            year = input("Employement year: ")
            per = input("Bonus Percentage: ")
            manager = Manager(name,int(age),int(salary),int(year),float(per))
            managers.append(manager)
            print("Manager added succesfully")
            pass
        else:
            pass


if __name__ == '__main__':
	main()

class EmployeeRecord:
    ## Initiaating a constructor that stores details for objects whenever objects calls this class
    def __init__(self,name,salary,contact_number):
        self.name=name
        self.salary=salary
        self.contact_number=contact_number
        
    ## Method to display details of any particular employeen when called
    def display_employee_details(self):
        print("HOLD ON...... PRINTING EMPLOYEE DETAILS")
        print (f" NAME : {self.name}\nCONTACT NUMBER : {self.contact_number}\nSALARY : {self.salary}")
        
        
    ## Method to increment the salary of requested employee
    def increment_salary(self,incremented_percentage):
       salary_incremented = round(int(self.salary) * (1 + incremented_percentage / 100), 2)
       print(f"Incremented salary is : {salary_incremented}")
       
       
       
       
def main():
    ## Creating employee objects
    employee1=EmployeeRecord(name="David Gea",salary="10",contact_number=12345)
    employee2=EmployeeRecord(name="Raya Henderson",salary="20",contact_number=56789)
    employee3=EmployeeRecord(name="David Alaba",salary="30",contact_number=11111)
    
    ## Printing employee details
    employee1.display_employee_details()
    employee2.display_employee_details()
    
    ## Incrementing salary of employees
    employee1.increment_salary(20)
    
    
    
    
    
    
    
if __name__=="__main__":
    print("Main function is running")
    main()
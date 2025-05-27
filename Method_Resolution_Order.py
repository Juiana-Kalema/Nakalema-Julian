class Person:
    def work(self):
        print("Person: Doing work.")

class Employee(Person):
    def work(self):
        print("Employee: Writing code.")

class Manager(Person):
    def work(self):
        print("Manager: Holding meetings.")

class TechLead(Manager, Employee):
    pass

# Create a TechLead object
lead = TechLead()

# Call the work method
lead.work()

# Show the Method Resolution Order
print("\nMethod Resolution Order (MRO):")
for cls in TechLead.__mro__:
    print(cls)

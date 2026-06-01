# #Getters and Setters

# import random
# #1.The decorator (THE LOGIC WRAPPER)
# def evaluate(reps):
#   def decorators(func):
#     def wrapper(self,*args,**kwargs):
#       print(f"---running {reps} trials to measure Performance{P} ")
#       total_score=0
#       for i in range(reps):
#         #the Task T :Executing the predection
#         score=func(slef,*args,**kwargs)
#         total_score += score

#         #CALCULATE THE AVG PERFORMANCE
#     avg_p = total_score/reps
#     #using the Setter here to update the models accuracy
#     self.model_accuracy= avg_p
#     print(f"Trials complete.Average Accuracy: {avg_p}%")
#     return wrapper    
#   return decorators

# # --- 2. THE CLASS (The ML Agent) ---
# class SmartModel:
#     def __init__(self, name):
#         self.name = name
#         self._accuracy = 0  # Hidden variable

#     # --- THE GETTER ---
#     @property
#     def model_accuracy(self):
#         return f"{self._accuracy}%"

#     # --- THE SETTER ---
#     @model_accuracy.setter
#     def model_accuracy(self, value):
#         # Logic: Accuracy cannot be higher than 100 or lower than 0
#         if value > 100:
#             self._accuracy = 100
#         elif value < 0:
#             self._accuracy = 0
#         else:
#             self._accuracy = value
#         print(f"[Internal Update] Model accuracy set to {self._accuracy}")  
#   # --- THE TASK (T) ---
#     @evaluate(reps=3) # Using the decorator to repeat the task 3 times
#     def run_prediction(self, data):
#         print(f"Processing data: {data}...")
#         # Experience (E): Simulating a result based on "learning"
#         result_score = random.randint(50, 110) # Simulating a score
#         return result_score

# # --- 3. EXECUTION ---
# my_ai = SmartModel("Spam_Detector_3000")

# print(f"Initial Accuracy: {my_ai.model_accuracy}")
# print("---")

# # Execute the task
# my_ai.run_prediction("Email_Inbound_XYZ")

# print("---")
# print(f"Final Accuracy: {my_ai.model_accuracy}")      





# #class instance -04
# class Employee:
#     company = "HP"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def print_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")

#     # --- NEW INSTANCE METHOD ---
#     def give_bonus(self, amount):
#         # We access the CURRENT salary using self.salary
#         # We add the amount to it
#         self.salary = self.salary + amount
#         print(f"🎉 Success! {self.name} received a bonus of {amount}.")

# # 1. Create two employees
# e1 = Employee("Jack", 3000)
# e2 = Employee("Jill", 5000)

# print("--- Before Bonus ---")
# e1.print_info()
# e2.print_info()

# # 2. Give a bonus ONLY to Jack
# # Python sends 'e1' as 'self' and '1000' as 'amount'
# e1.give_bonus(1000) 

# print("\n--- After Bonus ---")
# e1.print_info() # Jack's salary should change
# e2.print_info() # Jill's salary should remain the same.





# #dunder method is here 
# class Employee:
#     def __init__(self,name,salary):
#         self.name =name
#         self.salary=salary

#     def __str__(self):
#         return f"Name of employee :{self.name} and his salary is :{self.salary}"

#     def __repr__(self):
#         return "Employee(name={}, salary={})".format(self.name, self.salary)

#     def __len__(self):
#         return len(self.name)


# e1=Employee("basit",50000)
# e2=Employee("shahid",30000)

# print(e1)
# print(repr(e1))
# print([e1])
# print(len(e2))

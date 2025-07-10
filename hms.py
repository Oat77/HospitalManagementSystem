class Person:

    def __init__ (self, name, age, gender):  

        self.name= name
        self.age= age
        self.gender= gender

       
class Patient (Person):

    patient_id_counter= 1001

    def generate_patient_id(cls):
        cls.patient_id_counter += 1
        return cls.patient_id_counter
    
    def __init__ (self, name, age, gender):
        super().__init__(name, age, gender)
        self.get_patient_id= self.generate_patient_id()


    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Patient ID:", self.get_patient_id)


class Doctor (Person):

    doctor_calendar= {}

    months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']

    for month in months:
        doctor_calendar[month]= []

    for month, days in doctor_calendar.items(): 
        if month in ('April', 'June' , 'September' , 'November') :
            for i in range (30):
                days.append(False)
        else:
            for i in range (31):
                days.append(False)

    doctor_id_counter= 70001

    def generate_doctor_id(cls):
        cls.doctor_id_counter += 1
        return cls.doctor_id_counter
    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.get_doctor_id= self.generate_doctor_id()
    
    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Patient ID:", self.get_doctor_id)


patient1= Patient("Omaro", 22, 'M')

patient1.view_profile()

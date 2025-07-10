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

    doctor_id_counter= 70001

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.get_doctor_id= self.generate_doctor_id()
        self.doctor_calendar= self.create_calendar()
 
    def create_calendar(self):
        self.doctor_calendar= {}
        self.months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
        self.doctor_times=[]
        self.clock= [9,10,11,12,1,2,3,4]

        for month in self.months:
            self.doctor_calendar[month]= []

        for month, days in self.doctor_calendar.items(): 
            if month in ('April', 'June' , 'September' , 'November') :
                for i in range (30):
                    days.append(False)
                    self.doctor_times.append(self.clock)
            else:
                for i in range (31):
                    days.append(False)
                    self.doctor_times.append(self.clock)
        
        return self.doctor_calendar

    def check_availability(cls):
        cls.availabletimes= []
        cls.check_month= input("Enter month: ")
        cls.check_day= input("Enter day: ")
        for cls.hrs in cls.doctor_times[cls.doctor_calendar[cls.check_month][int(cls.check_day)-1]]:
            if cls.hrs != False:
                cls.availabletimes.append(cls.hrs)
        return cls.availabletimes

    def generate_doctor_id(cls):
        cls.doctor_id_counter += 1
        return cls.doctor_id_counter
    
    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Patient ID:", self.get_doctor_id)
        print("Available Times:", self.check_availability())


doctor1= Doctor("Omaro", 22, 'M')
doctor1.view_profile()
doctor1.check_availability


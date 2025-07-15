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
        self.get_patient_id= Patient.generate_patient_id()


    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Patient ID:", self.get_patient_id)


class Doctor (Person):

    doctor_id_counter= 70001

    def __init__(self, name, age, gender, appointments=[]):
        super().__init__(name, age, gender)
        self.get_doctor_id= self.generate_doctor_id()
        self.doctor_calendar= self.create_calendar()
        self.appointments= appointments
 
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

    def check_availability(self):
        self.availabletimes= []
        self.check_month= input("Enter month: ")
        self.check_day= input("Enter day: ")
        for self.hrs in self.doctor_times[self.doctor_calendar[self.check_month][int(self.check_day)-1]]:
            if self.hrs != False:
                self.availabletimes.append(self.hrs)
        return self.availabletimes
    
    def book_appointment(self, appointment):
        self.appointments.append(appointment)

    def generate_doctor_id(self):
        self.doctor_id_counter += 1
        return self.doctor_id_counter
    
    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Patient ID:", self.get_doctor_id)
        print("Available Times:", self.check_availability())


class Appointment:

    app_status= ['booked', 'pending', 'cancelled']

    def __init__ (self, appointment_id, patient, doctor, date, time, status):
        self.appointment_id= appointment_id
        self.patient= patient
        self.doctor= doctor
        self.date= date
        self.time= time
        self.status= status

    def confirm(self):
        self.status= self.app_status[0]

    def cancel(self):
        self.status= self.app_status[2]


class HospitalSystem():

    def __init__ (self, patients= [], doctors= [], appointments= []):
        self.patients= patients
        self.doctors= doctors
        self.appointments= appointments

    def add_patient(self, new_patient):
        self.patients.append(new_patient)

    def add_doctor(self, new_doctor):
        self.doctors.append(new_doctor)

    def book_appointment(self, new_appointment):
        self.appointments.append(new_appointment)

    def cancel_appointment(self, ex_appointment):
        self.appointments.remove(ex_appointment)


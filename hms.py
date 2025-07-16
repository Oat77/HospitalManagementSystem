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

    def __init__(self, name, age, gender, appointments):
        super().__init__(name, age, gender)
        self.get_doctor_id= self.generate_doctor_id()
        self.doctor_calendar= self.create_calendar()
        self.appointments= appointments if appointments else []
 
    def create_calendar(self):
        self.doctor_calendar= {}
        self.months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
        self.clock= ['9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM']

        for month in self.months:
            self.doctor_calendar[month]= {}
            if month in ('April', 'June' , 'September' , 'November') :
                for i in range (1,30):
                    self.doctor_calendar[month][i]= list(self.clock)
            else:
                for i in range (1,31):
                    self.doctor_calendar[month][i]= list(self.clock)
        
        return self.doctor_calendar

    def check_availability(self):
        self.availabletimes= []
        self.check_month= input("Enter month: ")
        self.check_day= input("Enter day: ")
        for i in self.doctor_calendar[self.check_month][self.check_day]:
            if i != True:
                return i
            break
        
        return self.availabletimes


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

    def book_appointment(self):
        self.book_month= input("Enter month: ")
        self.book_day= input("Enter day: ")
        self.book_time= input("Enter time: ")
        self.book_doctor= input("Enter Doctor ID: ")
        self.book_patient=("Enter Patient ID: ")
        self.book_appID= ("Enter Appointment ID: ")
        self.book_appStatus= ("Confirm Appointment Status: ")
        for i in self.doctor_calendar[self.book_month][self.book_month]:
            if i == self.book_time:
                i= True
            else:
                return "Time slot is not available"
            break


    def cancel_appointment(self, ex_appointment):
        self.appointments.remove(ex_appointment)


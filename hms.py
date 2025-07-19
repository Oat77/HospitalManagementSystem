class Person:

    def __init__ (self, name, age, gender):  

        self.name= name
        self.age= age
        self.gender= gender

       
class Patient (Person):

    patient_id_counter= 1001

    @classmethod
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

    def __init__(self, name, age, gender, appointments):
        super().__init__(name, age, gender)
        self.doctor_id= self.generate_doctor_id()
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
        self.check_month= input("Enter month: ")
        self.check_day= input("Enter day: ")
        for i in self.doctor_calendar[self.check_month][self.check_day]:
            if i != "BOOKED":
                self.appointments.append(i)
                for i in self.appointments:
                    return i
            else: 
                return "Doctor's day is fully booked"

    @classmethod
    def generate_doctor_id(self):
        self.doctor_id_counter += 1
        return self.doctor_id_counter
    
    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Doctor ID:", self.doctor_id)


class Appointment:

    app_status= ['booked', 'pending', 'cancelled']

    def __init__ (self, appointment_id, patient, doctor, month, day, time, status):
        self.appointment_id= appointment_id
        self.patient= patient
        self.doctor= doctor
        self.month= month
        self.day= day
        self.time= time
        self.status= status

    def confirm(self):
        self.status= self.app_status[0]

    def cancel(self):
        self.status= self.app_status[2]


class HospitalSystem():

    def __init__ (self, patients, doctors, appointments):
        self.patients= patients if patients else []
        self.doctors= doctors if doctors else []
        self.appointments= appointments if appointments else []
        

    def add_patient(self):
        self.name= input("Enter name: ")
        self.age= input("Enter age: ")
        self.gender= input("Enter gender: ")
        self.patient= Patient(self.name, self.age, self.gender)
        self.patients.append(self.patient)

    def add_doctor(self):
        self.name= input("Enter name: ")
        self.age= input("Enter age: ")
        self.gender= input("Enter gender: ")
        self.appointments= []
        self.doctor= Doctor(self.name, self.age, self.gender, self.appointments)
        self.doctors.append(self.doctor)

    def book_appointment(self):
        self.book_month= input("Enter month: ")
        self.book_day= input("Enter day: ")
        self.book_time= input("Enter time: ")
        self.book_doctor= input("Enter Doctor ID: ")
        self.book_patient=input("Enter Patient ID: ")
        self.book_appID= input("Enter Appointment ID: ")
        self.book_appStatus= input("Confirm Appointment Status: ")

        self.doctor= None
        self.patient= None

        for doc in self.doctors:
            if str(doc.doctor_id) == self.book_doctor:
                self.doctor= doc
                break
        
        for pat in self.patients:
            if pat.get_patient_id == self.book_patient:
                self.patient = pat
                break

        for i in self.doctor.doctor_calendar[self.book_month][int(self.book_day)]:
            if i == self.book_time:
                self.appointment= Appointment(self.book_appID, self.book_patient, self.book_doctor, self.book_month, self.book_day, self.book_time, self.book_appStatus)
                self.doctor.appointments.append(self.appointment)
                i= "BOOKED"
                print (f"Appointment {self.appointment.appointment_id()} successfully booked!")
                break
            else:
                return "Time slot is not available"
            break


    def cancel_appointment(self):

        cancelled_appointment= input("Enter appointment ID: ")
        
        for i in self.appointments():
            if i.appointment_id() == cancelled_appointment:
                self.appointments.remove(i)
                print (f"Appointment {cancelled_appointment} was successfully cancelled.")
            else:
                print (f"Appointment {cancelled_appointment} was not found.")
            

        

if __name__ == "__main__":

    hms= HospitalSystem([],[],[])

    print ("\n ######## Welcome to the Hospital Management System! ########")
    while True: 

        print ("\n1. Doctor Management ")
        print ("2. Register Patient")
        print ("3. Appointment Manager")
        print ("4. Exit")


        menu_choice=  input("\n Please enter the number tied to your desired option: ")


        if menu_choice== str(1):

            while True: 
                
                print ("\n ######## You are in the Doctor Management Menu! ########")
                print ("\n1. Register Doctor ")
                print ("2. See Doctor Listing ")
                print ("3. View Doctor Profile")
                print ("4. Remove Doctor")
                print ("5. Exit")

                dm_choice=  input("\n Please enter the number tied to your desired option: ")

                if dm_choice == str(1):
                    hms.add_doctor()
                    print ("\n Doctor successfully added!")

                elif dm_choice == str(2):
                    print ("\n ***** Doctor Listing *****")
                    for doctor in hms.doctors:
                        print (f"{doctor.doctor_id} : {doctor.name}")

                elif dm_choice == str(3):
                    doc_id= input("Please enter doctor ID: ")
                    for doctor in hms.doctors:
                        if str(doctor.doctor_id) == doc_id:
                            doctor.view_profile()
                        else:
                            print("Sorry, doctor ID not found. Try again!")

                elif dm_choice == str(4):
                    doc_id= input("Please enter doctor ID: ")
                    for doctor in hms.doctors:
                        if doctor.doctor_id() == doc_id:
                            hms.doctors.remove(doctor)
                        else:
                            print("Sorry, doctor ID not found. Try again!")

                elif dm_choice == str(5):
                    print ("\nExiting Doctor Management menu!")
                    break

        if menu_choice == str(2):

            while True: 
                
                print ("\n ######## You are in the Patient Management Menu! ########")
                print ("\n1. Register Patient ")
                print ("2. See Patient Listing ")
                print ("3. View Patient Profile")
                print ("4. Exit")

                pm_choice=  input("\n Please enter the number tied to your desired option: ")

                if dm_choice == str(1):
                    hms.add_patient()
                    print ("\n Patient successfully added!")

                elif dm_choice == str(2):
                    print ("\n ***** Patient Listing *****")
                    for patient in hms.patients:
                        print (f"{patient.get_patient_id} : {patient.name}")

                elif dm_choice == str(3):
                     pat_id= input("Please enter patient ID: ")
                     for patient in hms.patients:
                        if str(patient.get_patient_id) == pat_id:
                            patient.view_profile()
                        else:
                            print("Sorry, patient ID not found. Try again!")

                elif dm_choice == str(4):
                    print ("\nExiting Patient Management menu!")
                    break




        if menu_choice == str(3):

            while True: 
                
                print ("\n ######## You are in the Appointment Management Menu! ########")
                print ("\n1. Book Appointment")
                print ("2. Cancel Appointment")
                print ("3. Check Available Bookings")
                print ("4. View Patient Appointments")
                print ("5. Exit")

                ap_choice=  input("\n Please enter the number tied to your desired option: ")

                if ap_choice == str(1):
                    hms.book_appointment()
                    print ("\n Appointment successfully booked!")

                if ap_choice == str(2):
                    hms.cancel_appointment()
                    print ("\n Appointment successfully cancelled!")

                if ap_choice == str(3):
                    doc_id= input("Please enter doctor ID: ")
                    for i in hms.doctors:
                        if i.doctor_id == int(doc_id):
                            i.checkavailability()
                        else:
                            print ("Sorry, doctor's ID was not found!")

                if ap_choice == str(4):
                    pat_id= input("Please enter patient ID: ")
                    for i in hms.appointments:
                        if i.get_patient_id == pat_id:
                            print (f"\n {i.book_appID} || Dr. {i.name} || {i.book_month} {i.book_day} @ {i.book_time} \n")
                        else:
                            break
                    


        if menu_choice == str(4):
            print ("Exiting portal. Goodbye!")
            break


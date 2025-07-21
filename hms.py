
#Creates 'Person' class 

class Person:

    #Class initializer
    def __init__ (self, name, age, gender):  
        self.name = name
        self.age = age
        self.gender = gender

#Creates 'Patient' class 

class Patient (Person):

    patient_id_counter = 1001

    #Patient ID generator
    @classmethod
    def generate_patient_id(cls):
        cls.patient_id_counter += 1
        return cls.patient_id_counter

    
    #Class initializer
    def __init__ (self, name, age, gender):
        super().__init__(name, age, gender)
        self.get_patient_id = self.generate_patient_id()

    #Profile generator that generates all patient attributes
    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Patient ID:", self.get_patient_id)


#Creates Doctor class
class Doctor (Person):

    #Counter that keeps track of assigned doctor IDs
    doctor_id_counter = 70001

    #Doctor ID generator
    @classmethod
    def generate_doctor_id(cls):
        cls.doctor_id_counter += 1
        return cls.doctor_id_counter

    #Class initializer
    def __init__(self, name, age, gender, appointments):
        super().__init__(name, age, gender)
        self.doctor_id = self.generate_doctor_id()
        self.doctor_calendar = self.create_calendar()
        self.appointments = appointments if appointments else []

    #Creates a calender that keeps track of all booked appointments.
    def create_calendar(self):

        #Calendar takes the form of a dictionary that has months as keys. 
        doctor_calendar = {}
        self.months = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        self.clock = ['9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM']

        #The item tied to each key is a dictionary. 
        # Each key with represents a day of the month, with each item representing the doctors working hours. 
        for month in self.months:
            doctor_calendar[month] = {}
            days = 30 if month in ('April', 'June', 'September', 'November') else 31
            for i in range(1, days+1):
                doctor_calendar[month][i] = list(self.clock)
        return doctor_calendar

    #Checks the doctor's availability by returning unbooked hour slots for a specified month and day.
    def check_availability(self):
        check_month = input("Enter month: ").strip()
        try:
            check_day = int(input("Enter day: "))

        #Checks for legitimate month and day entries.
        except ValueError:
            print("Invalid entry. Please enter a number.")
            return

        if check_month not in self.doctor_calendar:
            print("Invalid month entered.")
            return

        if check_day not in self.doctor_calendar[check_month]:
            print("Invalid day entered.")
            return

        #Returns doctor's available hours for a specified month and day. 
        available_slots = [t for t in self.doctor_calendar[check_month][check_day] if t != "BOOKED"]
        if available_slots:
            print(f"Available slots on {check_month} {check_day}: {', '.join(available_slots)}")
        else:
            print("Doctor's day is fully booked.")

    #Profile generator that generates all patient attributes
    def view_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Doctor ID:", self.doctor_id)


#Initializes Doctor Class
class Appointment:

    #references of appointment statuses
    app_status = ['booked', 'completed', 'cancelled']

    #Class initializer
    def __init__ (self, appointment_id, patient, doctor, month, day, time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.month = month
        self.day = day
        self.time = time
        self.status = status

    #Assigns appropiate status for each appointment
    def confirm(self):
        self.status = self.app_status[0]

    def complete(self):
        self.status= self.app_status[1]

    def cancel(self):
        self.status = self.app_status[2]


#Creates HospitalSystem class
class HospitalSystem:

    #Class initializer
    def __init__ (self, patients, doctors, appointments):
        self.patients = patients if patients else []
        self.doctors = doctors if doctors else []
        self.appointments = appointments if appointments else []

    #Adds patient to Hospital System
    def add_patient(self):
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        patient = Patient(name, age, gender)
        self.patients.append(patient)
        print("\n Patient successfully added!")

    #Adds doctor to Hospital Systemn
    def add_doctor(self):
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        doctor = Doctor(name, age, gender, [])
        self.doctors.append(doctor)
        print("\n Doctor successfully added!")

    #Adds appointment to hospital queue
    def book_appointment(self):
        try:
            book_month = input("Enter month: ").strip()
            book_day = int(input("Enter day: "))
            book_time = input("Enter time (e.g., 9AM): ").strip()
            book_doctor = input("Enter Doctor ID: ").strip()
            book_patient = input("Enter Patient ID: ").strip()
            book_appID = input("Enter Appointment ID: ").strip()

            #Verifies legitimate entries
            doctor = next((d for d in self.doctors if str(d.doctor_id) == book_doctor), None)
            if doctor is None:
                print("Doctor not found.")
                return

            patient = next((p for p in self.patients if str(p.get_patient_id) == book_patient), None)
            if patient is None:
                print("Patient not found.")
                return

            if book_month not in doctor.doctor_calendar:
                print("Invalid month.")
                return
            
            if book_day not in doctor.doctor_calendar[book_month]:
                print("Invalid day.")
                return
            
            
            #Manages the booking of appointments and updating of doctor's calendar. 
            slots = doctor.doctor_calendar[book_month][book_day]
            if book_time in slots:
                idx = slots.index(book_time)
                slots[idx] = "BOOKED"
                appointment = Appointment(book_appID, patient, doctor, book_month, book_day, book_time, 'booked')
                appointment.confirm()
                self.appointments.append(appointment)
                doctor.appointments.append(appointment)
                print(f"Appointment {appointment.appointment_id} successfully booked!")
            else:
                print("Time slot is not available.")

        #Throws error exception for invalid appointment details. 
        except Exception as error: 
            print("Error in processing appointment:", error)
            print("Check submitted details and try again.")

    #Completes appointment and prints bill.
    def complete_appointment(self):
        consultation_charge= 300
        comp_app= input("Enter appointment ID: ")
        found= False
        for app in self.appointments:
            if app.appointment_id == comp_app:
                found= True
                extra= "N/A"
                service= "N/A"
                app.complete() 
                extra= input ("Were there any other service offered during this consultation? (Y/N): ").strip().upper()
                if extra == "Y":
                    service= input("Enter service offered: ")
                    cost= input("Enter service cost: ")
                    try:
                        total_cost= int(cost) + consultation_charge
                    except ValueError:
                        print ("Bill generation error due to invalid entry. Pease try again.")
                        return
                else: 
                    total_cost= consultation_charge
                break
        if not found:
            print("Appointment not found. Try again.")
            return

        print (f"######## Bill FOR APPOINTMENT: {app.appointment_id} ########")
        print (f"         Appointment Date: {app.month} {app.day}            ")
        print (f"         Assigned Doctor: {app.doctor.name}                 ")
        print (f"         Assigned Patient: {app.patient.name}               ")
        print (f"         Additional Services: {service}                    ")
        print (f"         Total Cost: {total_cost}                           ")
                

    #Manages the cancellation of appointments and the updating of doctor's calendar. 
    def cancel_appointment(self):
        cancelled_appointment = input("Enter appointment ID: ").strip()
        for appt in self.appointments:
            if appt.appointment_id == cancelled_appointment:
                appt.cancel()
                self.appointments.remove(appt)
                appt.doctor.appointments.remove(appt)
                appt.cancel
                print(f"Appointment {cancelled_appointment} was successfully cancelled.")
                return
        print(f"Appointment {cancelled_appointment} was not found.")

#Main program responsible for running user interface
if __name__ == "__main__":
    hms = HospitalSystem([], [], [])

    #Launches main menu
    print("\n ######## Welcome to the Hospital Management System! ########")
    while True:
        print("\n1. Doctor Management")
        print("2. Patient Management")
        print("3. Appointment Manager")
        print("4. Exit")
        menu_choice = input("\n Please enter the number tied to your desired option: ")

        #Launches doctor management menu
        if menu_choice == str(1):
            while True:
                print("\n ######## Doctor Management ########")
                print("1. Register Doctor")
                print("2. See Doctor Listing")
                print("3. View Doctor Profile")
                print("4. Remove Doctor")
                print("5. Exit")
                dm_choice = input("\n Your choice: ")

                #Adds docotor
                if dm_choice == str(1):
                    hms.add_doctor()
                
                #Produces list of registerd doctors
                elif dm_choice == str(2):
                    print("\n ***** Doctor Listing *****")
                    for doc in hms.doctors:
                        print(f"{doc.doctor_id} : {doc.name}")
                
                #Produces profile of a given doctor
                elif dm_choice == str(3):
                    doc_id = input("Enter doctor ID: ").strip()
                    doctor = next((d for d in hms.doctors if str(d.doctor_id) == doc_id), None)
                    if doctor:
                        print("\n ***** Doctor Profile *****")
                        doctor.view_profile()
                    else:
                        print("Doctor ID not found.")

                #De-registers doctor
                elif dm_choice == str(4):
                    doc_id = input("Enter doctor ID: ").strip()
                    doctor = next((d for d in hms.doctors if str(d.doctor_id) == doc_id), None)
                    if doctor:
                        hms.doctors.remove(doctor)
                        print("Doctor removed.")
                    else:
                        print("Doctor ID not found.")
                
                #Exits doctor management menu
                elif dm_choice == str(5):
                    print("Exiting Doctor Management.")
                    break

        
        #Launches Patient Management menu
        elif menu_choice == str(2):
            while True:
                print("\n ######## Patient Management ########")
                print("1. Register Patient")
                print("2. See Patient Listing")
                print("3. View Patient Profile")
                print("4. Exit")
                pm_choice = input("\n Your choice: ")

                #Adds patient
                if pm_choice == str(1):
                    hms.add_patient()

                #Produces listing of registered patients. 
                elif pm_choice == str(2):
                    print("\n ***** Patient Listing *****")
                    for p in hms.patients:
                        print(f"{p.get_patient_id} : {p.name}")

                #Generates profile for a given patient.
                elif pm_choice == str(3):
                    pat_id = input("Enter patient ID: ").strip()
                    patient = next((p for p in hms.patients if str(p.get_patient_id) == pat_id), None)
                    if patient:
                        print("\n ***** Patient Profile *****")
                        patient.view_profile()
                    else:
                        print("Patient ID not found.")

                #Exits Patient Management menu
                elif pm_choice == str(4):
                    print("Exiting Patient Management.")
                    break

        #Launches Appointment Management menu
        elif menu_choice == str(3):
            while True:
                print("\n ######## Appointment Manager ########")
                print("1. Book Appointment")
                print("2. Complete Appointment")
                print("3. Cancel Appointment")
                print("4. Check Available Bookings")
                print("5. View Patient Appointments")
                print("6. Exit")
                ap_choice = input("\n Your choice: ")

                #Books appointment
                if ap_choice == str(1):
                    hms.book_appointment()
                    
                #Completes appointment
                elif ap_choice == str(2):
                    hms.complete_appointment()

                #Cancels appointment
                elif ap_choice == str(3):
                    hms.cancel_appointment()

                #Displays available dates for a given doctor
                elif ap_choice == str(4):
                    doc_id = input("Enter doctor ID: ").strip()
                    doctor = next((d for d in hms.doctors if str(d.doctor_id) == doc_id), None)
                    if doctor:
                        doctor.check_availability()
                    else:
                        print("Doctor ID not found.")

                #Generates listing of all appointments for a given patient
                elif ap_choice == str(5):
                    pat_id = input("Enter patient ID: ").strip()
                    found = False
                    for appt in hms.appointments:
                        if str(appt.patient.get_patient_id) == pat_id:
                            print(f"\n {appt.appointment_id} || Dr. {appt.doctor.name} || {appt.month} {appt.day} @ {appt.time}")
                            found = True
                    if not found:
                        print("No appointments found for this patient.")

                elif ap_choice == str(6):
                    print("Exiting Appointment Manager.")
                    break

        #Closes Hospital Management System
        elif menu_choice == str(4):
            print("Exiting system. Goodbye!")
            break

### Purpose
The purpose of the program is to address the growing challenge where hospitals struggle to maintain adequate records as well as to properly track the status of doctors' apointments
It was created with the aim of completly virtualizing the hospial system- offering capabilities such as doctor management, patient manual as well as appointment management on both the hospital and doctor's level. 

### Features
- Register and view doctors and patients
- Book, complete, and cancel appointments
- View available booking slots for doctors
- Auto-generates patient and doctor IDs
- Generates appointment bills including additional services

### Program Structure
- Person class: Base class for shared attributes
- Patient class: Inherits from Person and manages patient data
- Doctor class: Inherits from Person, manages doctor's calendar and appointments
- Appointment class: Holds appointment details and status
- HospitalSystem class: Core logic to add, manage, and view doctors, patients, and appointments
- Command-line interface in the main block

### How to run
1. Clone the repository or download the script. 
2. Run the python script: hospital_system.py

### Assumptions
To facilitate the smooth usage of this program, the following assumptions should be taken into account: 
  
1) Each doctor's appointment does not exceed an hour.
2) A doctor's working hours runs from 9AM to 4PM.
3) A doctor is expected to be on call and available for every hour on any given day.
4) Doctors' and patients' IDS are generated in a sequential manner.

### Limitations
The followning limitations should be considered during the usage of this application: 

1) No security control nor priviledged access managament has been implemented.
2) Solution is void database management capabilities, therefore resulting in non-persistency of the data gathered.
3) No account was taken into for the momnth of February, which contains 28 months. 
4) History tracking for cancelled appointments is not in place. 


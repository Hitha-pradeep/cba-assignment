# Hospital Appointment System
class Patient:
    def __init__(self, patient_id, name, age, appointment_hour):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.appointment_hour = appointment_hour  # 24-hour format
    def age_category(self):
        if self.age >= 60:
            return "Senior Citizen"
        elif self.age >= 18:
            return "Adult"
        else:
            return "Child"
    def appointment_slot(self):
        if 6 <= self.appointment_hour < 12:
            return "Morning"
        elif 12 <= self.appointment_hour < 17:
            return "Afternoon"
        elif 17 <= self.appointment_hour <= 21:
            return "Evening"
        else:
            return "Outside Working Hours"
    def display_details(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} ({self.age_category()})")
        print(f"Appointment Hour: {self.appointment_hour}:00")
        print(f"Appointment Slot: {self.appointment_slot()}")
        print("---------------")
patient1 = Patient(101, "Alice", 65, 10)
patient2 = Patient(102, "Bob", 30, 14)
patient3 = Patient(103, "Charlie", 12, 18)
patient4 = Patient(104, "David", 45, 22)
patient1.display_details()
patient2.display_details()
patient3.display_details()
patient4.display_details()

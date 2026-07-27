# Hospital Patient Queue
def add_patient(queue, name):
    queue.append(name)
    print(f"Patient '{name}' added to the queue.")
def call_next_patient(queue):
    if queue:
        next_patient = queue.pop(0)  
        print(f"Calling patient: {next_patient}")
    else:
        print("No patients in the queue.")
def display_queue(queue):
    print("\n===== Current Waiting List =====")
    if queue:
        for i, patient in enumerate(queue, start=1):
            print(f"{i}. {patient}")
    else:
        print("No patients waiting.")
    print("================================")
def count_patients(queue):
    print(f"Number of patients waiting: {len(queue)}")
def main():
    queue = []
    while True:
        print("\n===== Hospital Queue Menu =====")
        print("1. Add New Patient")
        print("2. Call Next Patient")
        print("3. Display Waiting List")
        print("4. Show Number of Patients Waiting")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter patient name: ")
            add_patient(queue, name)
        elif choice == 2:
            call_next_patient(queue)
        elif choice == 3:
            display_queue(queue)
        elif choice == 4:
            count_patients(queue)
        elif choice == 5:
            print("Exiting Hospital Patient Queue System...")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()

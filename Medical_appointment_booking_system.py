appointments = []

def book_appointment():
    patient = input("Enter patient name: ")
    doctor = input("Enter doctor name: ")
    date = input("Enter appointment date: ")
    appointments.append({
        "patient": patient,
        "doctor": doctor,
        "date": date
    })
    print("Appointment booked successfully")

def view_appointments():
    if not appointments:
        print("No appointments found")
    else:
        for a in appointments:
            print("Patient:", a["patient"])
            print("Doctor:", a["doctor"])
            print("Date:", a["date"])
            print("------------------")

def main():
    while True:
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()

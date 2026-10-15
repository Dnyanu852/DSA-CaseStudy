
class HospitalPatientRecordSystem:
    def __init__(self, size=10):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, patient_id):
        return sum(ord(ch) for ch in str(patient_id)) % self.size

    # Add patient record
    def add_patient(self, patient_id, name, age, disease, record_ref):
        index = self.hash_function(patient_id)

        # Check whether patient ID already exists
        for patient in self.hash_table[index]:
            if patient["id"] == patient_id:
                print("Patient ID already exists!")
                return

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "disease": disease,
            "record_ref": record_ref
        }

        self.hash_table[index].append(patient)
        print("Patient record added successfully!")

    # Search patient record
    def search_patient(self, patient_id):
        index = self.hash_function(patient_id)

        for patient in self.hash_table[index]:
            if patient["id"] == patient_id:
                print("\n--- Patient Record ---")
                print("Patient ID:", patient["id"])
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])
                print("Medical Record Reference:",
                      patient["record_ref"])
                return

        print("Patient record not found!")

    # Delete patient record
    def delete_patient(self, patient_id):
        index = self.hash_function(patient_id)

        for patient in self.hash_table[index]:
            if patient["id"] == patient_id:
                self.hash_table[index].remove(patient)
                print("Patient record deleted successfully!")
                return

        print("Patient record not found!")

    # Display all patient records
    def display_patients(self):
        print("\n--- All Patient Records ---")
        found = False

        for index, bucket in enumerate(self.hash_table):
            if bucket:
                print("Bucket", index, ":")
                for patient in bucket:
                    print(patient)
                    found = True

        if not found:
            print("No patient records available.")


# Main program
hospital = HospitalPatientRecordSystem()

while True:
    print("\n===== Hospital Patient Record System =====")
    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Delete Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        disease = input("Enter Disease: ")
        record_ref = input("Enter Medical Record Reference: ")

        hospital.add_patient(
            patient_id, name, age, disease, record_ref
        )

    elif choice == "2":
        patient_id = input("Enter Patient ID to search: ")
        hospital.search_patient(patient_id)

    elif choice == "3":
        patient_id = input("Enter Patient ID to delete: ")
        hospital.delete_patient(patient_id)

    elif choice == "4":
        hospital.display_patients()

    elif choice == "5":
        print("Exiting Hospital Patient Record System.")
        break

    else:
        print("Invalid choice! Please try again.")

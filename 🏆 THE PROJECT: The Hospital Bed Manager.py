## 🏆 THE PROJECT: The Hospital Bed Manager

def find_and_update(patient_list, target_id, new_status="Stable"):
    for patient in patient_list:
        if patient["id"] == target_id:
            patient["status"] = new_status
            return True
    return False

ward_patients = [
    {"id": "P01", "name": "Alice", "status": "Admitted"},
    {"id": "P02", "name": "Bob", "status": "Admitted"},
    {"id": "P03", "name": "Charlie", "status": "Critical"}
]

id = input("Please Enter ID: ").upper()
status = input("Please Enter New Status: ").capitalize()
success = find_and_update(ward_patients,target_id=id,new_status=status)

if success:
    print("Patient updated successfully!")
else:
    print("Error: Patient ID not found.")
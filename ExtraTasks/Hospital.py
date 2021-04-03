period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
for day in range(1, period + 1):
    patients = int(input())
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors = doctors + 1
        else:
            doctors = doctors
    if patients <= doctors:
        treated_patients = treated_patients + patients
        untreated_patients = untreated_patients
    else:
        treated_patients = treated_patients + doctors
        untreated_patients = untreated_patients + (patients - doctors)
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

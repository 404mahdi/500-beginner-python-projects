class Patient:
    def __init__(self, id, name, age, bloodgroup, prev=None, next=None):
        self.id = id
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup
        self.prev = prev
        self.next = next
        
        
class WMS:
    patient_id = 1001
    def __init__(self):
        self.patients = Patient(None, None, None, None)
        self.patients.next = self.patients
        self.patients.prev = self.patients
        
    def registerPatient(self, name, age, bloodgroup):
        new_patient = Patient(WMS.patient_id, name, age, bloodgroup)
        last_node = self.patients.prev
        last_node.next = new_patient
        new_patient.prev = last_node
        new_patient.next = self.patients
        self.patients.prev = new_patient
        print()
        print(f'New Patient Registered with id: {WMS.patient_id}')
        print()
        WMS.patient_id += 1
        
    def servePatient(self):
        if self.patients.next == self.patients:
            print()
            print('No patient to serve.')
            print()
        else:
            served_patient = self.patients.next
            next = served_patient.next
            self.patients.next = next
            next.prev = self.patients
            served_patient.next = None
            served_patient.prev = None
            print()
            print(f'Served patient with id: {served_patient.id}')
            print()
            
    def cancelPatient(self, id):
        curr = self.patients.next
        while curr != self.patients:
            if curr.id == id:
                cancelled_patient = curr
                next = curr.next
                prev = curr.prev
                next.prev = prev
                prev.next = next
                cancelled_patient.next = None
                cancelled_patient.prev = None
                print()
                print(f'Cancelled patient with id: {cancelled_patient.id}')
                print()
                break
            if curr.next == self.patients:
                print()
                print(f'patients with {id} not found.')
                print()
            curr = curr.next
            
    def cancelAll(self):
        self.patients.next = self.patients
        self.patients.prev = self.patients
        print()
        print('All patients have been cancelled.')
        print()
        
    def showPatient(self, id):
        curr = self.patients.next
        patient_found = False
        while curr != self.patients:
            if curr.id == id:
                print()
                print(f'ID: {curr.id}\nName: {curr.name}\nAge: {curr.age}\nBlood Group: {curr.bloodgroup}')
                print()
                patient_found = True
            curr = curr.next
        if not patient_found:
            print()
            print(f'Patient with id {id} not found.')
            print()
            
    def showAll(self):
        curr = self.patients.next
        while curr != self.patients:
            print()
            print(f'ID: {curr.id}\nName: {curr.name}\nAge: {curr.age}\nBlood Group: {curr.bloodgroup}')
            print()
            curr = curr.next
            
    def canDoctorGoHome(self):
        if self.patients.next == self.patients:
            print()
            print('Yesss! Please...')
            print()
        else:
            print()
            print("Nooo! Can't you see this big line?") 
            print()
            
    def reverseLine(self):
        curr = self.patients.next
        while curr != self.patients:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp
            curr = temp
        temp = self.patients.next
        self.patients.next = self.patients.prev
        self.patients.prev = temp
        print()
        print('Line reversed')
        print()
        
        

def main():
    wms = WMS()
    while True:
        print("1. Register Patient")
        print("2. Serve Patient")
        print("3. Show Patient")
        print("4. Show All Patients")
        print("5. Cancel Patient")
        print("6. Cancel All Patients")
        print("7. Can Doctor Go Home")
        print("8. Reverse The Line")
        print("9. Exit")
        
        choice = input('Enter your Choice: ')
        
        if choice == '1':
            name = input('Enter patient Name: ')
            age = input('Enter Patients Age: ')
            bloodgroup = input('Enter Patients Bloodgroup: ')
            
            wms.registerPatient(name, age, bloodgroup)
        
        elif choice == '2':
            wms.servePatient()
            
        elif choice == '3':
            while True:
                try:
                    id = int(input('Enter Patient ID: '))
                    break
                except:
                    print()
                    print('Input valid id!')
                    print()
                    
            wms.showPatient(id)
        
        elif choice == '4':
            wms.showAll()
            
        elif choice == '5':
            while True:
                try:
                    id = int(input('Enter Patient ID: '))
                    break
                except:
                    print()
                    print('Input valid id!')
                    print()
            
            wms.cancelPatient(id)
        
        elif choice == '6':
            wms.cancelAll()
            
        elif choice == '7':
            wms.canDoctorGoHome()
            
        elif choice == '8':
            wms.reverseLine()
            
        elif choice == '9':
            break
        
        else:
            print()
            print('Invalid input!')
            print()


main()
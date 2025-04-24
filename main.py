from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Program:
    name : str
    
@dataclass
class Client:
    id: str
    name: str
    age: int
    enrolled_programs: list= field(default_factory=list) 

#store all programs and clients in memory
programs = []
clients = []  

#function to create a health program
def create_program(name):
    program = Program(name=name)
    programs.append(program)
    print(f"Program '{name}' created succesfully.")
    
#function to register a new client
def register_client(name, age):
    client = Client(id=str(uuid4()), name=name, age=age) 
    clients.append(client)
    print(f"Client '{name}' registered successfully with ID: {client.id}")        

#function to enroll a client in a program
def enroll_client(client_id, program_name):
    #check if program exists
    program_name = [p.name for p in programs] 
    if program_name not in Program:
        print(f"Program '{program_name}' does not exist.")
        return
    #find the cient
    for client in clients:
        if client.id == client_id:
            if program_name in client.enrolled_programs:
                print(f"Client '{client.name}' is already enrolled  in '{program_name}'.")
            else:
                client.enrolled_programs.append(program_name)
                print(f"Enrolled '{client.name}' in '{program_name}'.") 
            return       
    print("Client not found.")

#search for client by name
def find_client_by_name(name):
    found = False
    for client in clients:
        if client.name.lower() == name.lower():
            print(f"Found client: {client.name}, ID: {client.id}, Age: {client.age}")
            print(f"Enrolled Programs: {client.enrolled_programs}")
            found = True
    if not found:
        print(f"No client found with that name.")

#view client profile
def view_client_profile(client_id):
    for client in clients:
        if client.id == client_id:
            print(f"Client Profile")
            print("-----------------------------------")
            print(f"ID : {client.id}")    
            print(f"Name : {client.name}")
            print(f"Age : {client.age}")
            print(f"Programs : {','.join(client.enrolled_programs)if client.enrolled_programs else 'None'}")
            return
        print("Client not found.")

import json   
#function to expose client profile via an API
def get_client_profile(client_id):
    for client in clients:
        if client.id == client_id:
            profile = {
                "id": client.id,
                "name": client.name,
                "age": client.age,
                "enrolled_programs": client.enrolled_programs
            }  
            print(" API Response (JSON)")
            print("-------------------------------------------------")
            print(json.dumps(profile, indent=4))
            return profile
        print("Client not found.")
        return None   
    

#CLI interface for the program
def main_menu():
    while True:
        print("CEMA Health Information System")
        print("========================================")
        print("1. Create a Health Program")
        print("2. Register a New Client")
        print("3. Enroll a client in a program")
        print("4. Search for client by name")
        print("5. View Client Profile")
        print("6. Get client profile via API")
        print("0. Exit")
        choice = input("Select an option:")
        
        if choice == '1':
            name = input("Enter program name:")
            create_program(name)
            
        elif choice == '2':
            name = input("Enter client name:")
            age = input("Enter client age:")
            register_client(name, age) 
            
        elif choice == '3':
            client_id = input("Enter cient ID:")
            program = input("Enter program name to enroll in:")
            enroll_client(client_id, program) 
        
        elif choice == '4':
            name = input("Enter client name to search:")
            find_client_by_name(name)
        
        elif choice == '5':
            client_id = input("Enter client ID to view profile:")
            view_client_profile(client_id)
        
        elif choice == '6':
            client_id = input("Enter client ID to get API JSON:")
            get_client_profile(client_id)  
        
        elif choice == '0':
            print(" Exiting system...Goodbye!")
            break 
        else:
            print("Invalid option. Please try again.")
main_menu()                              
    
                       
        
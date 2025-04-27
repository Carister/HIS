This is a Health Information System built with Flask, designed to manage clients and health programs. 
The system allows for the creation of health programs, client registration, client enrollment in health programs, and viewing client profiles. 
It also exposes client profiles via a RESTful API for external systems to access.
Deployment to AWS Cloud is in progress

#Features
Health Program Management: Create and manage health programs.
Client Registration: Add clients with basic details like name and age.
Client Enrollment: Enroll clients in one or more health programs.
Client Search: Search for clients by name.
Profile View: View client profiles, including enrolled health programs.
API Integration: Expose client profiles through an API

#Installation
Make sure you have Python installed
1. Clone the repository:
   git clone [git@github.com:Carister/HIS.git](https://github.com/Carister/HIS.git)
2. Create a virtual environment and activate it
   python -m venv venv
   source venv/bin/activate
   Install the required dependencies
   pip install -r requirements.txt
3. Run the application
   python app.py
4. Access the app
   Open your browser and navigate to:
   http://127.0.0.1:5000/

#Usage
Health Program Creation
URL: /create-program
Method: GET (to show the form) and POST (to submit the form)
Description: Use this to create new health programs like TB, Malaria, HIV.

Client Registration
URL: /register-client
Method: GET (to show the registration form) and POST (to submit the form)
Description: Register new clients by providing their name and age.

Enroll Client in Program
URL: /enroll-client
Method: GET (to show the enrollment form) and POST (to submit the form)
Description: Enroll a client in one or more health programs.

Client Search
URL: /search-client
Method: GET
Description: Search for clients by name and view their profile.

View Client Profile
URL: /client-profile/<client_name>
Method: GET
Description: View a client's profile, including their details and enrolled programs.

API for Client Profiles
URL: /api/client/<client_name>
Method: GET
Description: Retrieve client profile data in JSON format.

#Testing
Manual Testing: You can manually test the application by interacting with the UI in your browser. Check the following functionalities:
1. Create health programs
2. Register clients
3. Enroll clients in programs
4. Search for clients
5. View client profiles
6. API Testing: Use tools like Postman or Curl to test the API endpoints for client profiles.

#Future Improvements
1. Database Integration: Replace in-memory data with a persistent database like SQLite or MySQL.
2. User Authentication: Add user authentication and roles (Admin, User).
3. Improved UI/UX: Enhance the user interface and experience with modern JavaScript frameworks like React.
4. Security Enhancements: Implement security best practices such as encryption for sensitive data and secure login mechanisms.


    
   
      

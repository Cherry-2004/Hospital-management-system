.

🏥 Hospital Management System (Flask)
📌 Project Description
The Hospital Management System is a web-based application developed using Python Flask.
It helps in managing hospital operations such as patient records, doctor details, and appointments in a digital and efficient manner.
This project is designed as a final year academic project and follows proper software development practices.

🎯 Objectives


To digitalize hospital record management


To reduce manual paperwork


To manage patients, doctors, and appointments efficiently


To provide secure access using login authentication



🛠️ Technologies Used
LayerTechnologyFrontendHTML, CSS, BootstrapBackendPython (Flask)DatabaseSQLiteServerFlask Development ServerArchitectureMVC (Model–View–Controller)

📂 Project Structure
HMS/
│
├── app.py
├── create_tables.py
├── hospital.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── hospital.jpg
│       ├── patient.png
│       ├── doctor.png
│       └── appointment.png
│
└── templates/
    ├── base.html
    ├── login.html
    ├── index.html
    ├── dashboard.html
    ├── add_patient.html
    ├── add_doctor.html
    ├── appointment.html
    ├── view_patients.html
    ├── view_doctors.html
    └── view_appointments.html


⚙️ Features


Admin Login System


Add Patient


View Patients


Add Doctor


View Doctors


Book Appointment


View Appointments


Session-based Authentication


Responsive UI using Bootstrap



🔐 Login Credentials 
Username: admin
Password: admin


▶️ How to Run the Project
1️⃣ Install Required Package
pip install flask


2️⃣ Create Database Tables (Run Once)
python create_tables.py


3️⃣ Start Flask Server
python app.py


4️⃣ Open in Browser



🧠 How It Works


Flask handles routing and server logic


HTML templates are rendered using Jinja


SQLite stores all hospital data


Admin authentication is managed using Flask sessions



🧪 Database Tables


admin – stores admin login credentials


patient – stores patient details


doctor – stores doctor details


appointment – stores appointment records



📊 Future Enhancements


Password encryption


Doctor login module


Search and filter options


Report generation (PDF/Excel)


Dashboard analytics



🎓 Academic Relevance
This project demonstrates:


CRUD operations


Web development using Flask


Database integration


MVC architecture


Secure login system


It is suitable for final-year project submission and viva examination.

📜 License
This project is developed for educational purposes only.


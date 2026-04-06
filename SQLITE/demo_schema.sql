-- Hospital Management Database
-- Task:
-- Create schema and queries for a Hospital Management System.
-- Instructions:
-- • Tables: Doctors, Patients, Appointments.
-- • Use AI to define constraints (unique IDs, valid dates).
-- • Generate queries:
-- • List all appointments for a specific doctor.
-- • Retrieve patient history by patient ID.
-- • Count total patients treated by each doctor.
-- Expected Output:
-- • Normalized schema and SQL queries with joins.
-- Create Doctors table
CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    specialty TEXT NOT NULL
);
-- Create Patients table
CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL
);
-- Create Appointments table
CREATE TABLE Appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
-- Query 1: List all appointments for a specific doctor
SELECT a.appointment_id, p.first_name AS patient_first_name, p.last_name AS patient_last_name, a.appointment_date
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = ?; -- Replace ? with the specific doctor_id
-- Query 2: Retrieve patient history by patient ID
SELECT a.appointment_id, d.first_name AS doctor_first_name, d.last_name AS doctor_last_name, a.appointment_date
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = ?; -- Replace ? with the specific patient_id
-- Query 3: Count total patients treated by each doctor
SELECT d.doctor_id, d.first_name, d.last_name, COUNT(DISTINCT a
.patient_id) AS total_patients
FROM Doctors d
LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id;

--INSERT sample data into Doctors table
INSERT INTO Doctors (first_name, last_name, specialty) VALUES ('John', 'Doe',
    'Cardiology');
INSERT INTO Doctors (first_name, last_name, specialty) VALUES ('Jane', 'Smith',
    'Neurology');
--INSERT sample data into Patients table
INSERT INTO Patients (first_name, last_name, date_of_birth) VALUES ('Alice', 'Johnson',
    '1980-05-15');
INSERT INTO Patients (first_name, last_name, date_of_birth) VALUES ('Bob', 'Brown',
    '1990-08-22');
--INSERT sample data into Appointments table
INSERT INTO Appointments (doctor_id, patient_id, appointment_date) VALUES (1, 1,
    '2024-07-01');
INSERT INTO Appointments (doctor_id, patient_id, appointment_date) VALUES (1, 2,
    '2024-07-02');
INSERT INTO Appointments (doctor_id, patient_id, appointment_date) VALUES (2, 1,
    '2024-07-03');
    

SELECT * FROM Doctors;
SELECT * FROM Patients;
SELECT * FROM Appointments;
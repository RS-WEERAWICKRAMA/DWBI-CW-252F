\copy dim_date FROM 'C:/Users/C Y B E X/.gemini/antigravity/scratch/cw-c/dim_date.csv' WITH (FORMAT csv, HEADER true);
\copy dim_clinic FROM 'C:/Users/C Y B E X/.gemini/antigravity/scratch/cw-c/dim_clinic.csv' WITH (FORMAT csv, HEADER true);
\copy dim_doctor FROM 'C:/Users/C Y B E X/.gemini/antigravity/scratch/cw-c/dim_doctor.csv' WITH (FORMAT csv, HEADER true);
\copy dim_patient FROM 'C:/Users/C Y B E X/.gemini/antigravity/scratch/cw-c/dim_patient.csv' WITH (FORMAT csv, HEADER true);
\copy fact_appointment(patient_key, doctor_key, clinic_key, date_key, appointment_id, wait_minutes, consultation_minutes, fee) FROM 'C:/Users/C Y B E X/.gemini/antigravity/scratch/cw-c/fact_appointment.csv' WITH (FORMAT csv, HEADER true);

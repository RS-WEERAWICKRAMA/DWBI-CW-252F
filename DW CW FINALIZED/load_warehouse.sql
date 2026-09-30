-- Coursework Part C: Warehouse Data Load
-- Tools: psql \copy

-- Load Dimensions First
\copy dim_date FROM 'dim_date.csv' WITH (FORMAT csv, HEADER true);
\copy dim_clinic FROM 'dim_clinic.csv' WITH (FORMAT csv, HEADER true);
\copy dim_doctor FROM 'dim_doctor.csv' WITH (FORMAT csv, HEADER true);
\copy dim_patient FROM 'dim_patient.csv' WITH (FORMAT csv, HEADER true);

-- Load Fact Table Last
\copy fact_appointment(patient_key, doctor_key, clinic_key, date_key, appointment_id, wait_minutes, consultation_minutes, fee) FROM 'fact_appointment.csv' WITH (FORMAT csv, HEADER true);

-- Verification: Row Counts
SELECT 'dim_patient' AS table_name, COUNT(*) AS row_count FROM dim_patient
UNION ALL SELECT 'dim_doctor', COUNT(*) FROM dim_doctor
UNION ALL SELECT 'dim_clinic', COUNT(*) FROM dim_clinic
UNION ALL SELECT 'dim_date', COUNT(*) FROM dim_date
UNION ALL SELECT 'fact_appointment', COUNT(*) FROM fact_appointment;

-- Verification: Referential Integrity
SELECT 
    COUNT(CASE WHEN p.patient_key IS NULL THEN 1 END) AS orphan_patient_fk,
    COUNT(CASE WHEN d.doctor_key IS NULL THEN 1 END) AS orphan_doctor_fk,
    COUNT(CASE WHEN c.clinic_key IS NULL THEN 1 END) AS orphan_clinic_fk,
    COUNT(CASE WHEN dt.date_key IS NULL THEN 1 END) AS orphan_date_fk
FROM fact_appointment f
LEFT JOIN dim_patient p ON f.patient_key = p.patient_key
LEFT JOIN dim_doctor d  ON f.doctor_key = d.doctor_key
LEFT JOIN dim_clinic c  ON f.clinic_key = c.clinic_key
LEFT JOIN dim_date dt   ON f.date_key = dt.date_key;

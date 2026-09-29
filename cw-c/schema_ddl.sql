-- Coursework Part C: Star Schema DDL
-- Database: PostgreSQL

DROP TABLE IF EXISTS fact_appointment CASCADE;
DROP TABLE IF EXISTS dim_patient CASCADE;
DROP TABLE IF EXISTS dim_doctor CASCADE;
DROP TABLE IF EXISTS dim_clinic CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;

-- 1. dim_patient
CREATE TABLE dim_patient (
    patient_key     SERIAL PRIMARY KEY,
    patient_id      VARCHAR(10) NOT NULL UNIQUE,
    gender          VARCHAR(10) NOT NULL,
    date_of_birth   DATE NOT NULL,
    district        VARCHAR(50) NOT NULL
);

-- 2. dim_doctor
CREATE TABLE dim_doctor (
    doctor_key      SERIAL PRIMARY KEY,
    doctor_id       VARCHAR(10) NOT NULL UNIQUE,
    doctor_name     VARCHAR(100) NOT NULL,
    specialty       VARCHAR(50) NOT NULL
);

-- 3. dim_clinic
CREATE TABLE dim_clinic (
    clinic_key      SERIAL PRIMARY KEY,
    clinic_id       VARCHAR(10) NOT NULL UNIQUE,
    clinic_name     VARCHAR(100) NOT NULL,
    city            VARCHAR(50) NOT NULL,
    province        VARCHAR(50) NOT NULL
);

-- 4. dim_date (2025 Calendar)
CREATE TABLE dim_date (
    date_key        INT PRIMARY KEY,
    full_date       DATE NOT NULL UNIQUE,
    year            INT NOT NULL,
    quarter         INT NOT NULL,
    quarter_name    VARCHAR(10) NOT NULL,
    month           INT NOT NULL,
    month_name      VARCHAR(20) NOT NULL,
    day             INT NOT NULL,
    day_name        VARCHAR(20) NOT NULL,
    day_of_week     INT NOT NULL,
    is_weekend      BOOLEAN NOT NULL
);

-- 5. fact_appointment
CREATE TABLE fact_appointment (
    appointment_key      SERIAL PRIMARY KEY,
    patient_key          INT NOT NULL REFERENCES dim_patient(patient_key),
    doctor_key           INT NOT NULL REFERENCES dim_doctor(doctor_key),
    clinic_key           INT NOT NULL REFERENCES dim_clinic(clinic_key),
    date_key             INT NOT NULL REFERENCES dim_date(date_key),
    appointment_id       VARCHAR(20) NOT NULL,
    wait_minutes         INT NOT NULL,
    consultation_minutes INT NOT NULL,
    fee                  NUMERIC(10, 2) NOT NULL
);

CREATE INDEX idx_fact_patient ON fact_appointment(patient_key);
CREATE INDEX idx_fact_doctor ON fact_appointment(doctor_key);
CREATE INDEX idx_fact_clinic ON fact_appointment(clinic_key);
CREATE INDEX idx_fact_date ON fact_appointment(date_key);
